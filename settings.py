from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'questionnaire',
        'display_name': "Questionnaire",
        'num_demo_participants': 2,
        'app_sequence': ['questionnaire'],
        'treatment': True
    },

    {
        'name': 'firstapp',
        'display_name': "First App",
        'num_demo_participants': 1,
        'app_sequence': ['first_app'],
    },

    #{
    #    'name': 'trust',
    #    'display_name': "Trust Game",
    #    'num_demo_participants': 2,
    #    'app_sequence': ['questionnaire', 'trust'],
    #    'treatment': True
    #},

     {
         'name': 'pgg_baseline',
         'display_name': "PGG",
         'num_demo_participants': 3,
         'app_sequence': ['pgg'],
         'hetero_endowment': False
         #'use_browser_bots': True
     },

{
         'name': 'pgg_het',
         'display_name': "PGG-heterogeneous endowment",
         'num_demo_participants': 3,
         'app_sequence': ['pgg'],
         'hetero_endowment': True
         #'use_browser_bots': True
     },

]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'sd3)pbk6ji#h37^g3v4w01%r5&0v%tq8(1g0^lap%enjunc3q7'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
