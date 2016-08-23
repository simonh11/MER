##############################################################################
# The Edge of Mists schedule
#
# Script for EOM shedule events

label shd_edge_None_template(action):
    $ d = action.actor.description()
    '[d] TOASTED!'
    return
    
label shd_edge_accommodation_makeshift(action):
    python:
        action.actor.comfort.set_tension()
        action.actor.prosperity.set_tension()
        action.actor.wellness.set_tension()   
        action.actor.add_buff('bad_sleep', {'vitality': -1}, 1)  
        name = action.actor.name
    return
    
label shd_edge_job_idle(action):
    python:
        pass
    'idling...'
    return
    
label shd_edge_job_explore(action):
    python:
        while len(edge.locations) < edge.loc_max:
            edge.explore_location()
        
    'All nearby locations explored'
    return
    
label shd_edge_job_foodwork(action):
    python:
        actor = action.actor
        name = actor.name
        beneficiar = action.special_values['beneficiar']
        core.resources.provision += 3
        core.resources.money += 800
        player.skills_used.append(action.special_values['skill'])
        player.moral_action('lawful', 'timid', target = beneficiar)  
    '[name] scavenging munition on the gim battlefield for the sake of [beneficiar.name] gang. Recived food (3)'
    return
    
label shd_edge_job_simplework(action):
    python:
        actor = action.actor
        name = actor.name
        moral = action.special_values['moral']
        skill = action.special_values['skill']
        beneficiar = action.special_values['beneficiar']
        tense = action.special_values['tense']
        statisfy = action.special_values['statisfy'] 
        txt = action.special_values['description'] 
        resname = action.special_values['resource_name'] 
        difficulty = action.special_values['difficulty'] 
        result = core.skillcheck(actor, skill, difficulty = difficulty, tense_needs=tense, satisfy_needs=statisfy, beneficiar=beneficiar, morality=moral, special_motivators=[])        
        gain = edge_yeld[result]
        action.special_values['resource'] += gain
        actor.skill(skill).get_expirience(result)
    '[name] [txt] [gain] [resname].'
    return
    
label shd_edge_job_scmunition(action):
    python:
        actor = action.actor
        name = actor.name
        moral = None
        result = core.skillcheck(actor, 'survival', difficulty = 1, tense_needs=['amusement', 'comfort'], satisfy_needs=['prosperity'], beneficiar=actor, morality=moral, special_motivators=[])        
        gain = edge_yeld[result]
        core.resources.munition += gain
        actor.skill('survival').get_expirience(result)
    '[name] scavenging munition on the gim battlefield. Yelds [gain] munition.'
    return
    
label shd_edge_job_dbexctraction(action):
    python:
        actor = action.actor
        name = actor.name
        moral = None
        result = core.skillcheck(actor, 'athletics', difficulty = 1, tense_needs=['amusement', 'comfort'], satisfy_needs=['prosperity'], beneficiar=actor, morality=moral, special_motivators=[])        
        gain = edge_yeld[result]
        core.resources.fuel += gain
        actor.skill('athletics').get_expirience(result)
    '[name] extracting demon blood from the crimson pit. Yelds [gain] fuel.'
    return
    
label shd_edge_job_scjunc(action):
    python:
        actor = action.actor
        name = actor.name
        moral = None
        result = core.skillcheck(actor, 'survival', difficulty = 2, tense_needs=['amusement', 'comfort'], satisfy_needs=['prosperity'], beneficiar=actor, morality=moral, special_motivators=[])        
        gain = edge_yeld[result]
        core.resources.hardware += gain
        actor.skill('survival').get_expirience(result)
    '[name] scavenging junk. Yelds [gain] hardware.'
    return
    
label shd_edge_job_disassemble(action):
    python:
        actor = action.actor
        name = actor.name
        moral = None
        result = core.skillcheck(actor, 'mechanics', difficulty = 1, tense_needs=['amusement', 'comfort'], satisfy_needs=['prosperity'], beneficiar=actor, morality=moral, special_motivators=[])        
        gain = edge_yeld[result]
        core.resources.hardware += gain
        actor.skill('mechanics').get_expirience(result)
    '[name] disasembles old machinery on the ruined factory. Yelds [gain] hardware.'
    return
    
label shd_edge_job_lookforstash(action):
    python:
        actor = action.actor
        place = action.special_values['place']
        difficulty = 5 - int(action.special_values['quality'])
        name = actor.name
        moral = ['chaotic', 'evil']
        result = core.threshold_skillcheck(actor, 'observation', difficulty = difficulty, tense_needs=['amusement', 'comfort'], satisfy_needs=['prosperity'], beneficiar=actor, morality=moral, threshold = 3, special_motivators=[])        
        if result[1] < 1:
            'Fail'
        else:
            'Win'

    return
    
label shd_edge_overtime_nap(action):
    python:
        pass
    'resting...'
    return      
    
label shd_edge_overtime_scout(action):
    python:
        if not edge.maximum_scouted():
            scouted = edge.explore_location()
            message = 'Found %s location.'% scouted.name
        else:
            message = 'Already exlored'
        
    '[message]'
    return        
    
label shd_edge_overtime_foundcamp(action):
    python:
        edge.locations.remove('outworld ruines')
        edge.locations.append('your base camp')
        camp.found()
    'Encamped in outworld ruines.'
    return       
    
    
    