from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.player.id_in_group == 1 or self.player.id_in_group == 2


class PaginaDecision(Page):
    form_model = "group"
    form_fields = ["sent_amount_1", "sent_amount_2_1", "sent_amount_2_2", "sent_amount_2_3", "sent_amount_2_4", "sent_amount_2_5",
    "sent_amount_2_6"]
    

class SendBack(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return dict(tripled_amount=self.group.sent_amount_1 * Constants.multiplier)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [Introduction, PaginaDecision, ResultsWaitPage, Results]
