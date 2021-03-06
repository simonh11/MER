init python:
    relations_translation = {'fervor': {-1: __("delicate"), 0: __("straight"), 1: __("passionate")},
        'distance': {-1: __("intimate"), 0: __("fair"), 1: __("formal")},
        'congruence': {-1: __("hater"), 0: __("associate"), 1: __("admirer")}}

    stance_translation = {'master': [__('cruel'), __('opressive'), __('rightful'), __('benevolent')],
        'slave': [__('rebellious'), __('forced'), __('accustomed'), __('willing')],
        'neutral': [__('hostile'), __('distrustful'), __('favorable'), __('friendly')]}
    stance_types_translation = {'master': __('master'),
        'slave': __('slave'),
        'neutral': __('neutral')}
    alignments_translation = {'orderliness': {-1: __("Chaotic"), 0: __("Conformal"), 1: __("Lawful")},
        'activity': {-1: __("Timid"), 0: __("Reasonable"), 1: __("Ardent")},
        'morality': {-1: __("Evil"), 0: __("Selfish"), 1: __("Good")}}

    mood_translation = {-1: '!!!CRUSHED!!!', 0: 'Gloomy', 1: 'Tense',
        2: 'Content', 3: 'Serene', 4: 'Jouful', 5: 'Enthusiastic'}

    attributes_translation = {
        'physique': __('Endurance'),
        'agility': __('Grace'),
        'mind': __('Wisdom'),
        'spirit': __('Spirit'),
        'anxiety': __('anxiety'),
        'determination': __('determination'),
        'mood': __('mood'),
        'vitality': __('vitality'),
        'motivation': __('motivation'),
        'focus': __('focus')
    }
    skills_translation = {
        'physique': __('Might'),
        'agility': __('Finesse'),
        'mind': __('Knowledge'),
        'spirit': __('Willpower'),
    }
    
    obligations_dict = {
    'master': __('{person.name} is pleased with your efforts'), 
    'slave': __('{person.name} wants to be useful to you'), 
    'hostile': __('{person.name} offers you a payoff'), 
    'neutral': __('{person.name} owes you'), 
    'friendly': __('{person.name} offers you a favor'), 
    }


    discipline_translation = {
        0: encolor_text(__("Independent mind"), 0),
        1: encolor_text(__("Subjected"), 2),
        2: '',
        3: encolor_text(__("Disciplined"), 4),
        4: encolor_text(__("Fidelity"), 5)
    }
    stance_overseer_translation = {
        -1: encolor_text(__("Controversy"), 'red'),
        0: '',
        1: encolor_text(__("Allegiance"), 'green'),
        2: encolor_text(__('Loyality'), 5)
    }
    motivation_translation = {
        -1: "!!!CRUSHED!!!",
        0: "Apatheic",
        1: "Careless",
        2: "Content",
        3: "Motivated",
        4: "Diligent",
        5: "Enthusiastic"
    }
    tokens_translation = {
        'insight': __('insight'),
        'stamina': __('stamina'),
        'grace': __('grace'),
        'willpower': __('willpower'),
        'idea': __('idea'),
        'emotion': __('emotion'),
        'luck': __('luck'),
        'determination': __('determination')
    }

    chances_names = {
        'unhealthy_job': 'Unhealthy job', 
        'beggar': 'Beggar life', 
        'humiliation': 'Humiliation', 
        'tiresome_job': 'Tiresome job', 
        'sexplotation': 'Sexual expluatation', 
        'poor_accomodation': 'Poor accomodation', 
        'bed_of_rocks': 'Bed of rocks', 
        'homeless': 'Homeless', 
        'bad_sleep': 'Bad sleep', 
        'robbery': 'Robbery', 

    }