label lbl_tokens_game(tokens_game):
    call screen sc_tokens_game(tokens_game)
    return


screen sc_tokens_game(tokens_game):
    window:
        xfill True
        yfill True
        window:
            xalign 0.5
            yalign 0.5
            yfill False
            xsize 610
            ysize 150
            text encolor_text(__("Opportunities"), tokens_game.chances):
                xalign 0.5
                yalign 0.0
            if tokens_game.failed:
                text encolor_text(__("Procrastination"), 'red')

            hbox:
                yalign 0.5
                spacing 3
                
                for i in range(0, 3):
                    $ value = tokens_game.revolver[i]
                    $ key = i
                    vbox:
                        frame:
                            xsize 200
                            ysize 50
                            if value is not None:
                                text encolor_text(value['name'], value['value'])
                        if tokens_game.roll_phase:
                            if value is None:
                                textbutton 'Roll':
                                    xsize 200
                                    ysize 30
                                    action Function(tokens_game.fill_revolver, key)
                            else:
                                textbutton 'Take':
                                    xsize 200
                                    ysize 30
                                    action [Function(player.add_inner_resource, **value), 
                                        Function(tokens_game.clear), Function(tokens_game.stop_rolling)]
    if not tokens_game.roll_phase:
        vbox:
            xalign 0.5
            yalign 1.0
            textbutton "Take chance":
                xsize 200
                action [Function(tokens_game.start_rolling),
                    SensitiveIf(tokens_game.chances > -1)]
            textbutton 'Done':
                action Return()
                xsize 200



init python:
    import collections
    class TokensGame(object):

        _tokens = {'stamina': 'physique', 'grace': 'agility',
            'willpower': 'spirit', 'idea': 'mind', 'emotion': 'sensitivity'}
        def __init__(self, person):
            self.chances = person.vitality
            self.roll_phase = False
            self.failed = False
            self.person = person
            self.revolver = {0: None, 1: None, 2: None}
            renpy.call_in_new_context('lbl_tokens_game', self)


        def start_rolling(self):
            self.chances -= 1
            self.roll_phase = True
            self.failed = False

        def stop_rolling(self):
            self.roll_phase = False


        def init_tokens(self):
            tokens = []
            for key, attribute in self._tokens.items():
                tokens.append({'name': key, 'attribute': attribute, 'value': getattr(self.person, attribute)})
            tokens.append(self.gen_luck_token())
            tokens.append(self.gen_determination_token())
            focus = self.gen_focus_token()
            if focus is not None:
                tokens.append(focus)
            return tokens

        def clear(self):
            self.revolver = {0: None, 1: None, 2: None}


        def gen_luck_token(self):
            value = randint(1, 5)
            token = {'name': 'luck', "attribute": 'any', 'value': value}
            return token

        def gen_determination_token(self):
            value = self.person.mood
            return {'name': 'determination', 'attribute': 'any', 'value': value}

        def gen_focus_token(self):
            focus = self.person.focused_skill
            if focus is None:
                return
            name = focus.name
            token_name = __('insight') + '_' + name
            value = self.person.get_focus(focus.id)
            if value == 5:
                return
            return {'name': token_name, 'attribute': 'focus', 'value': value+1}
        def fill_revolver(self, number):
            tokens = self.init_tokens()
            token = choice(tokens)
            if token['name'] == 'determination':
                if token['value'] == 0:
                    self.clear()
                    self.stop_rolling()
                    self.failed = True
                    return
            left = self.revolver.get(number-1)
            right = self.revolver.get(number+1)
            if left is not None:
                if left['name'] == token['name']:
                    token['value'] += 1
                    left['value'] += 1
            elif right is not None:
                if right['name'] == token['name']:
                    token['value'] += 1
                    right['value'] += 1
            if token['value'] > 5:
                token['value'] = 5

            self.revolver[number] = token