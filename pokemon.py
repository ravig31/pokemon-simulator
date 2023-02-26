from pokemon_base import PokemonBase
"""
This file implements each of the pokemon's unique statistic calculations based on their level, status, evolution
and attack damage in incurred.

Last modified: 25/09/2022
"""
__author__ = "Scaffold by Jackson Goerner, Code by Ravindu Gamage, Matt Ch'ng, Eric Theov, Adrian Louis"

class Charmander(PokemonBase): # Inherits the parent class PokemonBase to access its methods
    """
    Object constructor for Charmander pokemon
    """
    def __init__(self):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 8 + (1 * 1), 'Fire')  # O(1)
        self.poke_name = "Charmander"  # O(1)
        self.level = 1  # O(1)
        self.evolve_level = 3  # O(1)
        self.hp = 9  # O(1)
        self.attack_damage = 7  # O(1)
        self.speed = 8  # O(1)
        self.defence = 4  # O(1)
        self.pokedex_no = 1  # O(1)
        self.max_hp = 9  # O(1)
        
    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of the arithmetic operations
        """
        PokemonBase.level_up(self) # increment pokemon level to update statistics O(1)
        self.hp += 1  # O(1)
        self.max_hp += 1  # O(1)
        self.attack_damage = 6 + (1 * self.level)  # O(k^2)
        self.speed = 7 + (1 * self.level)  # O(k^2)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. When the effective attack is greater than Charmander’s defence,
        Charmander loses HP equal to the effective attack.

        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        if damage > self.defence:  # O(1)
            super().lose_hp(damage)  # super inherits the method from parent class O(1)
        else: 
            #Otherwise, it loses only half of the effective attack.
            super().lose_hp(damage // 2)  # O(k^2)
        return self.hp  # O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        if self.should_evolve() and self.can_evolve(): # comparison of two booleans = O(1)
            return Charizard(self.max_hp - self.hp if self.max_hp - self.hp > 0 else 0,
                            self.status) # O(1) 
        return self  # O(1)

#-----------------------------------------------------------------------------------------

class Squirtle(PokemonBase):
    """
    Object constructor for Squirtle pokemon
    """
    def __init__(self):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 9 + (2 * 1), 'Water') # O(1)
        self.poke_name = "Squirtle" # O(1)
        self.level = 1 # O(1)
        self.evolve_level = 3 # O(1)
        self.hp = 11 # O(1)
        self.attack_damage = 4 # O(1)
        self.speed = 7 # O(1)
        self.defence = 7 # O(1)
        self.pokedex_no = 2 # O(1)
        self.max_hp = 11 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        PokemonBase.level_up(self) # increment pokemon level to update statistics O(1)
        self.hp += 2 # O(1)
        self.max_hp += 2 # O(1)
        self.attack_damage = 4 + (self.level // 2) # O(k^2)
        self.defence = 6 + self.level  # O(1)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. 

        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        #When the effective attack is greater than twice of Squirtle’s defence, Squirtle loses HP equal to the effective attack.
        #Otherwise, it loses only half as much of the HP as the effective attack
        if damage > self.defence * 2: # O(n^2)
            super().lose_hp(damage) # O(1)
        else:
            super().lose_hp(damage // 2) # O(k^2)
        return self.hp # O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        if self.should_evolve() and self.can_evolve():  # comparison of two booleans = O(1)
            return Blastoise(self.max_hp - self.hp if self.max_hp - self.hp > 0 else 0,
                            self.status) # O(1)
        return self # O(1)

#-----------------------------------------------------------------------------------------

class Bulbasaur(PokemonBase):
    """
    Object constructor for Charmander pokemon
    """
    def __init__(self):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 12 + (1 * 1), 'Grass') # O(1)
        self.poke_name = "Bulbasaur" # O(1)
        self.level = 1 # O(1)
        self.evolve_level = 2 # O(1)
        self.hp = 13 # O(1)
        self.attack_damage = 5 # O(1)
        self.speed = 7 # O(1)
        self.defence = 5 # O(1)
        self.pokedex_no = 3 # O(1)
        self.max_hp = 13 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        PokemonBase.level_up(self)# increment pokemon level to update statistics O(1)
    
        self.hp += 1 # O(1)
        self.max_hp += 1 # O(1)
        self.speed = 7 + (self.level // 2) # O(k^2)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. When the effective attack is greater than (Bulbasaur’s defence +
        5), Bulbasaur loses HP equal to the effective attack. Otherwise, it
        loses only half as much of the HP as the effective attack

        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        if damage > self.defence + 5: # O(1)
            super().lose_hp(damage) # O(1)
        else:
            super().lose_hp(damage // 2) # O(k^2)

    def get_evolved_version(self) -> PokemonBase: # O(1)
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        if self.should_evolve() and self.can_evolve(): # O(1)
            return Venusaur(self.max_hp - self.hp if self.max_hp - self.hp > 0 else 0,
                            self.status) # O(1)
        return self  # O(1)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Gastly(PokemonBase):
    """
    Object constructor for Gastly pokemon
    """
    def __init__(self):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 6 + (1 // 2), 'Ghost') # O(1)
        self.poke_name = "Gastly" # O(1)
        self.level = 1 # O(1)
        self.evolve_level = 1 # O(1)
        self.hp = 6 # O(1)
        self.attack_damage = 4 # O(1)
        self.speed = 2 # O(1)
        self.defence = 8 # O(1)
        self.pokedex_no = 4 # O(1)
        self.max_hp = 6 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        PokemonBase.level_up(self) #O(1)
        if self.level // 2 == 0: # O(k^2)
            self.hp += 1 # O(1)
            self.max_hp += 1 #O(1)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. Loses HP equal to the effective attack

        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(1)
        """
        super().lose_hp(damage) # super inherits the method from parent class #O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        if self.should_evolve() and self.can_evolve(): # O(1)
            return Haunter(self.max_hp - self.hp if self.max_hp - self.hp > 0 else 0, 
                        self.status) #O(1)
        return self #O(1)

#-------------------------------------------------------------------------------------------------------------------------------------------------

class Eevee(PokemonBase):
    """
    Object constructor for Eevee pokemon
    """
    def __init__(self):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 10, 'Normal') # O(1)
        self.poke_name = "Eevee" # O(1)
        self.level = 1 # O(1)
        self.hp = 10 # O(1)
        self.attack_damage = 7 # O(1)
        self.speed = 8 # O(1)
        self.defence = 5 # O(1)
        self.pokedex_no = 5 # O(1)
        self.max_hp = 10 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(1)
        """
        PokemonBase.level_up(self)# increment pokemon level to update statistics
        self.attack_damage = 6 + self.level # O(1)
        self.speed = 7 + self.level # O(1)
        self.defence = 4 + self.level # O(1)

    def defend(self, damage: int) -> int:
        """
        Performs pokemon's defence calculations. When the effective attack is greater or equal to Eevee’s defence,
        lose HP equal to the effective attack. Otherwise lose no HP

        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        if damage >= self.defence: # O(1)
            super().lose_hp(damage) # super inherits the method from parent class O(1)
        return self.hp # O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        return self # O(1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

class Charizard(PokemonBase):
    """
    Object constructor for Charizard pokemon
    """
    def __init__(self, lost_hp=0, status=None):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 12 + (1 * 3), 'Fire') # O(1)
        self.poke_name = "Charizard" # O(1)
        self.level = 3 # O(1)
        self.hp = 15 - lost_hp # O(1)
        self.attack_damage = 16 # O(1)
        self.defence = 4 # O(1)
        self.speed = 12 # O(1)
        self.status = status # O(1)
        self.pokedex_no = 6 # O(1)
        self.max_hp = 15 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of the arithmetic operations
        """
        PokemonBase.level_up(self) # increment pokemon level to update statistics O(1)
        self.hp += 1 # O(1)
        self.attack_damage = 10 + (2 * self.level) # O(k^2)
        self.speed = 9 + (1 * self.level) # O(k^2)
        self.max_hp += 1  # O(1)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. When the effective attack is greater than Charizard’s defence,
        Charizard loses HP equal to twice the effective attack. Otherwise,
        it loses HP equal to the effective attack


        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        if damage > self.defence: # O(1)
            super().lose_hp(damage * 2) # super inherits the method from parent class O(k^2)
        else: 
            super().lose_hp(damage) # super inherits the method from parent class O(1)
        return self.hp # O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        return self # O(1)

#--------------------------------------------------------------------------------------------------------------------------------

class Blastoise(PokemonBase):
    """
    Object constructor for Blastoise pokemon
    """
    def __init__(self, lost_hp=0, status=None):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 15 + (2 * 3), 'Water') # O(1)
        self.poke_name = "Blastoise" # O(1)
        self.level = 3 # O(1)
        self.hp = 21 - lost_hp # O(1)
        self.attack_damage = 9 # O(1)
        self.defence = 11 # O(1)
        self.speed = 10 # O(1)
        self.status = status # O(1)
        self.pokedex_no = 7 # O(1)
        self.max_hp = 21 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of the arithmetic operations
        """
        PokemonBase.level_up(self) # O(1)
        self.hp += 2 # O(1)
        self.max_hp += 2 # O(1)
        self.attack_damage = 8 + (self.level // 2) # O(k^2)
        self.defence = 8 + self.level  # O(1)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. When the effective attack is greater than double Blastoise’s
        defence, Blastoise loses HP equal to the effective attack.
        Otherwise, it loses HP equal to half the effective attack 

        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        if damage > self.defence * 2: # O(k^2)
            super().lose_hp(damage) # O(1)
        else:
            super().lose_hp(damage // 2) # O(k^2)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        return self # O(1)

#--------------------------------------------------------------------------------------------------------------------------------
        
class Venusaur(PokemonBase):
    """
    Object constructor for Venusaur pokemon
    """
    def __init__(self, lost_hp=0, status=None):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 20 + (2 // 2), 'Grass')
        self.poke_name = "Venusaur" # O(1)
        self.level = 2 # O(1)
        self.hp = 21 - lost_hp # O(1)
        self.attack_damage = 5 # O(1)
        self.defence = 10 # O(1)
        self.speed = 4 # O(1)
        self.status = status # O(1)
        self.pokedex_no = 8 # O(1)
        self.max_hp = 21 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of the arithmetic operations
        """
        PokemonBase.level_up(self)# increment pokemon level to update statistics O(1)
        if self.level % 2 == 0: # O(k^2)
            self.hp += 1 # O(1)
            self.speed = 3 + (self.level // 2) # O(k^2)
            self.max_hp += 1 # O(1)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. When the effective attack is greater than (Venusaur’s defence +
        5), Venusaur loses HP equal to the effective attack. Otherwise, it
        loses HP equal to half the effective attack

        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(k^2)
        Where k is the cost of operations
        """
        if damage > self.defence + 5 :  # O(1)
            super().lose_hp(damage) # O(1)
        else: 
            super().lose_hp(damage // 2)# O(k^2)

        return self.hp # O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        return self # O(1)

#--------------------------------------------------------------------------------------------------------------------------------

class Haunter(PokemonBase):
    """
    Object constructor for Charmander pokemon
    """
    def __init__(self, lost_hp=0, status=None):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 9 + (1 // 2), 'Ghost') # O(1)
        self.poke_name = "Haunter" # O(1)
        self.level = 1 # O(1)
        self.evolve_level = 3 # O(1)
        self.hp = 9 - lost_hp # O(1)
        self.attack_damage = 8 # O(1)
        self.defence = 6 # O(1)
        self.speed = 6 # O(1)
        self.status = status # O(1)
        self.pokedex_no = 9 # O(1)
        self.max_hp = 9  # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of the arithmetic operations
        """
        PokemonBase.level_up(self)# increment pokemon level to update statistics O(1)
        if self.level % 2 == 0: # O(k^2)
            self.hp += 1 # O(1)
            self.max_hp += 1 # O(1)

    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. Loses HP equal to the effective attack


        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(1)
        """
        super().lose_hp(damage)# super inherits the method from parent class O(1)
        return self.hp # O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        if self.should_evolve() and self.can_evolve(): # O(1)
            return Gengar(self.max_hp - self.hp if self.max_hp - self.hp > 0 else 0, self.status) # O(1)
        return self   # O(1)

#--------------------------------------------------------------------------------------------------------------------------------

class Gengar(PokemonBase):
    """
    Object constructor for Charmander pokemon
    """
    def __init__(self, lost_hp=0, status=None):
        """
        Initialises pokemon's statistics

        Arguments: 
            self: obj
            
        Returns: 
            None         

        Total time complexity: O(1)
        """
        PokemonBase.__init__(self, 12 + (1 // 2), 'Ghost') # O(1)
        self.poke_name = "Gengar" # O(1)
        self.level = 3 # O(1)
        self.hp = 13 - lost_hp # O(1)
        self.attack_damage = 18 # O(1)
        self.defence = 3 # O(1)
        self.speed = 12 # O(1)
        self.status = status # O(1)
        self.pokedex_no = 10 # O(1)
        self.max_hp = 13 # O(1)

    def level_up(self) -> None:
        """
        Performs all the statistic calculations that are dependent on the pokemon's level.

        Arguments: 
            self: obj

        Returns:
            None

        Total time complexity: O(k^2)
        Where k is the cost of the arithmetic operations
        """
        PokemonBase.level_up(self)# increment pokemon level to update statistics O(1)
        if self.level % 2 == 0: # O(k^2)
            self.hp += 1 # O(1)
            self.max_hp += 1 # O(1)


    def defend(self, damage: int) -> int: 
        """
        Performs pokemon's defence calculations. Loses HP equal to the effective attack


        Arguments: 
            self: obj
            damage(inflicted by opponent): int

        Returns:
            Hp after incurring damage: int

        Total time complexity: O(1)
        """
        super().lose_hp(damage) # O(1)
        return self.hp # O(1)

    def get_evolved_version(self) -> PokemonBase:
        """
        Obtains the evolved version of the current pokemon

        Arguments: 
            self: obj

        Returns: 
            A new instance of the PokemonBase (self): obj

        Total time complexity: O(1)
        """
        return self # O(1)








