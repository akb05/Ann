from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class Investment(Page):
    form_model = 'group'
    form_fields = ['investment']

    def is_displayed(self):
        return self.player.role() == 'trustor'

    def before_next_page(self):
        self.group.multiplied_investment = self.group.investment * Constants.efficiency_factor



class AfterInvestmentWP(WaitPage):
    pass

class ReturnStage(Page):
    form_model = 'group'
    form_fields = ['returning_amount']

    def returning_amount_max(self):
        return self.group.multiplied_investment


    def is_displayed(self):
        return self.player.role() == 'trustee'

class BeforeResultsWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):
    pass


page_sequence = [
    Introduction,
    Investment,
    AfterInvestmentWP,
    ReturnStage,
    BeforeResultsWP,
    Results

]
