from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from referential_array import ArrayR, T
from stack_adt import ArrayStack
from random_gen import RandomGen

"""
This file implements all the features required for battles to work, which includes health calculations, level calculations,
fainting, statistics, string representations, defending/attacking and evolution.

Last modified: 25/09/2022
"""
__author__ = "Scaffold by Jackson Goerner, Code by Matt Ch'ng, Eric Theov, Ravindu Gamage, Adrian Louis"

class PokemonBase:

    """ Pokemon base class is used to store all the pokemon's features required for battle"""

    def __init__(self, hp: int, poke_type) -> None:
        """
        Initialises the Pokemon's hp, type and status

        Arguments: 
            self: obj
            hp: int
            
        Returns: 
            None       

        Total time complexity: O(1)  
        """
        self.hp = hp # O(1)
        self.poke_type = poke_type # O(1)
        self.status = 'free' # O(1)


    def is_fainted(self) -> bool:
        """
        Checks if the pokemon has fainted (hp has reached 0).

        Arguments: 
            self: obj

        Returns: 
            True/False 

        Total time complexity: O(1)
        """
        if self.hp <= 0: # Comparison = O(1)
            return True # return a boolean value = O(1)
        else:
            return False # return a boolean value = O(1)

    @abstractmethod
    # this method is implemented in the child class 'Pokemon' to update a pokemon's statistics when leveling up
    def level_up(self) -> None:
        """
        Increments a pokemon's level

        Arguments: 
            self: obj

        Returns: 
            None 

        Total time complexity: O(1)
        """
        self.level += 1 # O(1)
        
    def get_poke_name(self) -> str:
        """
        Accesses a pokemon's name

        Arguments: 
            self: obj

        Returns: 
            Pokemon's name: str 

        Total time complexity: O(1)
        """
        return self.poke_name #O(1)

    def get_level(self) -> int:
        """
        Accesses a pokemon's level

        Arguments: 
            self: obj

        Returns: 
            Pokemon's level: int 

        Total time complexity: O(1)
        """
        return self.level #O(1)
        
    def get_hp(self) -> int:
        """
        Accesses a pokemon's hp

        Arguments: 
            self: obj

        Returns: 
            Pkemon's hp: int

        Total time complexity: O(1)
        """
        if self.hp < 0: # comparison = O(1)
            return 0 # O(1)
        return self.hp # 0(1)

    def get_speed(self) -> int:
        """
        Accesses a pokemon's speed

        Arguments: 
            self: obj

        Returns: 
            Pokemon's speed: int 

        Total time complexity: O(1)
        """
        return self.speed # O(1)

    def get_attack_damage(self) -> int:
        """
        Accesses a pokemon's attack damage

        Arguments: 
            self: obj

        Returns: 
            Pokemon's attack damage: int 

        Total time complexity: O(1)
        """
        return self.attack_damage #O(1)

    def get_defence(self) -> int:
        """
        Accesses a pokemon's defence calculation

        Arguments: 
            self: obj

        Returns: 
            Pokemon's defence calculation: int 

        Total time complexity: O(1)
        """
        return self.defence # O(1)

    def get_status(self) -> str:
        """
        Accesses a pokemon's status

        Arguments: 
            self: obj

        Returns: 
            Pokemon's status: str 

        Total time complexity: O(1)
        """
        return self.status # O(1)

    def lose_hp(self, lost_hp: int) -> None:
        """
        Decrements a pokemon's hp and ensures that a pokemon's hp does not go below zero

        Arguments: 
            self: obj
            lost_hp: int

        Returns: 
            None 

        Total time complexity: O(1)
        """
        if self.hp - lost_hp > 0: # O(1)
            self.hp -= lost_hp # O(1)
        else:
            self.hp = 0 # O(1)

    @abstractmethod
    # this method is implemented in the child class 'Pokemon' as each pokemon has unique defence calculations
    def defend(self, damage: int) -> None:
        pass

    def attack(self, other: PokemonBase, confusion_chance=None):
        """
        Calculates a pokemon's attack damage based on type effectiveness

        Arguments: 
            self: obj
            lost_hp: int

        Returns: 
            None 

        Total time complexity: O(n + m + k^2)
        Where n is the number of types, m is comparison of strings, k is the cost of arithmetic operations
        """

        type_effectiveness_table = [
            [1,2,0.5,1,1], # fire
            [0.5, 1, 2, 1, 1], # grass
            [2, 0.5, 1, 1, 1], # water
            [1.25, 1.25, 1.25, 2, 0], # ghost
            [1.25, 1.25, 1.25, 0, 1] # normal
            ] # O(1)

        types = ['Fire', 'Grass', 'Water', 'Ghost', 'Normal'] # creating list = O(1)

        type_1 = types.index(self.poke_type) # O(n) where n is the len(types)
        
        type_2 = types.index(other.poke_type) # O(n) where n is the len(types)

        type_multiplier = type_effectiveness_table[type_1][type_2] # O(1)
        
        # status effects on attack damage 
        if self.status == "burn": # O(m)
            damage = self.attack_damage // 2 # O(k^2)
        elif self.status == "sleep": # O(m)
            return # O(1)
        else:
            damage = self.attack_damage # O(1)

        # redirecting attack
        if self.status == "confuse": # O(m)
            if confusion_chance == None: # O(1)
                confusion_chance = RandomGen.random_chance(0.5) # O(1)
            if confusion_chance: # O(1)
                self.hp -= self.attack_damage #O(1)
            else: # attack normally
                other.defend(int(damage * type_multiplier)) # O(1)
        else:
            other.defend(int(damage * type_multiplier)) # O(k^2)
        # losing hp to status
        if self.status == "burn": # O(m)
            self.hp -= 1 # O(1)
        elif self.status == "poison": # O(m)
            self.hp -= 3 # O(1)
        
        self.apply_status_effect(other) # O(m)

    def apply_status_effect(self, other: PokemonBase, status_chance=None):
        """
        Applies a status effect on the opponent based on the status of the pokemon.

        Arguments: 
            self: obj
            lother(opponent): obj
            status_chance: boolean

        Returns: 
            None 

        Total time complexity: O(n)
        Where n is the comparison of strings
        """
        if status_chance == None:
            status_chance = RandomGen.random_chance(0.2) # O(1)
        if status_chance:
            if self.poke_type == "Fire": # O(n)
                other.status = "burn"  # O(1)
            elif self.poke_type == "Grass": # O(n)
                other.status = "poison"  # O(1)
            elif self.poke_type == "Water": # O(n)
                other.status = "paralysis"  # O(1)
            elif self.poke_type == "Ghost": # O(n)
                other.status = "sleep"  # O(1)
            else:
                other.status = "confuse"  # O(1)
         
    def __str__(self) -> str:
        """
        Creates a string representation of the pokemon and its statistics

        Arguments: 
            self: obj

        Returns: 
            String representation: str 
        """
        return f'LV. {self.level} {self.poke_name}: {self.hp} HP' # O(1)

    def should_evolve(self) -> bool:
        """
        Determines whether is the pokemon is fainted. If so, the pokemon should not evolve despite reaching the
        required evolution level.

        Arguments: 
            self: obj

        Returns: 
            True/False 

        Total time complexity: O(1)
        """
        if self.is_fainted(): # O(1)
            return False # O(1)
        else:
            return True # O(1)

    def can_evolve(self) -> bool:
        """
        Checks whether pokemon has reached the required level to evolve.

        Arguments: 
            self: obj

        Returns: 
            True/False 

        Total time complexity: O(1)
        """
        if self.level >= self.evolve_level: # O(1)
            return True # O(1)
        else:
            return False # O(1)

    @abstractmethod
    # this method is implemented in the child class 'Pokemon' as each pokemon has own its unique evolution
    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evovlved version of the current pokemon
        """
        pass

        


