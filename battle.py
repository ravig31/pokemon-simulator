from __future__ import annotations

"""
This file implements the battle logic based on the rules outlines in the spec sheet. These include the application of ACTIONS, 
determining the winners of battles and the order of turns.

last modified: 25/09/2022
"""
__author__ = "Scaffold by Jackson Goerner, Code by Matthew Ch'Ng, Ravindu Gamage, Adrian Louis, Eric Theov"


from random_gen import RandomGen
from poke_team import Action, PokeTeam, Criterion
from print_screen import print_game_screen

class Battle:
    """
    Implements the battle logic based on the rules outlines in the spec sheet. These include the application of ACTIONS, 
    determining the winners of battles and the order of turns.
    """
    def __init__(self, verbosity=0) -> None:
        self.verbosity = verbosity # O(1)
        self.team_automatic_win = None # O(1)

    def battle(self, team1: PokeTeam, team2: PokeTeam) -> int:
        """
        Initialises the battle class.

        Arguments: 
            self: obj
            verbosity: int

        Returns:
            0/1/2 indicating a draw, team 1 winning or team 2 winning: int

        Total time complexity: O(n + k^2)
        Where k is cost of arithmetic operations 
        """
        poke = team1.retrieve_pokemon() # O(1)
        other_poke = team2.retrieve_pokemon() # O(1)
        team1_length = team1.team.length + 1 # O(1)
        team2_length = team2.team.length + 1 # O(1)
        first_turn = True # O(1)
        print_game_screen(poke.get_poke_name(), other_poke.get_poke_name(), int(poke.hp), int(poke.max_hp), int(other_poke.hp), int(other_poke.max_hp), poke.get_level(), other_poke.get_level(), poke.get_status(), other_poke.get_status(), team1_length, team2_length) # O(1)
        team1.return_pokemon(poke) # O(1)
        team2.return_pokemon(other_poke) # O(1)


        def perform_action(pokemon, other_pokemon, team, action):
            """
            Implements the ACTION performed by each pokemon team based on the chosen battle mode

            Arguments: 
                pokemon(current pokemon): obj
                other_pokemon(opponent): obj
                team(instance of PokeTeam class): obj
                action(instance of Action class): obj
                
            Returns: 
                pokemon(current pokemon):obj

            Total time complexity: O(1)
            """
            if action == Action.HEAL and team.heals_remaining == 0: # O(1)
                self.team_automatic_win = 2 if team == team1 else 1 # O(1)
                return

            if action == Action.ATTACK: # O(1)
                pokemon.attack(other_pokemon) # O(n+m+k^2)
                return pokemon # O(1)

            elif action == Action.HEAL:
                pokemon.status = 'free' # O(1)
                pokemon.hp = pokemon.max_hp # O(1)
                team.heals_remaining -= 1 # O(1) decrement the heals remaning everytime it is used
                return pokemon # O(1)

            elif action == Action.SPECIAL: # O(1)
                team.return_pokemon(pokemon) # O(1)
                if team.team.length > 1: # O(1)
                    team.special()

                pokemon = team.retrieve_pokemon() # O(1)
                return pokemon # O(1)

            else:
                pokemon.status = 'free' # O(1)
                team.return_pokemon(pokemon) # O(1)
                pokemon = team.retrieve_pokemon() # O(1)
                return pokemon # O(1)
            
        
        continue_battle = True # O(1)

        while continue_battle: # O(n)
            if first_turn: # O(1)
                poke = team1.retrieve_pokemon()  # O(1)
                other_poke = team2.retrieve_pokemon() # O(1)
            # implementing paralysis
            speed_poke = poke.speed # O(1)
            speed_other = other_poke.speed # O(1)

            if poke.status == 'paralysis': # string comparison = O(n)
                speed_poke = poke.speed // 2 # O(k^2)

            if other_poke.status == 'paralysis': # string comparison = O(n)
                speed_other = other_poke.speed // 2 # O(k^2)

            action_poke = team1.choose_battle_option(poke, other_poke) # O(n)
            action_other = team2.choose_battle_option(other_poke, poke) # O(n)
            
            # handle swap actions
            if action_poke == Action.SWAP or action_other == Action.SWAP: # O(1)
                if action_poke == Action.SWAP: # O(1)
                    poke = perform_action(poke, other_poke, team1, action_poke) # O(1)
                if action_other == Action.SWAP: # O(1) 
                    other_poke = perform_action(other_poke, poke, team2, action_other) # O(1)

            # handle special actions
            if action_poke == Action.SPECIAL or action_other == Action.SPECIAL: # O(1)
                if action_poke == Action.SPECIAL: # O(1)
                    poke = perform_action(poke, other_poke, team1, action_poke) # O(1)
                if action_other == Action.SPECIAL: # O(1)
                    other_poke = perform_action(other_poke, poke, team2, action_other) # O(1)

            # handle heals
            if action_poke == Action.HEAL or action_other == Action.HEAL: # O(1)
                if action_poke == Action.HEAL: # O(1)
                    poke = perform_action(poke, other_poke, team1, action_poke) # O(1)
                    if self.team_automatic_win: return self.team_automatic_win  # O(1)
                if action_other == Action.HEAL: # O(1)
                    other_poke = perform_action(other_poke, poke, team2, action_other) # O(1)
                    if self.team_automatic_win: return self.team_automatic_win  # O(1)

            # if one pokemon attacks but the other does not
            if (action_poke == Action.ATTACK or action_other == Action.ATTACK) and not (action_poke == Action.ATTACK and action_other == Action.ATTACK): # O(1)
                if action_poke == Action.ATTACK: # O(1)
                    poke = perform_action(poke, other_poke, team1, action_poke) # O(1)
                if action_other == Action.ATTACK: # O(1)
                    other_poke = perform_action(other_poke, poke, team2, action_other) # O(1)
            
            # if both pokemon attack, determine who attacks first
            if action_poke == Action.ATTACK and action_other == Action.ATTACK: # O(1)
                # team1 faster than team2
                if speed_poke > speed_other: # O(1)
                    poke = perform_action(poke, other_poke, team1, action_poke) # O(1)
                    if not other_poke.is_fainted(): # O(1)
                        other_poke = perform_action(other_poke, poke, team2, action_other) # O(1)
                # team2 faster than team1
                elif speed_poke < speed_other: # O(1)
                    other_poke = perform_action(other_poke, poke, team2, action_other) # O(1)
                    if not poke.is_fainted(): # O(1)
                        poke = perform_action(poke, other_poke, team1, action_poke)  # O(1)   
                # speed is equal
                else: 
                    poke = perform_action(poke, other_poke, team1, action_poke) # O(1)
                    other_poke = perform_action(other_poke, poke, team2, action_other) # O(1)

            if not poke.is_fainted() and not other_poke.is_fainted(): # O(1)
                poke.hp -= 1 # O(1)
                other_poke.hp -= 1 # O(1)
            
            if not poke.is_fainted() and other_poke.is_fainted(): # O(1)
                poke.level_up() # O(k^2)

            if poke.is_fainted() and not other_poke.is_fainted(): # O(1)
                other_poke.level_up() # O(k^2)
            
            if not poke.is_fainted(): # O(1)
                poke = poke.get_evolved_version() # O(1)
            
            if not other_poke.is_fainted(): # O(1)
                other_poke = other_poke.get_evolved_version() # O(1)

            first_turn = False # O(1)
            
            if poke.is_fainted() and not team1.is_empty(): # O(1)
                poke = team1.retrieve_pokemon() # O(1)
            if other_poke.is_fainted() and not team2.is_empty(): # O(1)
                other_poke = team2.retrieve_pokemon() # O(1)

            team1_length = team1.team.length + 1 # O(1)
            team2_length = team2.team.length + 1 # O(1)
            
            print_game_screen(poke.get_poke_name(), other_poke.get_poke_name(), int(poke.hp), int(poke.max_hp), int(other_poke.hp), int(other_poke.max_hp), poke.get_level(), other_poke.get_level(), poke.get_status(), other_poke.get_status(), team1_length, team2_length) # O(1)
            
            if (team1.is_empty() and poke.is_fainted()) or (team2.is_empty() and other_poke.is_fainted()): # O(1)
                continue_battle = False # O(1)
 
 
        # return pokemon back into party if they are not fainted by the end of a battle. 
        # This ensures that teams will not be recognised as empty in a 1v1 edge case.
        if not poke.is_fainted(): # O(1)
            team1.return_pokemon(poke)  # O(1)
        if not other_poke.is_fainted(): # O(1)
            team2.return_pokemon(other_poke)  # O(1)
        
        if team1.is_empty() and team2.is_empty():  # O(1)
            return 0 # O(1)
        elif team1.is_empty():  # O(1)
            return 2  # O(1)
        else: # O(1)
            return 1 # O(1)