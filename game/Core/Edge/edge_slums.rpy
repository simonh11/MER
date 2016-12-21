##############################################################################
# The Edge of Mists living in slums
#
# Slums menu

label lbl_edge_squatted_slums(location):
    menu:
        'Only place to live in if you not in a gang.'
        'Find some work in a slums':
            call lbl_edge_slums_work(location)
        'Sign in' if not edge.slums_mode:
            $ edge.slums_mode = True
            call lbl_edge_slums_livein
        'Manage accomodation' if edge.slums_mode:
            call lbl_edge_slums_livein            
        'Get out':
            return         
    
    call lbl_edge_squatted_slums(location)
    return

label lbl_edge_slums_livein:
    $ resources = encolor_text(show_resource[edge.resources.value], edge.resources.value)
    $ free = encolor_text('free', 5)
    $ cost_1 = encolor_resource_text(1)
    $ cost_2 = encolor_resource_text(2)
    $ cost_3 = encolor_resource_text(3)
    $ cost_4 = encolor_resource_text(4)
    $ cost_5 = encolor_resource_text(5)    
    $ consumption_level = edge.resources.consumption_level()
    $ bill = encolor_text(spending_rate[5-consumption_level], 5-consumption_level)
    
    menu:        
        "[resources] \nDecade bill: [bill]"
        'Accomodation':
            call lbl_edge_slums_accomodation            
        'Catering':
            call lbl_edge_slums_ration
        'Services':
            call lbl_edge_slums_services
        'Back':
            call lbl_edge_manage
   
    jump lbl_edge_slums_livein
    return
    
label lbl_edge_slums_accomodation:

    menu:
        'Tiny mat in common room ([cost_1])':
            $ target.schedule.add_action('accommodation_mat', single=False) 
            $ cost = 1
        'Cot & bkanket ([cost_2])':
            $ target.schedule.add_action('accommodation_cot', single=False) 
            $ cost = 2
        'Apartments ([cost_3])':
            $ target.schedule.add_action('accommodation_appartment', single=False) 
            $ cost = 3            
        'Rough ground, out of the walls ([free])':
            $ target.schedule.add_action('accommodation_makeshift', single=False) 
            $ cost = 0
            
    $ edge.resources.add_consumption(target, 'accomodation fee',  cost, 'accomodation')
    call lbl_edge_slums_livein
    return

    
label lbl_edge_slums_ration:
    menu:
        'Junkfood lunch ([cost_1])':
            $ target.schedule.add_action('feed_catering', single=False, special_values={'ammount': 1, 'taste': 0}) 
            $ cost = 1           
        'Junkfood 3 time meals ([cost_2])':
            $ target.schedule.add_action('feed_catering', single=False, special_values={'ammount': 2, 'taste': 0}) 
            $ cost = 2           
        'Cooked lunch ([cost_2])':
            $ target.schedule.add_action('feed_catering', single=False, special_values={'ammount': 1, 'taste': 2}) 
            $ cost = 2   
        'All junkfood you can eat ([cost_3])':
            $ target.schedule.add_action('feed_catering', single=False, special_values={'ammount': 3, 'taste': 0}) 
            $ cost = 3           
        'Cooked 3 time meals ([cost_3])':
            $ target.schedule.add_action('feed_catering', single=False, special_values={'ammount': 2, 'taste': 2}) 
            $ cost = 3   
        'Whole roasted girl ([cost_4])':
            $ target.schedule.add_action('feed_catering', single=False, special_values={'ammount': 3, 'taste': 3}) 
            $ cost = 4               
        'Eat your own food ([free])':
            $ target.schedule.remove_action('feed_catering')
            $ cost = 0
            
    $ edge.resources.add_consumption(target, 'catering cost',  cost, 'nutrition')            
    call lbl_edge_slums_livein
    return
    
    
label lbl_edge_slums_services:
    menu:
        'Back':
            call lbl_edge_slums_livein

    return
    

label lbl_edge_slums_work_food:
    menu:
        'You slacking right now - relaxing, but will not fill your belly and pockets. You can get some selfemployeed work to get some resources with your skill, or miserablly beg for some leftovers. Any way you will get yor payment after a full decade of an adequate work.'
        'Beg for food (no skill)':
            $ target.schedule.add_action('job_beg')  
            jump lbl_edge_manage
            
        'Manual labor (athletics)':
            $ title = __('Some manual labor (athletics).')
            $ skill_id = 'athletics'
            $ description = _('doing manual labor at the slums. Yelds ')
            $ special_values = {'description': description,  'skill': skill_id, 'difficulty' : 2, 'moral': ['lawful', 'timid'], 'tense': ['amusement', 'comfort'], 'statisfy': ['prosperity'], 'beneficiar': player,}
            $ target.schedule.add_action('job_simplework', 1, special_values=special_values)  
            jump lbl_edge_manage
            
        'Household services (housekeeping)':
            $ title = __('Some labor (housekeeping).')
            $ skill_id = 'housekeeping'
            $ description = _('providing household services at the slums. Yelds ')
            $ special_values = {'description': description,  'skill': skill_id, 'difficulty' : 2, 'moral': ['lawful', 'timid'], 'tense': ['amusement', 'comfort'], 'statisfy': ['prosperity'], 'beneficiar': player,}
            $ target.schedule.add_action('job_simplework', 1, special_values=special_values)  
            jump lbl_edge_manage
                                    
        'Sexual services (sex)':
            $ title = __('Some labor (sex).')
            $ skill_id = 'sex'
            $ description = _('doing sexual services at the slums. Yelds ')
            $ special_values = {'description': description,  'skill': skill_id, 'difficulty' : 2, 'moral': ['lawful', 'timid'], 'tense': ['amusement', 'comfort'], 'statisfy': ['prosperity'], 'beneficiar': player,}
            $ target.schedule.add_action('job_simplework', 1, special_values=special_values)  
            jump lbl_edge_manage
                                    
        'Newermind':
            $ pass
            
    call lbl_edge_squatted_slums(location)
    return
    
