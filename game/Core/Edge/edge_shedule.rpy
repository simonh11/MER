##############################################################################
# The Edge of Mists schedule
#
# Script for EOM shedule events

label edge_None_template(actor):
    $ d = actor.description()
    '[d] TOASTED!'
    return
 

## SERVICE SLOT    
label edge_service_whores(actor):
    python:
        name = actor.name
        actor.set_satisfy('eros', 3)
    "[name]fucks whores."
    return

label edge_service_booze(actor):
    python:
        name = actor.name
        actor.set_satisfy('wellness', 3)
    "[name]is drunk. Makes him feel better."
    return

label edge_service_maid(actor):
    python:
        name = actor.name
        actor.set_satisfy('authority', 3)
    "[name]have subservient maid."
    return
         
## OVERTIME SLOT
label edge_overtime_nap(actor):
    python:
        name = actor.name
        actor.add_buff('rested')
    '[name]resting.'
    return      

## FEED SLOT    

label edge_feed_starve(actor):
    python:
        name = actor.name
        ration = actor.food_info()    
    '[name]ration is [ration].'    
    return  

label edge_feed_dry_low(actor):
    python:
        name = actor.name
        actor.eat(1, 0)        
        ration = actor.food_info()  
    'Eating some nutrition bars. [name]ration is [ration].'    
    return  

label edge_feed_dry(actor):
    python:
        name = actor.name
        actor.eat(2, 0)        
        ration = actor.food_info()    
    'Eating nutrition bars. [name]ration is [ration].'    
    return  

label edge_feed_dry_high(actor):
    python:
        name = actor.name
        actor.eat(3, 0)        
        ration = actor.food_info()    
    'Eating nutrition bars greedily. [name]ration is [ration].'    
    return  

label edge_feed_cooked(actor):
    python:
        name = actor.name
        actor.eat(2, 4)        
        ration = actor.food_info()    
    'Eating cooked food in a slums pub. [name]ration is [ration].'    
    return  

label edge_feed_cooked_high(actor):
    python:
        name = actor.name
        actor.eat(3, 4)        
        ration = actor.food_info()  
    'Feasting on a whole grilled girl. [name]ration is [ration].'    
    return  
                    
label edge_feed_canibalism(actor):
    python:
        name = actor.name
    '[name]is a canibal.'    
    return  
   

## ACCOMODATION SLOT    
label edge_accommodation_makeshift(actor):
    python:
        name = actor.name
        person.set_tension('comfort', 'bad_sleep')
        person.set_tension('prosperity', 'homeless')
        person.set_tension('wellness', 'bed_of_rocks')
    "[name]sleeps on a rocky cold ground. It's painful, uncomfortable and reminds of poverty."
    return

label edge_accommodation_mat(actor):
    python:
        person.set_tension('comfort', 'bad_sleep')
        person.set_tension('prosperity', 'poor_accomodation')
        name = actor.name
    "[name]sleeps on a rugged mat in a common room. It's uncomfortable and reminds of poverty."          
    return 

label edge_accommodation_cot(actor):
    python:
        actor.set_satisfy('comfort', 1)    
        name = actor.name
    '[name]sleeps on a rough cot under the ruggy blanket. Well, SOME comfort at least...'    
    return 

label edge_accommodation_appartment(actor):
    python:
        actor.set_satisfy('comfort', 3)    
        person.set_tension('prosperity', 1)
        name = actor.name
    '[name]sleeps on a real bed in a single apartments. Comfortable and even luxurious by the standards of the border.'    
    return  

## JOB SLOT        
label edge_job_idle(actor):
    python:
        name = actor.name
        actor.add_buff('rested')
        txt = encolor_text('some comfort', 2)
    "[name]have no job to do and resting. It's conserves energy and gives [txt]"
    return
   
label edge_job_beg(actor):
    python:
        actor = actor
        name = actor.name
        actor.moral_action(activity = 'timid') 

        person.set_tension('wellness', 'unhealthy_job')
        person.set_tension('prosperity', 'beggar')
        person.set_tension('authority', 'humiliation')        

        actor.eat(1, -1)
        ration = actor.food_info()    
      
    '[name]humbly begs for food and gains a few disgustning leftovers. Disgracing, lowly and definetly not healthy experience. [ration]'
    return
    
label edge_job_bukake(actor):
    python:
        name = actor.name
        person.set_tension('wellness', 'unhealthy_job')
        person.set_tension('comfort', 'tiresome_job')
        person.set_tension('authority', 'humiliation')    
        person.set_tension('eros', 'sexplotation')    
        actor.eat(3, -1)
        ration = actor.food_info()    
        text = __('')
    '[name]humbly sucks stangers diks and consume their semen for nutrition. Nutritive but disgusting. This labor is disgracing, uncomfortable and even painful.'
    'Ration: [ration]'
    return
    
label edge_job_manual(actor):
    python:
        name = actor.name
        result = actor.job_productivity()
        actor.moral_action(orderliness = 'lawful') 
    if result > 0:
        "[name]earns: 10 nutrition bars for manual labor. It's a boring job but brings life to order"
        $ player.add_money(10)
        $ person.set_tension('amusement', 'boring_job')    
    elif result < 0: 
        $ person.set_tension('ambition', 'failure_at_work')    

    return
    
label edge_job_houseservice(actor):
    python:
        name = actor.name
        result = actor.job_productivity()
        actor.moral_action('lawful') 
    if result > 0:
        "[name]earns: 10 nutrition bars for househod services. It's a boring job but brings life to order."
        $ player.add_money(10)
        $ person.set_tension('amusement', 'boring_job')    
    elif result < 0: 
        $ person.set_tension('ambition', 'failure_at_work')    
    return
    
label edge_job_construction(actor):
    python:
        name = actor.name
        yeld = yeld_table[actor.job_productivity()]        
    if yeld > 0:
        "[name]yelds: [yeld] nutrition bars. It's a tiresome job."
        $ player.add_money(yeld)
        $ person.set_tension('comfort', 'tiresome_job') 
    else: 
        $ person.set_tension('prosperity', 'buissiness_fail') 
        $ person.set_tension('ambition', 'failure_at_work')            
    return
    
label edge_job_entertain(actor):
    python:
        name = actor.name
        yeld = yeld_table[actor.job_productivity()]        
    if yeld > 0:
        "[name]yelds: [yeld] nutrition bars. It's a humiliating job."
        $ player.add_money(yeld)
        $ person.set_tension('authority', 'humiliation') 
    else: 
        $ person.set_tension('prosperity', 'buissiness_fail') 
        $ person.set_tension('ambition', 'failure_at_work')            
    return
    
label edge_job_disassembly(actor):
    python:
        name = actor.name
        yeld = yeld_table[actor.job_productivity()]        
    if yeld > 0:
        "[name]yelds: [yeld] nutrition bars. It's a boring job."
        $ player.add_money(yeld)
        $ person.set_tension('amusement', 'boring_job')  
    else: 
        $ person.set_tension('prosperity', 'buissiness_fail') 
        $ person.set_tension('ambition', 'failure_at_work')            
    return
                
label edge_job_range(actor):
    python:
        name = actor.name
    '[name]patroling the Edge of Mists.'
    call lbl_edge_randenc_errant
    return
          
          
          
          
          
          
          
          
            
label shd_edge_job_servitor(actor):
    python:
        name = actor.name
        beneficiar = actor
        actor.moral_action('timid') 
        actor.authority.set_tension()
        actor.comfort.set_tension()
        actor.ambition.set_tension()        
        actor.independence.set_tension()
        text = __(' ministering gang members.')
        target.supervisor.gain_favor(1)
    '[name] [text]'
    return

    
label shd_edge_job_treasurehunt(actor):
    python:
        skill = 'observation'
        difficulty = special_values['difficulty'] 

        name = actor.name
        descr = special_values['description'] 

    call lbl_skillcheck(actor, skill, motivation, difficulty)

    python:
        result = skillcheck.result
        if result > 0:
            trs = edge.gen_treasures
            yeld = __('Found: [trs].')
        else:
            yeld = __('Noting found.')

    '[name] [descr][yeld].'
    return
       

    
    
