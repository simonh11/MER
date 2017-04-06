##############################################################################
# The Edge of Mists main
#
# Main script for EOM core module

init -8 python:
    sys.path.append(renpy.loader.transfn("Core/Edge/scrypt"))
    from edge_engine import *
    from edge_camp import *
    
    pass
    def canibalism_unlocker(person, *args, **kwargs):
        person.schedule.set('ration', ScheduleObject('canibalism', edge_feeds_data['canibalism'], True))

    def canibalism_locker(person, *args, **kwargs):
        if len(person.get_corpses()) < 1:
            person.schedule.make_default('ration')

label lbl_edge_main:    
    'The Mist gives you a way...'  
    python:
        edge = EdgeEngine()
        core.set_world(edge)
        edge.go_to_mist()
        edge.init_player_schedule(player)
        player.add_corpse.add_callback(canibalism_unlocker)
        player.remove_corpse.add_callback(canibalism_locker)
        spendings_text = __("Decade bill: ")
        def encolor_resource_text(value):
            new_value = edge.resources.calculate_consumption(value)
            return encolor_text(spending_rate[5-new_value], 5-new_value)
        def encolor_favor_text(value, person):
            new_value = person.calculate_favor(value)
            return encolor_text(favor_rate[new_value], 5-new_value)
        def show_consumption_level():
            consumption = edge.resources.can_tick()
            consumption_level = edge.resources.consumption_level()
            consumption_text = spendings_text + encolor_text(spending_rate[5-consumption_level], 5-consumption_level)
            return consumption_text
        
        ## Main quest
        core.quest_tracker.add_quest(Quest(one_time=True, **quests_data['edge_main_quest']))
        
        ## Houses & Persons
        garantor = None
        edge_sovereign = core.get_faction('serpis')
                        
        # slums_leader = gen_willed_master('human')        
        # slums_leader.add_feature('confident')        
        # slums_faction = edge.add_faction(slums_leader, __('Slums'), 'slums')
        # player.relations(slums_faction)

        # slums_champion = gen_mighty_master('human')          
        # slums_faction.add_member(slums_champion) 
        # slums_faction.set_member_to_role(slums_champion, 'champion') 

        # slums_entertainer = gen_elegant_master('human')    
        # slums_faction.add_member(slums_entertainer)
        # slums_faction.set_member_to_role(slums_entertainer, 'entertainer') 
        
        # slums_medic = gen_wise_master('human')    
        # slums_faction.add_member(slums_medic)
        # slums_faction.set_member_to_role(slums_medic, 'medic') 

    # Special NPC - representative of the Edge        
        edge_recruiter = gen_wise_master('human')  
        edge_sovereign.add_member(edge_recruiter)
        edge_recruiter.set_nickname("Serpis")   


    # Special NPC - slaver of the Edge
        edge_slaver = gen_willed_master('human')
        slavers = core.get_faction('slavers_guild')
        slavers.add_member(edge_slaver)
        edge_slaver.set_nickname("The Slavedriver")
        edge_slaver.add_quest(SlaverQuest(one_time=False, **quests_data['slaver_quest']))
        npc = ['citisen', edge_slaver]

    call lbl_edge_init_questrewards(npc)


    # Special NPC - junker of the Edge
    python:
        edge_junker = gen_willed_master('human')
        edge_sovereign.add_member(edge_junker)
        edge_junker.set_nickname("The Junker")
        edge_junker.add_quest(SexualPleasureQuest(edge_junker, one_time=False, **quests_data['edge_junker_sex']))

        player.relations(edge_junker) 

        npc = ['citisen', edge_junker]

    call lbl_edge_init_questrewards(npc)

    # Special NPC - guard of the Edge
    python:
        edge_guard = gen_mighty_master('human')
        edge_sovereign.add_member(edge_guard)
        edge_guard.set_nickname("The Guard")
        edge_guard.add_quest(FightQuest(edge_guard, one_time=True, **quests_data['edge_guard_duel']))
        armor = create_item('fullplate', 'armor')
        wpn = create_item('sword', 'weapon')
        edge_guard.equip_on_slot('garment', armor)
        edge_guard.equip_on_slot('weapon', wpn)

        player.relations(edge_guard)  

        npc = ['citisen', edge_guard]

    call lbl_edge_init_questrewards(npc)

    
    #slums_leader 'Hi, I am a leader of the Slums'
    #$ player.relations(slums_leader)
    #slums_champion "I'll watch for you"
    #$ player.relations(slums_champion)
    #slums_entertainer 'If you need to relax, welcome to my pub.'
    #$ player.relations(slums_entertainer)
    #slums_medic "I'll patch you if you'l get hurt... for a price!"
    #$ player.relations(slums_medic)    

    call edge_init_events
    call lbl_edge_manage
    return

label lbl_edge_init_questrewards(argument):
    python:
        if argument[0] == 'citisen':
            argument[1].reward = CardsMaker()
            argument[1].reward.add_entry('reward_garantor', edge_quest_rewards)
            argument[1].reward.add_entry('reward_sparks', edge_quest_rewards)
            argument[1].reward.add_entry('reward_banknotes', edge_quest_rewards)
            argument[1].reward.add_entry('reward_bars', edge_quest_rewards)
            argument[1].reward.add_entry('reward_relations', edge_quest_rewards)  
        if argument[0] == 'freeman':
            argument[1].reward = CardsMaker()
            argument[1].reward.add_entry('reward_relations', edge_quest_rewards)  

    return
    
label lbl_edge_manage:
    show expression "interface/bg_base.jpg" as bg
    show screen sc_player_hud
    python:
        target = player
        money = player.money
        bill = player.decade_bill
        enrgy_txt = encolor_text('energy', player.energy)
           
    menu:
        'Opportunities':
            if player.energy > 0:
                call lbl_edge_opportunities 
            else:
                'No energy'
        'Marketplace':
            python:
                knife = create_item('knife', 'weapon')
                edge_recruiter.add_item(knife)
                sword = create_item('sword', 'weapon')
                edge_recruiter.add_item(sword)  
                heavy_axe = create_item('heavy_axe', 'weapon')
                edge_recruiter.add_item(heavy_axe)            
                shield = create_item('shield', 'weapon')
                edge_recruiter.add_item(shield)                                        
                harm = create_item('fullplate', 'armor')
                edge_recruiter.add_item(harm)
                sarm = create_item('hides', 'armor')
                edge_recruiter.add_item(sarm)
                clth = create_item('fine_clothes', 'armor')
                edge_recruiter.add_item(clth)
                jewel = create_item('jewel', 'accessory')
                edge_recruiter.add_item(jewel)                
            call screen sc_trade(edge_recruiter) 

        'Стать богатым':            
            $ player.add_money(1000)
    
    jump lbl_edge_manage
    return

# label lbl_edge_places:
#     menu:
#                     pass
#         'House [edge_sovereign.name] outpost':
#             call lbl_edge_outpost
#         'Hazy marsh' if edge.is_stash_found('hazy_marshes'):
#             $ stash = edge.get_stash('hazy_marshes')
#             call screen sc_manage_stash(stash)   
#         'Echoing hills' if edge.is_stash_found('echoing_hills'):
#             $ stash = edge.get_stash('echoing_hills')
#             call screen sc_manage_stash(stash) 
#         'Dying grove' if edge.is_stash_found('dying_grove'):
#             $ stash = edge.get_stash('dying_grove')
#             call screen sc_manage_stash(stash)              
#         'Edge of Mists':
#             call lbl_edge_randenc_errant
#         'Done':
#             jump lbl_edge_manage
    
#     call lbl_edge_places    
#     return

label lbl_all_gangs:
    python:
        menu_list = [(gang.name, gang) for gang in edge.gang_list]
        menu_list.append(('Leave', 'leave'))
        choice = renpy.display_menu(menu_list)
    if choice == 'leave':
        return
    else:
        call screen sc_gang_info(choice)
    call lbl_all_gangs

label lbl_edge_outpost:
    menu:
        'Slaver' if 'slaver' in edge.options:
            call lbl_edge_slavery
        'Recruiter' if 'recruiter' in edge.options:
            call lbl_edge_hiring            
        'Get out':
            call lbl_edge_manage
        
    call lbl_edge_outpost
    return

label lbl_edge_stashes:
    python:
        stashes = edge.active_stashes()
        stashes = [(edge_locations[i], i) for i in stashes]
        stashes.append((__("leave"), 'leave'))
        stash = renpy.display_menu(stashes)
        if not stash == 'leave':
            stash = edge.get_stash(stash)
    if stash == 'leave':
        return
    call screen sc_manage_stash(stash)
    jump lbl_edge_stashes

label lbl_edge_turn:
    $ edge.new_turn()
    if edge.faction_mode:
        call lbl_edge_faction_livein
    if edge.slums_mode:
        call lbl_edge_manage
    else:
        call lbl_edge_manage        
    return
