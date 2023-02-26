from __future__ import annotations

"""
This file implements the single elimination style tournament, where any loss means you exit the competition. We can represent
a tournament using the binary operator `+`, which means 'the remaining player from the
upper bracket will play off against the remaining player from the lower bracket.
"""
__author__ = "Scaffold by Jackson Goerner, Code by Matt Ch'ng, Ravindu Gamage, Eric Theov, Adrian Louis"

from poke_team import PokeTeam
from battle import Battle
from linked_list import LinkedList
from stack_adt import ArrayStack
from queue_adt import CircularQueue

class Tournament:
    """
    Initialises the tournament class. A battle instance can be passed in, which all tournament games
    will be run with. 
    """
    
    def __init__(self, battle: Battle|None=None) -> None:
        """
        Initialises the tournament class. A battle instance can be passed in, which all tournament games
        will be run with. 

        Arguments: 
            self: obj
            battle(instance of Battle class): obj

        Returns: 
            None

        Total time complexity: O(c) where c is the complexity of calling the class Battle()
        """
        if battle: # O(1)
            self.battle = battle # O(1)
        else:
            self.battle = Battle() # O(c) where c is the complexity of calling the class Battle()
            self.battle_mode = None # O(1)
            self.tournament_teams = None # O(1)
            self.battle_order = None # O(1)
            self.battle_order_position = 0 # O(1)
            self.battle_stack = None # O(1)
            self.teams = 0 # O(1)
            self.is_reversed = False # O(1)


    def set_battle_mode(self, battle_mode: int) -> None:
        """
        Set the battle mode for all randomly generated teams.

        Arguments: 
            self: obj
            battle_mode: int

        Returns: 
            None

        Total time complexity: O(1)
        """
        self.battle_mode = battle_mode # O(1)
            

    def is_valid_tournament(self, tournament_str: str) -> bool:
        """
        Returns true if the tournament_str passed represents a valid tournament.

        Arguments: 
            self: obj
            tournament_str(contains tournament contestants and '+'): str

        Returns: 
            True/False : boolean

        Total time complexity: O(n)

        """
        s = tournament_str.split(' ') # O(1)
        self.teams = [team for team in s if team != '+'] # O(n)
        stack = ArrayStack(len(self.teams)) # O(1)
        self.battle_order = s # O(1)
        for item in s: # O(n)
            if item != '+': # O(1)
                stack.push(item) # O(1)
            else:
                if len(stack) >= 2: # O(1)
                    item1 = stack.pop() # O(1)
                    item2 = stack.pop() # O(1)
                    stack.push(item1[0] + item2[0]) # O(1)
                else:
                    raise ValueError("Invalid string") # O(1)
                
        if len(stack) == 1: # O(1)
            return True # O(1)
        else: # O(1)
            raise ValueError() # O(1)

    def start_tournament(self, tournament_str: str) -> None:
        """
        Generates teams based on the tournament_str (it should set the names of each PokeTeam, and use
        PokeTeam.random_team()), but does not play any games

        Arguments: 
            self: obj
            tournament_str(contains tournament contestants and '+'): str

        Returns: 
            None

        Total time complexity: O(n)
        """
        if self.is_valid_tournament(tournament_str): # O(1)
            items = tournament_str.split(' ') # O(1)
            self.tournament_teams = CircularQueue(len(self.teams)) # O(n)
            for name in self.teams: # O(n)
                self.tournament_teams.append(PokeTeam.random_team(name, self.battle_mode)) # O(1)
        else:
            raise  # O(1)

    def advance_tournament(self) -> tuple[PokeTeam, PokeTeam, int] | None:
        """
        Simulates one battle of the tournament, following the order of the previously given tournament string (Each + represents a game, and each game is simulated from left
        to right). If no games are remaining, None should be returned.

        Arguments: 
            self: obj

        Returns: 
            tuple containing two instances of PokeTeam and an integer

        Total time complexity: O(n)

        """
        self.battle_stack = ArrayStack(len(self.teams)) # O(1)
        for item in self.battle_order: # O(n)
            if item != '+': # O(1)
                self.battle_stack.push(self.tournament_teams.serve()) # O(1)
            else: # O(1)
                if len(self.battle_stack) >= 2: # O(1)
                    team1 = self.battle_stack.pop() # O(1)
                    team2 = self.battle_stack.pop() # O(1)
                    res = self.battle.battle(team1, team2) # O(1)
                    self.battle_stack.push(team1 if res == 1 else team2) # O(1)
                    break

        return (team1, team2, res) # O(1)


    def linked_list_of_games(self) -> LinkedList[tuple[PokeTeam, PokeTeam]]:
        """
        Returns a linked list, containing a tuple for each match of the 
        tournament, in the same order as linked_list_of_games does. 

        Arguments: 
            self: obj

        Returns: 
            Linkedlist adt

        Total time complexity: O(n)
        """
        l = LinkedList()
        while True: # O(n)
            res = self.advance_tournament() # O(1)
            if res is None: # O(1)
                break # O(1)
            l.insert(0, (res[0], res[1])) # O(1)
        return l # O(1)
    
    def linked_list_with_metas(self) -> LinkedList[tuple[PokeTeam, PokeTeam, list[str]]]:
        """
        Returns a linked list, containing a tuple for each match of the 
        tournament, in the same order as linked_list_of_games does. 

        Arguments: 
            self: obj

        Returns: 
            Linkedlist adt

        Total time complexity: O(n)
        """
        l = LinkedList() # O(1)
        while True: # O(n)
            res = self.advance_tournament() # O(1)
            if res is None: # O(1)
                break # O(1)
            team1, team2, outcome = res # O(1)
            meta_types = [] # O(1)
            types = ["FIRE", "GRASS", "WATER", "GHOST", "NORMAL"] # O(1)
            for types, t1_types, t2_types in zip(types, team1.team_numbers, team2.team_numbers): # O(n)
                if not t1_types or not t2_types: # O(1)
                    meta_types.append(types) # O(1)
            print((team1, team2, meta_types)) # O(1)
            l.insert(0, (team1, team2, meta_types)) # O(1)
        return l # O(1)
    

