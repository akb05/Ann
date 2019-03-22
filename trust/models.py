from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 1
    efficiency_factor = 3
    endowment = c(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    investment = models.CurrencyField(min=0, max=Constants.endowment,
                                      label=f'Invest something between 0 and {Constants.endowment}')
    multiplied_investment = models.CurrencyField()
    returning_amount = models.CurrencyField(min=0)

    def set_payoffs(self):
        trustor = self.get_player_by_role('trustor')
        trustee = self.get_player_by_role('trustee')
        trustor.payoff = Constants.endowment - self.investment + self.returning_amount
        trustee.payoff = Constants.endowment + self.multiplied_investment - self.returning_amount


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'trustor'
        else:
            return 'trustee'