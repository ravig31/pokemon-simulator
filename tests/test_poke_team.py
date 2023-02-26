from poke_team import Action, Criterion, PokeTeam
from random_gen import RandomGen
from pokemon import Bulbasaur, Charizard, Charmander, Gastly, Squirtle, Eevee
from tests.base_test import BaseTest

class TestPokeTeam(BaseTest):

    def test_random(self):
        """
        Tests whether the correct team has been created based on the seed provided
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 0)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Eevee, Eevee, Eevee]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regen_team(self):
        """
        Tests if a team is regenerated when regenerate_team() is called, and ensures all the correct
        pokemon are back in the team.
        """
        RandomGen.set_seed(123456789)
        t = PokeTeam.random_team("Cynthia", 2, team_size=4, criterion=Criterion.HP)
        # This should end, since all pokemon are fainted, slowly.
        while not t.is_empty():
            p = t.retrieve_pokemon()
            p.lose_hp(1)
            t.return_pokemon(p)
        t.regenerate_team()
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_battle_option_attack(self):
        """
        Tests if the correct battle option is chosen based on the integer passed into PokeTeam
        """
        t = PokeTeam("Wallace", [1, 0, 0, 0, 0], 1, PokeTeam.AI.ALWAYS_ATTACK) 
        p = t.retrieve_pokemon()
        e = Eevee()
        self.assertEqual(t.choose_battle_option(p, e), Action.ATTACK)

    def test_return_2(self): 
        """
        Tests if pokemons are returned and retrieved correctly in accordance to the properties of a list adt
        """
        t = PokeTeam("Gamage", [1, 0, 0, 1, 0], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        t.retrieve_pokemon()
        b = Bulbasaur()
        p = t.return_pokemon(b)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_team = [Bulbasaur, Gastly]
        for p, e in zip(pokemon, expected_team): 
            self.assertIsInstance(p, e)

    def test_return_0(self): 
        """
        Tests if pokemons are returned and retrieved correctly in accordance to the properties of a stack adt
        """
        t = PokeTeam("Ravindu", [1, 0, 0, 0, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        t.retrieve_pokemon()
        e = Eevee()
        p = t.return_pokemon(e)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_team = [Eevee, Eevee]
        for p, e in zip(pokemon, expected_team): 
            self.assertIsInstance(p, e)

    def test_return_1(self): 
        """
        Tests if pokemons are returned and retrieved correctly in accordance to the properties of a queue adt
        """
        t = PokeTeam("Nigel", [1, 1, 0, 0, 0], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        t.retrieve_pokemon()
        b = Bulbasaur()
        p = t.return_pokemon(b)
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_team = [Bulbasaur, Bulbasaur]
        for p, e in zip(pokemon, expected_team): 
            self.assertIsInstance(p, e)


    def test_special_mode_1(self):
        """
        Tests if pokemons are arranged correctly in the party, in accordance to the guidlines of battle mode 1
        """
        t = PokeTeam("Lance", [1, 1, 1, 1, 1], 1, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # self.assertEqual(len(t), 10)
        # C B S G E
        t.special()
        # S G E B C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Squirtle, Gastly, Eevee, Bulbasaur, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)
        
    def test_special_mode_0(self):
        """
        Tests if pokemons are arranged correctly in the party, in accordance to the guidlines of battle mode 0
        """
        t = PokeTeam("Donkey", [1, 1, 1, 1, 1], 0, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # self.assertEqual(len(t), 10)
        # C B S G E
        t.special()
        # E B S G C
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Eevee, Bulbasaur, Squirtle, Gastly, Charmander]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)
        
        
    def test_special_mode_2(self):
        """
        Tests if pokemons are arranged correctly in the party, in accordance to the guidlines of battle mode 2
        """
        t = PokeTeam("Monkey", [1, 1, 1, 1, 1], 2, PokeTeam.AI.SWAP_ON_SUPER_EFFECTIVE)
        # G B S C E
        t.special()
        # E C S B G
        pokemon = []
        while not t.is_empty():
            pokemon.append(t.retrieve_pokemon())
        expected_classes = [Gastly, Charmander, Eevee, Squirtle, Bulbasaur]
        self.assertEqual(len(pokemon), len(expected_classes))
        for p, e in zip(pokemon, expected_classes):
            self.assertIsInstance(p, e)

    def test_regenerate_team_0(self):
        """
        Tests if a team is regenerated when regenerate_team() is called, and ensures all the correct
        pokemon are back in the team.
        """
        t = PokeTeam("Horse", [1, 1, 1, 1, 1], 0, PokeTeam.AI.ALWAYS_ATTACK)
        r = []
        t.regenerate_team()
        while not t.is_empty():
            r.append(t.retrieve_pokemon())
        expected = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]
        self.assertEqual(len(r), len(expected))
        for p, e in zip(r, expected):
            self.assertIsInstance(p, e)

    def test_regenerate_team_1(self):
        """
        Tests if a team is regenerated when regenerate_team() is called, and ensures all the correct
        pokemon are back in the team.
        """
        t = PokeTeam("Arceus", [1, 1, 1, 1, 1], 1, PokeTeam.AI.ALWAYS_ATTACK)
        r = []
        t.retrieve_pokemon()
        t.regenerate_team()
        while not t.is_empty():
            r.append(t.retrieve_pokemon())
        expected = [Charmander, Bulbasaur, Squirtle, Gastly, Eevee]
        self.assertEqual(len(r), len(expected))
        for p, e in zip(r, expected):
            self.assertIsInstance(p, e)
    
    def test_regenerate_team_2(self):
        """
        Tests if a team is regenerated when regenerate_team() is called, and ensures all the correct
        pokemon are back in the team.
        """
        t = PokeTeam("Magikarp", [1, 1, 0, 1, 1], 2, PokeTeam.AI.ALWAYS_ATTACK)
        r = []
        t.retrieve_pokemon()
        t.regenerate_team()
        while not t.is_empty():
            r.append(t.retrieve_pokemon())
        expected = [Bulbasaur, Eevee, Charmander, Gastly]
        self.assertEqual(len(r), len(expected))
        for p, e in zip(r, expected):
            self.assertIsInstance(p, e)

    def test_string(self):
        """
        Tests if the correct string representation is outputed, ensuring that it matches the statistics of each pokemon
        """
        t = PokeTeam("Dawn", [1, 1, 1, 1, 1], 2, PokeTeam.AI.RANDOM, Criterion.DEF)
        self.assertEqual(str(t), "Dawn (2): [LV. 1 Gastly: 6 HP, LV. 1 Squirtle: 11 HP, LV. 1 Eevee: 10 HP, LV. 1 Bulbasaur: 13 HP, LV. 1 Charmander: 9 HP]")
