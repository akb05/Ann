from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=18, max=100,
                              label='How old are you?')
    gender = models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')],
                                 label='What is your gender?',
                                 widget=widgets.RadioSelectHorizontal)
    income = models.IntegerField(label='What is your monthly income?',
                                 choices=[(500, '<1000'),
                                          (1500, '1000-2000'),
                                          (2500, '2000-3000')])
    # FloatField --> da können sie alles mögliche eingeben

    # for each player; get ist im String --> definieren hier eine Funktion



    def get_years_till_retirement(self):
        if self.gender == 1:
            return 60 - self.age
        else:
            return 63 - self.age
    reveal = models.BooleanField(label = 'DO you want PI revealed',
                                choices=[(False, 'Nope'), (True, 'Yes')])
