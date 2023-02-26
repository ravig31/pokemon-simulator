from poke_team import PokeTeam, Action, Criterion
from battle import Battle
from queue_adt import CircularQueue
from random_gen import RandomGen
from stack_adt import ArrayStack
"""
This file implements the battle logic of a tower, in which we start by generating some random PokeTeams, and give each of these
teams a certain amount of lives. Your PokeTeam then faces off against every team in the order generated.

Last modified: 25/09/2022
"""
__author__ = "Scaffold by Jackson Goerner, Code by Eric Theov, Matt Ch'ng, Ravindu Gamage"

class BattleTower:
    """ BattleTower class is used create a tower of Pokemon and set a team which battles through the each team in the tower"""

    def __init__(self, battle: Battle|None=None) -> None:
        """
        Initialises the Battle Tower's battle instance, my team, current team and tower

        Arguments: 
            self: obj
            battle: Battle obj
            
        Returns: 
            None       

        Total time complexity: O(1)  
        """
        self.battle = battle # O(1)
        self.my_team = None # O(1) team fighting through the tower, Type: PokeTeam obj
        self.current_team = None # O(1) current team, which my team is battling, Type: PokeTeam obj
        self.tower = None # O(1) the tower itself, Type: CircularQueue obj

    def set_my_team(self, team: PokeTeam) -> None:
        """
        Sets the my_team attribute to the inputted team

        Arguments: 
            self: obj
            team: PokeTeam obj, inputted team

        Returns: 
            None       

        Total time complexity: O(1)  
        """
        self.my_team = team
    
    def generate_teams(self, n: int) -> None:
        """
        Generates the teams in the tower 

        Arguments: 
            self: obj
            n: int, number of teams in tower 

        Returns: 
            None       

        Total time complexity: O((n^2)log(n))  
        """
        self.tower = CircularQueue(n)
        for i in range(n): # O(n)
            battle_mode = RandomGen.randint(0,1) # O(1)
            current_opponent_team = PokeTeam.random_team(f'{n}', battle_mode) # O(nlog(n))
            current_opponent_team.lives = RandomGen.randint(2,10) # O(1)
            self.tower.append(current_opponent_team) # O(1), appends generated team onto tower

    def __iter__(self):
        """
        Magic method. Creates and returns an iterator for the BattleTower

        Arguments: 
            self: obj

        Returns: 
            BattleTowerIterator: obj       

        Total time complexity: O(1)  
        """
        return BattleTowerIterator(self.battle, self.tower, self.current_team, self.my_team) # O(1)

class BattleTowerIterator:
    """ Iterator for class BattleTower. """
    
    def __init__(self, battle, tower, current_team, my_team):
        """
        Initialises the Battle Tower's battle instance, my team, current team and tower

        Arguments:
            battle: Battle obj, battle instance passed in
            tower: CircularQueue obj, generated tower
            current_team: PokeTeam obj, head of the tower queue
            my_team: PokeTeam obj, my_team passed in
            my_team_loss: bool, whether battle returns a loss for my team

        Returns: 
            None       

        Total time complexity: O(1)  
        """
        self.battle = battle # O(1)
        self.tower = tower # O(1)
        self.current_team = current_team # O(1)
        self.my_team = my_team # O(1)
        self.my_team_loss = False # O(1)

    def __iter__(self):
        """ Returns itself, as required to be iterable. """
        return self # O(1)
        
    def __next__(self):
        """ 
        Returns the current item and moves to the next node.
        :raises StopIteration: if tower is empty (my_team victory) and if my_team_loss == True 

        Arguments: 
            self: obj

        Returns: 
            battle result, my_team, current_team, current_team.lives: tuple  

        Total time complexity: O(n^2 + B + P) 

        """
        if self.my_team_loss: #checks if battle from last iteration returned a loss for my_team
            raise StopIteration # O(1)

        self.current_team = self.tower.serve() # O(1)
        self.current_team.regenerate_team() # O(n^2)
        self.my_team.regenerate_team() # O(n^2)
        
        battle_result = self.battle.battle(self.my_team, self.current_team) # O(B + P)
        
        if battle_result == 2: # O(1)
            self.my_team_loss = True # O(1)
        
        else: #win/draw 
            self.current_team.lives -= 1 # O(1)
            if self.current_team.lives > 0: # O(1)
                self.tower.append(self.current_team) # O(1)

            elif self.tower.is_empty(): # O(1)
                raise StopIteration # O(1)
        
        return (battle_result, self.my_team, self.current_team, self.current_team.lives) # O(1)

    def avoid_duplicates(self) -> None:
        """ 
        Removes all currently alive trainers from the battle tower which have multiple pokemon with the same types.    

        Arguments: 
            self: obj

        Returns: 
            None  

        Total time complexity: O(N * P): N = length of tower, P = length of PokeTeam
        
        """
        for i in range(len(self.tower)): # O(N)  # for each tower in the team 
            self.current_team = self.tower.serve() # O(1) #serve current team off queue
            team_total_len = self.current_team.team.length # O(1) 

            if isinstance(self.current_team.team, ArrayStack): # O(1)
                temp_stack1 = ArrayStack(team_total_len) # O(1)
                for j in range(team_total_len-1): # O(P)
                    temp_stack1.push(self.current_team.team.pop()) # O(1)
                    if temp_stack1.peek().poke_type == self.current_team.team.peek().poke_type: # O(1) #checks for duplicate   
                        break  #if duplicate break for loop
                    elif j == team_total_len - 2: # O(1) #duplicate checked for last element, no duplicates founds
                        self.tower.append(self.current_team) # O(1)  #if no duplicate append back on to tower
                    
            if isinstance(self.current_team.team, CircularQueue):        
                temp_stack2 = ArrayStack(team_total_len) # O(1)
                temp_stack2.push(self.current_team.team.serve()) # O(1) #put first pokemon into temp stack
                for k in range(team_total_len-1): # O(P)
                    head_orig_q = self.current_team.team.serve() # O(1)  #get next pokemon of queue
                    if head_orig_q.poke_type == temp_stack2.peek().poke_type: # O(1) #checks if next pokemon type == first poke type
                        break
                    elif k == team_total_len - 2: # O(1) #if checked through whole team
                        self.tower.append(self.current_team)  #if no duplicate append back on to tower
                    else: # O(1) #if no duplicate pushes next element onto temp stack
                        temp_stack2.push(head_orig_q)
                            



