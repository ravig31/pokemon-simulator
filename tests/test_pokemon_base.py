from random_gen import RandomGen
from pokemon_base import PokemonBase, PokeType
from pokemon import Eevee, Gastly, Haunter
from tests.base_test import BaseTest

class TestPokemonBase(BaseTest):

    def test_cannot_init(self):
        """
        Tests that we cannot initialise PokemonBase, and that it raises the correct error.

        Total time complexcity: O(n) 
        """
        self.assertRaises(TypeError, lambda: PokemonBase(30, PokeType.FIRE))  # O(n)

    def test_level(self):
        """
        Tests that pokemon's level increases when levelling up
        
        Total time complexity: O(1)
        """
        e = Eevee()
        self.assertEqual(e.get_level(), 1) # O(1)
        e.level_up()
        self.assertEqual(e.get_level(), 2) # O(1)
    
    def test_hp(self):
        """
        Tests that hp increases and decreases after actions are performed
        
        Total time complexity: O(1)
        """
        e = Eevee()
        self.assertEqual(e.get_hp(), 10) # O(1)
        e.lose_hp(4)
        self.assertEqual(e.get_hp(), 6) # O(1)
        e.heal()
        self.assertEqual(e.get_hp(), 10) # O(1)

    def test_status(self):
        """
        Tests that status effects are applied on pokemon when attacked
        
        Total time complexity: O(n^2)
        """
        RandomGen.set_seed(0)  # O(1)
        e1 = Eevee()  # O(1)
        e2 = Eevee()  # O(1)
        e1.attack(e2)  # O(n^2)
        # e2 now is confused.
        e2.attack(e1)  # O(1)
        # e2 takes damage in confusion.
        self.assertEqual(e1.get_hp(), 10)  # O(1)

    def test_evolution(self):
        """
        Tests if pokemon evolves given that it meets the criteria

        Total time complexity: O(1)
        """
        g = Gastly()  # O(1)
        self.assertEqual(g.can_evolve(), True) # O(1)
        self.assertEqual(g.should_evolve(), True) # O(1)
        new_g = g.get_evolved_version()  # O(1)
        self.assertIsInstance(new_g, Haunter) # O(1)
