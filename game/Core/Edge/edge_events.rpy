##############################################################################
# The Edge of Mists events
#
# Script for EOM main events

 
# !!!!!! REGISTER EACH EVENT HERE !!!!
label edge_init_events:
    $ register_event('evn_edge_uneventful')
    $ register_event('evn_edge_mistadvance')
    $ register_event('evn_edge_slaver')
    $ register_event('evn_edge_recruiter')
    
    return True
    
#TESTS & TEMPLATES 

label evn_edge_blank:
   $pass   
   return True
  
label evn_edge_template(event):
    
    #Проверка для турн энда
    if not event.skipcheck:
        if True:
            $ event.skipcheck = True
    # Вообще это должно делаться не так, но в сыче пойдет
    if event.target != child:
        $ event.skipcheck = False 
    
    # Отсечка
    if not event.skipcheck:
        return False
       
        
    #тело эвента
    return True

############## HERO EVENTS ##################



############## EXPLORATION ##################
      
label evn_edge_slaver(event):
    
    #Проверка для турн энда
    if not event.skipcheck:
        if 'slaver' not in edge_exploration:
            $ event.skipcheck = True
        else:
            $ edge_exploration.remove('slaver')
    
    # Отсечка
    if not event.skipcheck:
        return False
       
        
    #тело эвента
    edge_slaver 'Hey! Now you know me!'
    'You found a slaver, new options in Outpost'
    $ edge.options.append('slaver')
    $ player.relations(edge_slaver)
    return True
      
label evn_edge_recruiter(event):
    
    #Проверка для турн энда
    if not event.skipcheck:
        if 'recruiter' not in edge_exploration:
            $ event.skipcheck = True
        else:
            $ edge_exploration.remove('recruiter')
    
    # Отсечка
    if not event.skipcheck:
        return False
       
        
    #тело эвента
    edge_recruiter 'Hey! Do you wanna be a Noble House servant?!'
    'You found a recruiter, new options in Outpost'
    $ edge.options.append('recruiter')
    $ player.relations(edge_recruiter)
    return True
        
############## NO CHARACTER EVENTS ##################

label evn_edge_uneventful(event):    
    'Unevetful decade...'    
    return True
    
label evn_edge_mistadvance(event):
    if len(edge.locations) == 0:
        $ event.skipcheck = False 
    if not event.skipcheck:
        return False
    python:
        loc_list = [location for location in edge.locations if not location.permanent]
        to_remove = choice(loc_list)
        edge.remove_location(to_remove)
    'Mists take over [to_remove.name] location'
    return True
