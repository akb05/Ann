from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'
doc = """
Your app description
"""

import random

class Constants(BaseConstants):
    name_in_url = 'pgg'
    players_per_group = 3
    num_rounds = 2
    efficiency_factor = 2
    endowment = c(100)
    lb = 50
    ub = 150


class Subsession(BaseSubsession):
    def creating_session(self):
        for i in self.get_players():
            if self.round_number == 1:
                if self.session.config.get('hetero_endowment'):
                    i.endowment = random.randint(Constants.lb, Constants.ub)
                else:
                    i.endowment = Constants.endowment
            else:
                i.endowment = i.in_round(1).endowment


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    average_contribution = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        self.average_contribution = self.total_contribution / Constants.players_per_group
        for p in self.get_players():
            p.payoff = p.endowment - p.contribution + self.individual_share


class Player(BasePlayer):
    endowment = models.CurrencyField()
    contribution = models.CurrencyField(
        min=0,
        max=Constants.endowment,
        label="How much will you contribute?"
    )
