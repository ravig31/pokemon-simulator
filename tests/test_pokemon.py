from pokemon import Venusaur, Charmander, Bulbasaur, Gastly, Haunter, Squirtle, Charizard, Eevee, Gengar, Blastoise
from tests.base_test import BaseTest

class TestPokemon(BaseTest):

    def test_venusaur_stats(self):
        """
        Checks Venusaur's statistics after levelling up and losing hp
        """
        v = Venusaur() 
        self.assertEqual(v.get_poke_name(), "Venusaur")
        self.assertEqual(v.get_hp(), 21)
        self.assertEqual(v.get_level(), 2) 
        self.assertEqual(v.get_attack_damage(), 5) 
        self.assertEqual(v.get_speed(), 4) 
        self.assertEqual(v.get_defence(), 10) 
        v.level_up() 
        v.level_up() 
        v.level_up() 
        self.assertEqual(v.get_hp(), 22) 
        self.assertEqual(v.get_level(), 5) 
        self.assertEqual(v.get_attack_damage(), 5) 
        self.assertEqual(v.get_speed(), 5) 
        self.assertEqual(v.get_defence(), 10) 
        v.lose_hp(5) 

        self.assertEqual(str(v), "LV. 5 Venusaur: 17 HP")  # O(n)

    def test_charmander_stats(self):
        """
        Checks Charmander's statistics after levelling up and evolving
        """
        c = Charmander() 
        self.assertEqual(c.get_poke_name(), "Charmander") # O(n)
        self.assertEqual(c.get_hp(), 9) 
        self.assertEqual(c.get_level(), 1) 
        self.assertEqual(c.get_attack_damage(), 7) 
        self.assertEqual(c.get_speed(), 8) 
        self.assertEqual(c.get_defence(), 4) 
        c.level_up() 
        c.level_up() 
        c = c.get_evolved_version() 
        self.assertEqual(c.get_hp(), 15) 
        self.assertEqual(c.get_level(), 3) 
        self.assertEqual(c.get_attack_damage(), 16) 
        self.assertEqual(c.get_speed(), 12) 
        self.assertEqual(c.get_defence(), 4) 
        c.lose_hp(5) 
        self.assertEqual(c.get_hp(), 10) 


        self.assertEqual(str(c), "LV. 3 Charizard: 10 HP")  # O(n)

    def test_gastly_vs_bulbasaur(self):
        """
        Tests Gastly's defence calculations and base stats after evolving.
        Checks Bulbasaur and Gastly's stats after an attack.
        """
        g = Gastly()  
        b = Bulbasaur()  
        self.assertEqual(g.get_hp(), 6)  
        self.assertEqual(g.get_level(), 1) 
        self.assertEqual(g.get_attack_damage(), 4) 
        self.assertEqual(g.get_speed(), 2) 
        self.assertEqual(g.get_defence(), 8) 
        g.defend(3) 
        self.assertEqual(g.can_evolve(), True) 
        self.assertEqual(g.should_evolve(), True) 
        g = g.get_evolved_version() 
        self.assertEqual(str(g), "LV. 1 Haunter: 6 HP") # O(n)
        
        self.assertEqual(g.get_hp(), 6) 

        setattr(g, "status", "burn") 
        g.attack(b) 
        self.assertEqual(g.get_hp(), 5)  
        self.assertEqual(b.get_hp(), 11) 

        g.level_up() 
        self.assertEqual(g.get_hp(), 6) 

        self.assertEqual(str(b), "LV. 1 Bulbasaur: 11 HP") 

    
    def test_charizard_vs_blastoise(self):
        """
        Tests if pokemon has fainted after its hp reaches 0 following an attack.
        """
        c = Charizard() 
        self.assertEqual(c.get_poke_name(), "Charizard") # O(n)
        self.assertEqual(c.is_fainted(), False) 
        b = Blastoise() 
        b.attack(c) 
        self.assertEqual(c.is_fainted(), True) 
        

    def test_haunter_vs_eevee(self):
        """
        Tests if pokemon has carried over the damage it had incurred prior to evolving.
        Checks the stats of the evolved version.
        """
        h = Haunter() 
        e = Eevee() 
        h.attack(e) 
        e.attack(h) 
        h.attack(e) 
        e.attack(h) 
        self.assertEqual(e.is_fainted(), False) 
        h.level_up() # O(k^2)
        h.level_up() # O(k^2)
        self.assertEqual(h.can_evolve(), True) 
        self.assertEqual(h.should_evolve(), True) 
        h.apply_status_effect(e, True) 
        self.assertEqual(e.get_status(), "sleep")  # O(n)
        e.lose_hp(5) 
        self.assertEqual(e.get_hp(), 5) 

    def test_transfer_status(self): 
        """
        Checks that status effects have carried over once a pokemon has evolved.
        Checks stats after incurring damage.
        """
        s = Squirtle() 
        g = Gengar() 
        g.apply_status_effect(s, True) 
        self.assertEqual(s.get_status(), "sleep") # O(n)
        s.apply_status_effect(g, True) 
        self.assertEqual(g.get_status(), "paralysis") # O(n)
        s.level_up() 
        s.level_up() 
        s = s.get_evolved_version() 
        self.assertEqual(s.get_status(), "sleep") # O(n)
        s.defend(7) 
        self.assertEqual(s.get_hp(), 18) 
        g.defend(10) 
        self.assertEqual(g.get_hp(), 3) 

