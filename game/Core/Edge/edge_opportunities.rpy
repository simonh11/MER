## Opportunities

label lbl_edge_opportunities:
    
    #TODO
    
    call lbl_edge_manage
    return

label lbl_edge_feed_hungry:
    if player.money < 5:
        'You have no spare food.'
        return 
    else:
        $ player.money -= 5
        'You feed the hungry one.'
        $ player.moral_action(target=visavis, moral='good') 
    return
    
label lbl_edge_look_troble:
    $ player.moral_action(target=visavis, activity='ardent') 
    call edge_job_range(player)
    
    return
        
label lbl_edge_observe:
    python:
        'Observing...'
        rnd = choice(edge_exploration)
        evn = 'evn_edge_' + rnd
        call_event(evn, player)
    
    return
