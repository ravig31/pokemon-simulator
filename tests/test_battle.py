from random_gen import RandomGen
from battle import Battle
from poke_team import Criterion, PokeTeam
from pokemon import Charizard, Charmander, Eevee, Gastly, Squirtle, Venusaur, Blastoise
from tests.base_test import BaseTest

class TestBattle(BaseTest):

    def test_basic_battle(self):
        """
        Testing a battle between Ash and Gary. 
        Checks the remaining pokemon in the winning team and their statistics
        """
        RandomGen.set_seed(1337)
        team1 = PokeTeam("Ash", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("Gary", [0, 0, 0, 0, 3], 0, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        self.assertTrue(team2.is_empty())
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].get_hp(), 1)
        self.assertIsInstance(remaining[0], Venusaur)
        self.assertEqual(remaining[1].get_hp(), 11)
        self.assertIsInstance(remaining[1], Squirtle)

    def test_complicated_battle(self):
        """
        Testing a battle between Ash and Gary. 
        Checks the remaining pokemon in the winning team and their statistics
        """
        RandomGen.set_seed(192837465)
        team1 = PokeTeam("Brock", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.HP)
        team2 = PokeTeam("Misty", [0, 0, 0, 3, 3], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].get_hp(), 11)
        self.assertIsInstance(remaining[0], Charizard)
        self.assertEqual(remaining[1].get_hp(), 6)
        self.assertIsInstance(remaining[1], Gastly)

    def test_our_battle1(self):
        """
        Testing a battle between LinusTechTips and StaffCarPark. 
        Checks the remaining pokemon in the winning team and their statistics

        This is the edge case with a 1v1 situation, with each team having only one pokemon.
        """
        RandomGen.set_seed(1959)
        team1 = PokeTeam("LinusTechTips", [1, 0, 0, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("StaffCarpark", [0, 0, 1, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 2)
        self.assertTrue(team1.is_empty())
        remaining = []
        while not team2.is_empty():
            remaining.append(team2.retrieve_pokemon())
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0].get_hp(), 4)
        self.assertIsInstance(remaining[0], Squirtle)

    def test_our_battle2(self):
        """
        Testing a battle between etheov and matching. 
        Checks the remaining pokemon in the winning team and their statistics
        """
        RandomGen.set_seed(1998)
        team1 = PokeTeam("etheov", [1, 1, 1, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK)
        team2 = PokeTeam("matching", [0, 0, 1, 1, 1], 1, PokeTeam.AI.ALWAYS_ATTACK)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        self.assertTrue(team2.is_empty())
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 2)
        self.assertEqual(remaining[0].get_hp(), 19)
        self.assertIsInstance(remaining[0], Venusaur)
        self.assertEqual(remaining[1].get_hp(), 11)
        self.assertIsInstance(remaining[1], Squirtle)

    def test_our_battle3(self):
        """
        Testing a battle between eugene and buzzfeed. 
        Checks the remaining pokemon in the winning team and their statistics
        """
        RandomGen.set_seed(1998)
        team1 = PokeTeam("eugene", [0, 0, 5, 0, 0], 0, PokeTeam.AI.ALWAYS_ATTACK, criterion=Criterion.HP)
        team2 = PokeTeam("buzzfeed", [0, 0, 0, 3, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE, criterion=Criterion.SPD)
        b = Battle(verbosity=0)
        res = b.battle(team1, team2)
        self.assertEqual(res, 1)
        self.assertTrue(team2.is_empty())
        remaining = []
        while not team1.is_empty():
            remaining.append(team1.retrieve_pokemon())
        self.assertEqual(len(remaining), 5)
        self.assertEqual(remaining[0].get_hp(), 17)
        self.assertIsInstance(remaining[0], Blastoise)
        self.assertEqual(remaining[1].get_hp(), 11)
        self.assertIsInstance(remaining[1], Squirtle)
        self.assertEqual(remaining[2].get_hp(), 11)
        self.assertIsInstance(remaining[2], Squirtle)
        self.assertEqual(remaining[2].get_hp(), 11)
        self.assertIsInstance(remaining[2], Squirtle)
        self.assertEqual(remaining[2].get_hp(), 11)
        self.assertIsInstance(remaining[2], Squirtle)


