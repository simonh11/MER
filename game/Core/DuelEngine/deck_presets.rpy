init python:
    default_decks = {
        'noncombatant': {'clinch': 1, 'hit_n_run': 1, 'rage': 1, 'outsmart': 1, 'initiative': 1, 'fatigue': 1, 'bite': 3, 'punch': 4, 'recoil': 4, 'deep_breath': 4},  
        'desperado': {'clinch': 1, 'hit_n_run': 1, 'rage': 1, 'outsmart': 1, 'initiative': 1, 'fatigue': 1, 'desperate_strike': 3, 'desperate_move': 3, 'desperate_block': 3, 'kick': 3, 'dodge': 3, 'caution': 3},      
        'rookie': {'clinch': 1, 'hit_n_run': 1, 'rage': 1, 'outsmart': 2, 'initiative': 2, 'fatigue': 2, 'kick': 1, 'simple_strike': 4, 'simple_move': 4, 'simple_block': 4},
        'beast': {'initiative': 2, 'vicious_bite': 4, 'rend': 4, 'gnaw': 4, 'dodge': 4, 'caution': 4},  
    }
    leveled_decks = {
        #named 'punk' in disdoc
        'wrestler2': {'clinch': 1, 'hit_n_run': 1, 'rage': 1, 'outsmart': 1, 'initiative': 1, 'fatigue': 1, 'kick': 4, 'punch': 4, 'dodge': 4, 'caution': 4},
        'wrestler3': {'initiative': 2, 'fatigue': 2, 'punch': 2, 'kick': 4, 'caution': 4, 'grapple': 4, 'lock': 4},
        'wrestler4': {},
        'wrestler5': {},
        'breter3': {'hit_n_run': 1, 'rage': 1, 'initiative': 2, 'outsmart': 2, 'strike': 4, 'move': 4, 'block': 4, 'follow_up': 4},
        'breter4': {'hit_n_run': 1, 'rage': 1, 'initiative': 2, 'outsmart': 2, 'tricky_strike': 4, 'flurry': 4, 'tricky_block': 4, 'follow_up': 4},
        'breter5': {'critical_hit': 1, 'outsmart': 1, 'initiative': 2, 'great_strike': 4, 'great_move': 2, 'great_block': 4, 'follow_up': 4, 'flurry': 4},         
        'juggernaut3': {'clinch': 1, 'rage': 1, 'outsmart': 2, 'initiative': 2, 'strike': 4, 'move': 4, 'block': 4, 'battering_strike': 4},
        'juggernaut4': {'outsmart': 2, 'initiative': 2, 'tricky_strike': 4, 'tricky_move': 3, 'tricky_block': 3, 'battering_strike': 4, 'rampage': 4},
        'juggernaut5': {'critical_hit': 1, 'outsmart': 1, 'initiative': 2, 'great_strike': 4, 'great_move': 3, 'great_block': 3, 'battering_strike': 4, 'rampage': 4},
        'shieldbearer3': {'clinch': 1, 'hit-n-run': 1, 'outsmart': 2, 'initiative': 2, 'strike': 4, 'move': 4, 'block': 4, 'second_thought': 4},
        'shieldbearer4': {'outsmart': 3, 'initiative': 3, 'tricky_strike': 4, 'tricky_move': 4, 'second_thought': 4, 'stability': 4},
        'shieldbearer5': {'critical_hit': 1, 'outsmart': 3, 'initiative': 2, 'great_strike': 4, 'great_move': 4, 'second_thought': 4, 'stability': 4},
        'beast3': {'initiative': 2, 'vicious_bite': 4, 'rend': 4, 'gnaw': 4, 'dodge': 4, 'caution': 4}, 
        'beast4': {'initiative': 2, 'gnaw': 4, 'tricky_move': 4, 'tricky_block': 4, 'savage_force': 4, 'frenzy': 4},
        'beast5': {'initiative': 2, 'critical_hit': 1, 'gnaw': 4, 'great_move': 4, 'great_block': 3, 'savage_force': 4, 'frenzy': 4}
    }