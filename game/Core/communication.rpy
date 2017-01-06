##############################################################################
# Communication with NPCs
#

label lbl_communicate(target):
    target "I'm here"
    menu:
        'Gratify':
            call lbl_gratify(target)              
        'Cooperate':
            call lbl_cooperate(target)
        'Dominate':
            call lbl_dominate(target)
        'Nevermind':
            pass
    
    return

label lbl_dominate(target):
    menu:
        'Insult (charisma)':
            pass
                        
        'Back':
            call lbl_communicate(target)
    
    $ player.ap -= 1
    return

label lbl_gratify(target):
    menu:
        'Compliment (charisma)':
            python:
                morality = ['good']
                difficulty = core.token_difficulty(target, 'contribution', 'communication')
                skillcheck = core.skillcheck(player, 'charisma', morality, difficulty, beneficiar=player)
                skillcheck = skillcheck.result
                result = core.gain_ctoken(skillcheck, target, 'contribution', tense=None, satisfy=['communication'])
            
            if result:
                'Bingo'
            else:
                'No chance'
                        
        'Back':
            call lbl_communicate(target)
    
    $ player.ap -= 1
    return
