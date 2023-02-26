from random_gen import RandomGen
from poke_team import Criterion, PokeTeam
from battle import Battle
from tower import BattleTower
from tests.base_test import BaseTest

class TestTower(BaseTest):

    def test_creation(self):
        """
        Tests the creation of a tower with random teams, and the results of battles against that set tower
        """
        RandomGen.set_seed(51234)
        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("N", 2, team_size=6, criterion=Criterion.HP))
        bt.generate_teams(4)
        # Teams have 7, 10, 10, 3 lives.
        RandomGen.set_seed(1029873918273)
        results = [
            (1, 6),
            (1, 9),
            (2, 10)
        ]
        it = iter(bt)
        for (expected_res, expected_lives), (res, me, tower, lives) in zip(results, it):
            self.assertEqual(expected_res, res, (expected_res, expected_lives))
            self.assertEqual(expected_lives, lives)

    def test_duplicates(self):
        """
        Tests the creation of a tower with random teams and checks for the elimination of duplicates.
        Checks results of battles against this set team.
        """
        RandomGen.set_seed(29183712400123)
    
        bt = BattleTower(Battle(verbosity=0))
        bt.set_my_team(PokeTeam.random_team("Jackson", 0, team_size=6))
        bt.generate_teams(10)

        # Team numbers before:
        # [0, 4, 1, 0, 0], 6
        # [1, 0, 2, 0, 0], 5
        # [1, 1, 0, 1, 0], 8
        # [1, 2, 1, 1, 0], 10
        # [0, 0, 2, 1, 1], 8
        # [1, 1, 3, 0, 0], 4
        # [0, 2, 0, 1, 0], 5
        # [1, 0, 0, 4, 0], 3
        # [1, 1, 1, 0, 2], 7
        # [0, 1, 1, 1, 0], 9
        it = iter(bt)
        it.avoid_duplicates()
        # Team numbers after:
        # [1, 1, 0, 1, 0], 8
        # [0, 1, 1, 1, 0], 9

        l = []
        for res, me, tower, lives in bt:
            tower.regenerate_team()
            l.append((res, lives))
        
        self.assertEqual(l, [
            (1, 7),
            (1, 8),
            (2, 7)
        ])

