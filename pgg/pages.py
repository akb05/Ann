from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def vars_for_template(self):
        return {'mylabel': f'Please choose your investment btw 0 to {Constants.endowment}'}

    def contribution_max(self):
        return self.player.endowment


class DecisionWP(WaitPage):

    def after_all_players_arrive(self):
       self.group.set_payoffs()


class Results(Page):
    #    def after_all_players_arrive(self):
    pass

class final(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Introduction,
    Contribution,
    DecisionWP,
    Results,
    final,

]
