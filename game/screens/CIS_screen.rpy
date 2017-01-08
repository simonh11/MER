style hoverable_text is text:
    color '#fff'
    underline True
    hover_background '#fff'
style char_info_window is window:
    background Color((0, 0, 0, 255))

screen sc_character_info_screen(person, return_l=False, communicate=False):
    python:
        if person.player_controlled:
            mood = encolor_text(mood_translation[person.mood], person.mood)
        else:
            mood = encolor_text(motivation_translation[person.motivation()], person.motivation())
    modal True
    window:
        xfill True
        yfill True
        xalign 0.0
        yalign 0.0
        style 'char_info_window'
        hbox:
            frame:
                vbox:
                    
                    hbox:
                        if person.has_feature('dead'):
                            image im.Grayscale(im.Scale(person.avatar_path, 150, 150))
                        else:  
                            image im.Scale(person.avatar_path, 150, 150)
                        vbox:
                            if communicate:
                                textbutton 'Communicate' action Function(renpy.call_in_new_context, 'lbl_communicate', person)
                            textbutton 'Leave' action If(return_l, Return(),false=Hide('sc_character_info_screen'))
                    hbox:
                        spacing 10
                        vbox:
                            for i in person.visible_features():
                                text i.name
                        vbox:
                            for i in person.items:
                                textbutton i.name:
                                    text_style 'hoverable_text'
                                    style 'hoverable_text'
                                    action NullAction()
                                    hovered Show('sc_weapon_info', weapon=i)
                                    unhovered Hide('sc_weapon_info')
                    frame:
                        vbox:
                            text encolor_text(__('Allure'), person.allure())
                            text encolor_text(__('Hardiness'), person.hardiness())
                            text encolor_text(__('Succulence'), person.succulence())
                            text encolor_text(__('Purity'), person.purity())
                            text encolor_text(__('Exotic'), person.exotic())
                            text encolor_text(__('Style'), person.style())
                            text encolor_text(__('Menace'), person.menace())
            vbox:
                hbox:
                    xalign 0.32
                    frame:
                        
                        vbox:
                            text person.full_name():
                                size 25
                            text person.age + ' ' + person.gender + ' ' + person.genus.name + ' ' + '(%s)'%person.kink
                            
                            hbox:
                                text "{0} {1} {2} ".format(*person.alignment.description())
                                if person.player_controlled:
                                    textbutton "({mood})".format(mood=mood):
                                        style 'hoverable_text'
                                        text_style 'hoverable_text'
                                        hovered Show('sc_mood_info', person=person)
                                        unhovered Hide('sc_mood_info')
                                        action NullAction()
                            if person != core.player:
                                text (person.stance(player).show_type() + ' ' +
                                    '{0} {1} {2}'.format(*person.relations(player).description()))
                            text "{b}%s{/b}"%encolor_text("Energy", person.energy)
                    frame:
                        vbox:
                            text '{b}Skills{/b}'
                            for i in person.get_all_skills():
                                if i.level != 1:
                                    textbutton encolor_text(i.name, i.level) + '(%s)'%i.level:
                                        style 'hoverable_text'
                                        text_style 'hoverable_text'
                                        hovered Show('sc_skill_info', skill=i)
                                        unhovered Hide('sc_skill_info')
                                        action NullAction()
                            if person.focused_skill is not None:
                                $ i = person.focused_skill
                                text '{b}Focus:{/b}'
                                text encolor_text(i.name, i.focus) + '(%s)'%i.focus
                if any([person.get_buffs()]):
                    frame:
                        vbox:
                            for i in person.get_buffs():
                                text encolor_text(i.name, i.color())
        if person.has_resources():
            frame:
                xalign 1.0
                yalign 1.0
                vbox:
                    textbutton 'Tokens' action Show('sc_tokens', person=person)

init python:
    active_determination = None

screen sc_tokens(person):
    $ tokens = person.inner_resources
    modal True
    window:
        xfill True
        yfill True
        xalign 0.0
        yalign 0.0
        style 'char_info_window'
        hbox:
            frame:
                xsize 200

                vbox:
                    text 'Attributes'
                    for i in tokens:
                        if i['name'] != 'luck' and i['name'] != 'determination':
                            textbutton encolor_text(tokens_translation[i['name']], i['value']):
                                action [SensitiveIf(person.can_upgrade_resource(i, active_determination)),
                                    Function(person.apply_determination, i, active_determination),
                                    SetVariable('active_determination', None)]
                                
            frame:
                xsize 250
                vbox:
                    text 'Determination'
                    for i in tokens:
                        if i['name'] == 'determination':
                                textbutton encolor_text(tokens_translation[i['name']], i['value']):
                                    action [If(active_determination is None, SetVariable('active_determination', i)),
                                        If(active_determination == i, SetVariable('active_determination', None)),
                                        If(active_determination is not None and i != active_determination,
                                            Function(person.unite_determinations, i, active_determination)),
                                        If(active_determination is not None and i != active_determination,
                                            SetVariable('active_determination', None))]
                                    selected active_determination == i
                                    if active_determination is not None:
                                        if active_determination != i:
                                            sensitive active_determination['value'] < 5
            frame:
                xsize 200
                vbox:
                    text "Focus"
                    for key, value in person.focus_dict.items():
                        if value > 0:
                            text encolor_text(key + ' ' + __('insight'), value)
            frame:
                xsize 200
                vbox:
                    text 'Luck'
                    for i in person.luck_tokens:
                            text encolor_text(tokens_translation['luck'], i)
        textbutton 'Leave' action Hide('sc_tokens'):
            xalign 0.5
            yalign 1.0
            xsize 200

screen sc_skill_info(skill):
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            for i in skill.description:
                text i
        

screen sc_info_popup(person):
    window:  
        xfill False
        xalign 0.5
        yalign 0.0
        vbox:
            xalign 0.5
            text person.full_name():
                size 25
            text person.age + ' ' + person.gender + ' ' + person.genus.name + ' ' + '(%s)'%person.kink
            text "{0} {1} {2} ({mood})".format(*person.alignment.description(),
                mood=encolor_text(person.show_mood(), person.mood))
            if person != player:
                text (person.stance(player).show_type() + ' ' +
                    '{0} {1} {2}'.format(*person.relations(player).description()))
            for i in person.visible_features():
                text i.name
            for i in person.equiped_items():
                text i.name

screen sc_mood_info(person):
        frame:
            xalign 0.5
            yalign 0.5
            vbox:
                spacing 5
                if person.life_level > 0:
                    text encolor_text('Life quality', 'green')
                elif person.life_level < 0:
                    text encolor_text("Life quality", 'red')
                else:
                    text encolor_text("Life quality", 2)

                if person.selfesteem is not None:
                    if person.selfesteem < 0:
                        text encolor_text(__('Faithless'), 'red')
                    elif person.selfesteem > 0:
                        text encolor_text(__('Faithful'), 4)
                    else:
                        text encolor_text(__('Cynical'), 2)
                
                if not person.player_controlled:
                
                    if person.stimul < 0:
                        text encolor_text(__('Punished'), 2)
                    elif person.stimul > 0:
                        text encolor_text(__('Rewarded'), 'green')
                    else:
                        text encolor_text(__('Uninterested'), 'red')

                    if person.master is None:
                        text encolor_text(__("Own choice"), 'green')
                    else:
                        if person.discipline != 2:
                            text discipline_translation[person.discipline]

                    if person.overseer is not None:
                        if person.discipline != 0:
                            text stance_overseer_translation[person.overseer_stance().value]
                else:
                    if person.joy == 1:
                        text encolor_text("Joy", 'green')
                    if person.success == 1:
                        text encolor_text("Success", 'green')
                    if person.purporse == 1:
                        text encolor_text("Purporse", 5)


                

screen sc_weapon_info(weapon):
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 5
            text weapon.stats()
            if weapon.description is not None:
                text weapon.description()
            text 'price: ' + str(weapon.price)

screen sc_vitality_info(person):
    $ d, l = person.vitality_info()
    python:
        list_ = list(d.items())
        for i in l:
            list_.append(i)
    frame:
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 10
            vbox:
                text 'Good'
                for k, v in list_:
                    if v > 0:
                        text encolor_text(k, v)
            vbox:
                text 'Bad'
                for k, v in list_:
                    if v < 0:
                        text encolor_text(k, 0)
            vbox:
                text 'Nonfactors'
                for k, v in list_:
                    if v == 0:
                        text encolor_text(k, 6)

