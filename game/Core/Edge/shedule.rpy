##############################################################################
# The Edge of Mists schedule
#
# Script for EOM shedule events

label shd_evn_None_template(character):
    $ d = character.description()
    '[d] TOASTED!'
    return
    
label shd_living_makeshift(character):
    python:
        action.actor.comfort.set_tension()
        action.actor.prosperity.set_tension()
        action.actor.wellness.set_tension()   
        action.actor.add_modifier('bad_sleep', {'vitality': -1}, 1)  
        name = action.actor.name()
    return