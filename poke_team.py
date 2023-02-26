from __future__ import annotations
from typing import TypeVar, Generic

from array_sorted_list import ArraySortedList
T = TypeVar('T')
from pokemon import Bulbasaur, Charizard, Charmander, Gastly, Squirtle, Eevee
from random_gen import RandomGen

"""
This file decides the ordering of the party when printing, and how pokemon are retrieved / returned based on battle modes.
It also creates pokemon teams with a team name, team numbers, a battle mode, an AI type. 
AI types give PokeTeams the ability to decide which actions to take in battles (attack, swap, heal, special).

Last modified: 25/09/2022
"""
__author__ = "Scaffold by Jackson Goerner, Code by Matthew Ch'Ng, Ravindu Gamage, Adrian Louis, Eric Theov"

from stack_adt import Stack, ArrayStack
from queue_adt import Queue, CircularQueue
from sorted_list import ListItem, SortedList
from array_sorted_list import ArraySortedList

from enum import Enum, auto
from pokemon_base import PokemonBase

class Action(Enum):
    """
    Enum class creates a set of symbolic names, in this case specified actions, that are bound to unique constant values.
    """
    # auto() automatically assigns numbers in ascending order based on the number of variables in the class
    ATTACK = auto() # O(1)
    SWAP = auto() # O(1)
    HEAL = auto() # O(1)
    SPECIAL = auto() # O(1)
    
class Criterion(Enum):
    """
    Enum class creates a set of symbolic names, in this case specified cireterion, that are bound to unique constant values
    """
    # auto() automatically assigns numbers in ascending order based on the number of variables in the class
    SPD = auto() # O(1)
    HP = auto() # O(1)
    LV = auto() # O(1)
    DEF = auto() # O(1)

class PokeTeam:
    """
    PokeTeam class allows for the allocation of battle modes and gives each team the ability to decide
    which actions to take in battle (ATTACK, SWAP, HEAL, SPECIAL).
    """
    class AI(Enum):
        """
        Enum class creates a set of symbolic names, in this case the battle options, 
        that are bound to unique constant values.
        """
        ALWAYS_ATTACK = auto() # O(1)
        SWAP_ON_SUPER_EFFECTIVE = auto() # O(1)
        RANDOM = auto() # O(1)
        USER_INPUT = auto() # O(1)


    def __init__(self, team_name: str, team_numbers: list[int], battle_mode: int, ai_type: PokeTeam.AI, criterion=None, criterion_value=None) -> None:
        """
        Creates the team and initialises its attributes

        Arguments: 
            self: obj
            team_name: str
            team_numbers: list
            battle_mode: int
            ai_type: obj

        Returns: 
            None

        Total time complexity: O(1)
        """
        self.team_name = team_name # O(1)
        self.team_numbers = team_numbers # O(1)
        self.battle_mode = battle_mode # O(1)
        self.ai_type = ai_type # O(1)
        self.criterion = criterion # O(1)
        self.criterion_value = criterion_value # O(1)
        self.lives = 0 # O(1)
        self.team_size = 0 # O(1)
        self.heals_remaining = 3 # O(1)
        self.is_reversed = False
        self.team = PokeTeam.set_team(self, team_name=self.team_name, team_numbers=self.team_numbers, battle_mode=self.battle_mode, team_size=sum(self.team_numbers), ai_mode=self.ai_type ) # O(n^2)
        

    def set_team(self, team_name, team_numbers, battle_mode, team_size, ai_mode):
        """
        Creates the team and initialises its attributes

        Arguments: 
            self: obj
            team_name: str
            team_numbers: list
            battle_mode: int
            team_size: int
            ai_type: obj

        Returns: 
            None

        Total time complexity: O(nm)
        """

        pokemon = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee] # O(1)
         # stack
        if battle_mode == 0: # O(1)
            pokemon_team = ArrayStack(team_size) # O(1)
            for i in range(len(team_numbers)-1, -1, -1): # O(n)
                for j in range(team_numbers[i]): # O(m)
                    pokemon_team.push(pokemon[i]()) # O(1)
            # two for loops = O(nm)
        # queue
        elif battle_mode == 1:
            pokemon_team = CircularQueue(team_size)
            for i in range(len(team_numbers)): # O(n)
                for j in range(team_numbers[i]): # O(m)
                    pokemon_team.append(pokemon[i]())
            # two for loops = O(nm)
        elif battle_mode == 2: # sorted list
            pokemon_team = ArraySortedList(team_size) # O(1)
            for i in range(len(team_numbers)): # O(n)
                for j in range(team_numbers[i]): # O(m)
                    pokemon_team.add(ListItem(pokemon[i](), -1*(getattr(pokemon[i](), PokeTeam.criterion_to_str(self))))) # O(1)
            # two for loops = O(nm)

        PokeTeam.team = pokemon_team # O(1)
        self.team_size = team_size # O(1)
        return pokemon_team # O(1)

    def criterion_to_str(self) -> str:
        """
        Creates a string representation of the criterion

        Arguments: 
            self: obj

        Returns: 
            String representation: str 

        Total time complexity: O(1)
        """
        if self.criterion == Criterion.SPD: # O(1)
            return 'speed' # O(1)
        elif self.criterion == Criterion.DEF: # O(1)
            return 'defence' # O(1)
        elif self.criterion == Criterion.LV: # O(1)
            return 'level' # O(1)
        else: 
            return 'hp' # O(1)

    @classmethod
    def random_team(cls, team_name: str, battle_mode: int, team_size=None, ai_mode=None, **kwargs):
        """
        Creates a random team given the rules provided in the spec sheet

        Arguments: 
            cls: obj
            team_name: str
            battle_mode: int
            team_size: int
            ai_type: obj
            kwargs(keyword arguments)

        Returns: 
            cls (reference of the PokeTeam)

        Total time complexity: O(nlog(n))
        """
        if not team_size: # O(1)
            team_size = RandomGen.randint(3,6) # O(1)
        unformatted_team_numbers = sorted([0, team_size] + [RandomGen.randint(0,team_size) for i in range(4)]) # O(nlog(n))
        formatted_team_numbers = [] # O(1)
        for i in range(1, len(unformatted_team_numbers)): # O(n)
            diff = unformatted_team_numbers[i] - unformatted_team_numbers[i-1] # O(1)
            formatted_team_numbers.append(diff) # O(1)

        return cls(team_name, formatted_team_numbers, battle_mode, ai_mode) # O(1)


    def return_pokemon(self, poke: PokemonBase) -> None:
        """
        Returns a pokemon into the party (team)

        Arguments: 
            self: obj
            poke(instance of PokemonBase): obj

        Returns: 
            None

        Total time complexity: O(1)
        """
        if not poke.is_fainted(): # O(1)
            if self.battle_mode == 0:
                self.team.push(poke) # O(1)
            elif self.battle_mode == 1: # O(1)
                self.team.append(poke) # O(1)
            else: 
                # if special has been called, return in reverse order
                if not self.is_reversed: # O(1)
                    self.team.add(ListItem(poke, -1*(getattr(poke, PokeTeam.criterion_to_str(self))))) # O(log(n))
                else:
                    self.team.add(ListItem(poke, (getattr(poke, PokeTeam.criterion_to_str(self))))) # O(log(n))
                    
    def retrieve_pokemon(self) -> PokemonBase | None:
        """
        Deploys a pokemon on to the field based on battle mode 

        Arguments: 
            self: obj

        Returns: 
            None

        Total time complexity: O(1)
        """
        if self.battle_mode == 0: # O(1)
            return self.team.pop() # O(1)
        elif self.battle_mode == 1:  # O(1)
            return self.team.serve()  # O(1)
        else:
            return self.team.delete_at_index(0).value  # O(1)

    def special(self) -> None:
        """
        Performs the team's special operation based on battle mode 

        Arguments: 
            self: obj

        Returns: 
            None

        Total time complexity: O(m+n)
        """
        if self.battle_mode == 0: # O(1)
            orig_stack = self.team # O(1)
            final_stack = ArrayStack(self.team_size) # O(1)
            temp_stack = ArrayStack(self.team_size) # O(1)

            if orig_stack.is_empty(): # O(1)
                return # O(1)
            final_stack.push(orig_stack.pop()) # putting first element O(1)
            for i in range(len(orig_stack)-1): # middle elements into temp_stack O(n)
                temp_stack.push(orig_stack.pop()) # O(1)
            for i in range(len(temp_stack)): # middle elements into final O(m)
                final_stack.push(temp_stack.pop()) #O(1)
            final_stack.push(orig_stack.pop()) # putting last element O(1)
            # two separate for loops = O(m+n)
            
            self.team = final_stack # O(1)
        elif self.battle_mode == 1: # O(1)
            orig_q = self.team # O(1)
            temp_stack = ArrayStack(self.team_size) # O(1)
            if orig_q.is_empty():# O(1)
                return # O(1)

            half_len = len(orig_q) // 2 # O(n^2)
            for i in range(half_len): # move half of queue into stack O(n)
                temp_stack.push(orig_q.serve())
            for i in range(len(temp_stack)): # pop from stack and place into queue O(m)
                orig_q.append(temp_stack.pop())
            # two separate for loops = O(m+n)

            self.team = orig_q # O(1)
        else: 
            orig_list = self.team
            temp_stack = ArrayStack(self.team_size) # create a stack O(1)
            final_list = ArraySortedList(self.team_size) # create a sorted list O(1)
            if orig_list.is_empty(): # O(1)
                return # O(1)
            for i in range(len(orig_list)): # O(n)
                poke = orig_list.__getitem__(i).value # O(1)
                if not self.is_reversed: # O(1)
                    final_list.add(ListItem(poke, getattr(poke, PokeTeam.criterion_to_str(self)))) # O(log(n))
                else:
                    final_list.add(ListItem(poke, -1*getattr(poke, PokeTeam.criterion_to_str(self)))) # O(log(n))
            self.is_reversed = not self.is_reversed # O(1)
            self.team = final_list # O(1)


    def regenerate_team(self) -> None: 
        """
        Regenerate the team from the same battle numbers. Used to make a team ready for another battle

        Arguments: 
            self: obj

        Returns: 
            None

        Total time complexity: O(nm)
        """
        team_numbers = self.team_numbers # O(1)
        pokemon = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee] # O(1)
        if self.battle_mode == 0: # O(1)
            self.team = ArrayStack(sum(team_numbers)) # O(n)
            for i in range(len(team_numbers)-1,-1,-1): #O(n)
                for j in range(team_numbers[i]): #O(m) -> nested for loops = O(nm)
                    self.team.push(pokemon[i]())  # O(1) 
        if self.battle_mode == 1:  # O(1)
            self.team = CircularQueue(sum(team_numbers))  # O(n)
            for i in range(len(team_numbers)):  # O(n)
                for j in range(team_numbers[i]):  # O(m) -> nested for loops = O(nm)
                    self.team.append(pokemon[i]())  # O(1)
        if self.battle_mode == 2: 
            self.team = ArraySortedList(sum(team_numbers)) # O(n)
            for i in range(len(team_numbers)):# O(n)
                for j in range(team_numbers[i]):# O(n)
                    self.team.add(ListItem(pokemon[i](), -1*(getattr(pokemon[i](), 'hp'))))# O(n) -> nested for loops = O(nm)
        self.heals_remaining = 3 # O(n)

    def __str__(self):
        """
        Creates a string representation of the pokemon and its statistics

        Arguments: 
            self: obj

        Returns: 
            String representation: str 

        Total time complexity: O(n)
        """
        pokemon_list = [] # O(1)
        temp_team = self.team # O(1)
        if self.battle_mode == 0: # O(1)
            for i in range(self.team.length): # O(n)
                pokemon = self.team.pop() # O(1)
                pokemon_list.append(f"LV. {pokemon.level} {pokemon.poke_name}: {pokemon.hp} HP") # O(1)
        elif self.battle_mode == 1: # O(1)
            for i in range(self.team.length):
                pokemon = self.team.serve()# O(1)
                pokemon_list.append(f"LV. {pokemon.level} {pokemon.poke_name}: {pokemon.hp} HP")# O(1)
        else:
                for i in range(self.team.length):# O(n)
                    pokemon = self.team# O(1)
                    pokemon_list.append(f"LV. {pokemon[i].value.level} {pokemon[i].value.poke_name}: {pokemon[i].value.hp} HP")# O(1)

            
        pokemon_list = str(pokemon_list).replace("'", "") # O(n)
        self.team = temp_team # O(1)
        return f"{self.team_name} ({self.battle_mode}): " + pokemon_list  # O(1)

    def is_empty(self):
        """
        Checks if team is currentyl empty

        Arguments: 
            self: obj

        Returns: 
            True/False

        Total time complexity: O(1)
        """

        return len(self.team) == 0 # O(1)

    def choose_battle_option(self, my_pokemon: PokemonBase, their_pokemon: PokemonBase) -> Action:
        """
        Represents the the AI of the pokemon. Decides on an action depending on the pokemon currently in the field.

        Arguments: 
            self: obj
            my_pokemon: obj
            their_poke: obj

        Returns: 
            An action (instance of the Action class): obj

        Total time complexity: O(n)
        """
        if self.ai_type == PokeTeam.AI.USER_INPUT: #O(1)
            valid_input = False #O(1)
            while not valid_input:  #O(n)
                user_choice = input(f"Choose your mode: \
                                    'A' = ATTACK \
                                    'S' = SWAP \
                                    'H' = HEAL (heals remaining: {self.heals_remaining})\
                                    'X' = SPECIAL")  #O(1)
                                    
                if user_choice == 'A':  #O(n)
                    return Action.ATTACK  #O(1)
                elif user_choice == 'S':  #O(n)
                    return Action.SWAP  #O(1)
                elif user_choice == 'H':  #O(n)
                    if self.heals_remaining == 0: #O(1)
                        print('No heals remaining')  #O(1) 
                        continue #O(1)
                    self.heals_remaining -= 1  #O(1)
                    return Action.HEAL #O(1)
                elif user_choice == 'X': #O(n)
                    return Action.SPECIAL #O(1)
                else:
                    print('Please enter a valid input') #O(1)

        elif self.ai_type == PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE:
            types = [['Fire', 'Water'], ['Water', 'Grass'], 
                    ['Grass', 'Fire'], ['Ghost', 'Ghost']]  #O(1)
            for i in range(len(types)):  #O(n)
                if my_pokemon.poke_type == types[i][0] and their_pokemon.poke_type == types[i][1]:  #O(1)
                    return Action.SWAP  #O(1)

            return Action.ATTACK  #O(1)
            
        elif self.ai_type == PokeTeam.AI.ALWAYS_ATTACK:  #O(1)
            return Action.ATTACK  #O(1)

        else:
            actions = list(Action)  #O(1)
            # if no more heals remaining, remove heal option
            if self.heals_remaining == 0:  #O(1)
                actions.remove(Action.HEAL) # O(n)
            return actions[RandomGen.randint(0, len(actions)-1)] # O(n)
                

    @classmethod
    def leaderboard_team(cls):
        raise NotImplementedError()

# if __name__ == "__main__":
#     print(list(Action))
#     RandomGen.set_seed(123456789)
#     t = PokeTeam.random_team("Cynthia", 0)
#     pokemon = []
#     while not t.is_empty():
#         pokemon.append(t.retrieve_pokemon())
#     expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
#     self.assertEqual(len(pokemon), len(expected_classes))
#     for p, e in zip(pokemon, expected_classes):
#         self.assertIsInstance(p, e)