# Edge of Mists locations

label lbl_edge_missed_location:
    menu:
        'Explore all (job)' if len(edge.locations) < edge.loc_max:
            $ target.schedule.add_action('job_explore', 1)       
        'Go back':
            $pass
    call lbl_edge_manage
    return
    
label lbl_edge_outpost(location):
    menu:
        'Bukake-slut for food (full time)':
            $ special_values = {'skill': 'sex', 'beneficiar': player, 'slut_rate': 0,}
            menu:
                'More dicks you suck, more miserable you feel. Who you will feed upon?'
                'Gentle and clean humans':
                    $ special_values['slut_rate'] = 1
                'Clean humans':
                    $ special_values['slut_rate'] = 2
                'Humans':
                    $ special_values['slut_rate'] = 3
                'Humans and beastmans':
                    $ special_values['slut_rate'] = 4
                'All dicks you can find':
                    $ special_values['slut_rate'] = 5                  
                'No one':
                    jump lbl_edge_locations_menu
            $ target.schedule.add_action('job_bukake', special_values=special_values)  
        'Prostitute for money (full time)':
            $ description = ' fucks for a price. Yelds '
            $ special_values = {'description': description, 'resource_name': 'money', 'skill': 'sex', 'difficulty' : 1, 'moral': None, 'tense': ['wellness', 'comfort'], 'statisfy': ['prosperity', 'communication', 'eros'], 'beneficiar': player,}
            $ target.schedule.add_action('job_moneywork',special_values=special_values)         
        'Trade':
            call screen sc_universal_trade
        'Get out':
            return 
                
    call lbl_edge_outpost(location)
    return

label lbl_edge_shifting_mist(location=None):
    'Battle'
    python:
        ally1 = DuelCombatant(player)
        
        enemy_weapon = Weapon('twohand', 'subdual', quality=1)
        enemy_armor = Armor('heavy_armor', quality=1)
        enemy = gen_random_person('human')
        enemy.main_hand = enemy_weapon
        enemy.armor = enemy_armor
        enemy1 = DuelCombatant(enemy)

        
        fight = DuelEngine([ally1],[enemy1], None)
        fight.start()
    return

label lbl_edge_grim_battlefield(location):
    $ dif = encolor_text('straightforward', 1)
    $ achive = encolor_text('adequate results', 2)
    
    menu:
        'The tides of Mist brought here an old battlefield full of dead bodies and battered armaments. Territory is under control of [location.owner.name]. You can see a few scavergers here and there, they looking for usible munitions.'
        'Find out about [location.owner.name]':
            call screen sc_faction_info(location.owner)
        'Work for food (full time)':
            menu:
                'The [location.owner.name] offer to give you some food (3 provisions units) if you {b}scavenge{/b} armaments for them for a decade. It is [dif] task, but you must achieve [achive] in order to get your reward.'
                'Agree':
                    $ special_values = {'skill': 'survival', 'moral': ['lawful', 'timid'], 'beneficiar': location.owner, 'difficulty': 1}
                    $ special_values['succes_text'] = _('scavenging munition on the grim battlefield for a local gang, but fails to deliver. No food recived.')                    
                    $ special_values['fail_text'] = _('succesfully scavenging munition on the grim battlefield for a local gang. Recived food (3)')
                    $ target.schedule.add_action('job_foodwork', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Pay a tool for scavenge (full time)':
            menu:
                'You must pay 100 banknotes to [location.owner.name] in order to scavenge their territory for usible munitions for a decade. All you can find and carry out is yours.'
                'Agree (100 banknotes)' if core.resources.money >= 100:
                    $ core.resources.money -= 100
                    $ description = _('scavenging munition on the gim battlefield. Yelds ')
                    $ special_values = {'description': description,  'resource_name': 'munition', 'skill': 'survival', 'difficulty' : 1, 'moral': None, 'tense': ['amusement', 'comfort'], 'statisfy': ['prosperity'], 'beneficiar': player,}
                    $ target.schedule.add_action('job_simplework', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Ask to join the [location.owner.name] gang' if not core.has_any_faction(player):
            $ location.owner.add_member(player)
            $ edge.faction_mode = True
            jump lbl_edge_faction_livein
        'Get out':
            return 

    call lbl_edge_grim_battlefield(location) 
    return

label lbl_edge_crimson_pit(location):
    $ dif = encolor_text('straightforward', 1)
    $ achive = encolor_text('adequate results', 2)
    
    menu:
        'Dense smoke and the smell of burned tar guides you to a enormous scorched pit. You can see a pool of glossy crimson liquid on its bottom, the infamous "Demon Blood", fuel of Eternal Rome. Place is guarded by [location.owner.name] while tired workers mine the substance.'
        'Find out about [location.owner.name]':
            call screen sc_faction_info(location.owner)
        'Work for food (full time)':
            menu:
                'The [location.owner.name] offer to give you some food (3 provisions units) if you will work at the pit for a decade. The {b}athletics{/b} skill could be helpful. It is [dif] task, but you must achieve [achive] in order to get your reward.'
                'Agree':
                    $ special_values = {'skill': 'athletics', 'moral': ['lawful', 'timid'], 'beneficiar': location.owner, 'difficulty': 1}
                    $ special_values['succes_text'] = _('working for local gang, but fails to deliver. No food recived.')                    
                    $ special_values['fail_text'] = _('succesfully works for a local gang. Recived food (3)')
                    $ target.schedule.add_action('job_foodwork', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Buy extraction license (full time)':
            menu:
                'You must pay 100 banknotes to [location.owner.name] in order to work here for a decade. All fuel you can extract and carry out is yours.'
                'Agree (100 banknotes)' if core.resources.money >= 100:
                    $ core.resources.money -= 100
                    $ description = _('extracts demon blood and renders it to a fuel bars. Yelds ')
                    $ special_values = {'description': description,  'resource_name': 'fuel', 'skill': 'athletics', 'difficulty' : 1, 'moral': None, 'tense': ['amusement', 'comfort'], 'statisfy': ['prosperity'], 'beneficiar': player,}
                    $ target.schedule.add_action('job_simplework', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Ask to join the [location.owner.name] gang' if not core.has_any_faction(player):
            $ location.owner.add_member(player)
            $ edge.faction_mode = True
            jump lbl_edge_faction_livein
        'Get out':
            return 

    call lbl_edge_crimson_pit(location) 
    return

label lbl_edge_junk_yard(location):
    $ dif = encolor_text('straightforward', 1)
    $ achive = encolor_text('adequate results', 2)
    
    menu:
        'Junk yard. Owned by [location.owner.name].'
        'Find out about [location.owner.name]':
            call screen sc_faction_info(location.owner)
        'Work for food (full time)':
            menu:
                'The [location.owner.name] offer to give you some food (3 provisions units) for a decade of a hard labor. The {b}survival{/b} skill will be helpful. It is [dif] task, but you must achieve [achive] in order to get your reward.'
                'Agree':
                    $ special_values = {'skill': 'survival', 'moral': ['lawful', 'timid'], 'beneficiar': location.owner, 'difficulty': 1}
                    $ special_values['succes_text'] = _('working for local gang, but fails to deliver. No food recived.')                    
                    $ special_values['fail_text'] = _('succesfully works for a local gang. Recived food (3)')
                    $ target.schedule.add_action('job_foodwork', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Buy scavenger license (full time)':
            menu:
                'You must pay 100 banknotes to [location.owner.name] in order to work here for a decade.'
                'Agree (100 banknotes)' if core.resources.money >= 100:
                    $ core.resources.money -= 100
                    $ description = _('scavenges the hardvare on a junk yard. Yelds ')
                    $ special_values = {'description': description,  'resource_name': 'hardware', 'skill': 'survival', 'difficulty' : 1, 'moral': None, 'tense': ['amusement', 'comfort'], 'statisfy': ['prosperity'], 'beneficiar': player,}
                    $ target.schedule.add_action('job_simplework', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Ask to join the [location.owner.name] gang' if not core.has_any_faction(player):
            $ location.owner.add_member(player)
            $ edge.faction_mode = True
            jump lbl_edge_faction_livein
        'Get out':
            return 

    call lbl_edge_junk_yard(location) 
    return

label lbl_edge_ruined_factory(location):
    $ dif = encolor_text('straightforward', 1)
    $ achive = encolor_text('adequate results', 2)
    
    menu:
        'Ruinded factory. Owned by [location.owner.name].'
        'Find out about [location.owner.name]':
            call screen sc_faction_info(location.owner)
        'Work for food (full time)':
            menu:
                'The [location.owner.name] offer to give you some food (3 provisions units) for a decade of a hard labor. The {b}mechanics{/b} skill will be helpful. It is [dif] task, but you must achieve [achive] in order to get your reward.'
                'Agree':
                    $ special_values = {'skill': 'mechanics', 'moral': ['lawful', 'timid'], 'beneficiar': location.owner, 'difficulty': 1}
                    $ special_values['succes_text'] = _('working for local gang, but fails to deliver. No food recived.')                    
                    $ special_values['fail_text'] = _('succesfully works for a local gang. Recived food (3)')
                    $ target.schedule.add_action('job_foodwork', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Buy scavenger license (full time)':
            menu:
                'You must pay 100 banknotes to [location.owner.name] in order to work here for a decade.'
                'Agree (100 banknotes)' if core.resources.money >= 100:
                    $ core.resources.money -= 100
                    $ description = _('scavenges the hardvare on a junk yard. Yelds ')
                    $ special_values = {'description': description,  'resource_name': 'hardware', 'skill': 'mechanics', 'difficulty' : 1, 'moral': None, 'tense': ['amusement', 'comfort'], 'statisfy': ['prosperity'], 'beneficiar': player,}
                    $ target.schedule.add_action('job_simplework', 1, special_values=special_values)  
                    jump lbl_edge_manage
                'Decline':
                    $ pass
        'Ask to join the [location.owner.name] gang' if not core.has_any_faction(player):
            $ location.owner.add_member(player)
            $ edge.faction_mode = True
            jump lbl_edge_faction_livein
        'Get out':
            return 

    call lbl_edge_junk_yard(location) 
    return
    
label lbl_edge_squatted_slums(location):
    menu:
        'Slums squatted by [location.owner.name] gang are open to live in... for a price.'
        'Sign in':
            $ edge.slums_mode = True
            call lbl_edge_slums_livein
        'Get out':
            return         
    
    call lbl_edge_squatted_slums(location)
    return

label lbl_edge_dying_grove(location):
    $ special_values = {'place': 'grove', 'quality': location.cache}
    menu:
        'Look for hidden stash (job)':
            $ target.schedule.add_action('job_lookforstash', 1, special_values=special_values)  
            jump lbl_edge_schedule
        'Go back':
            $ pass            
        
    jump lbl_edge_locations_menu             
    return

label lbl_edge_hazy_marsh(location):
    $ special_values = {'place': 'marsh', 'quality': location.cache}
    menu:
        'Look for hidden stash (job)':
            $ target.schedule.add_action('job_lookforstash', 1, special_values=special_values)  
            jump lbl_edge_schedule
        'Go back':
            $ pass            
        
    jump lbl_edge_locations_menu        
    return
    
label lbl_edge_echoing_hills(location):
    $ special_values = {'place': 'hills', 'quality': location.cache}
    menu:
        'Look for hidden stash (job)':
            $ target.schedule.add_action('job_lookforstash', 1, special_values=special_values)  
            jump lbl_edge_schedule
        'Go back':
            $ pass            
        
    jump lbl_edge_locations_menu        
    return
