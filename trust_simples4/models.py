from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
Simple trust game
"""


class Constants(BaseConstants):
    name_in_url = 'trust_simple'
    players_per_group = 2
    num_rounds = 1

    endowment = c(6)
    multiplier = 3

    playera_role = 'Jugador A'
    playerb_role = 'Jugador B'

    instructions_template = 'trust_simples4/instructions.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    sent_amount_1 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6],
        doc="""Amount sent if you are A""",
        label="Si fueras el jugador A, ¿cuánto enviarías al Jugador B?",
    )

    sent_amount_2_1 = models.IntegerField(
        choices=[0, 1, 2, 3],
        doc="""Amount sent if you are B""",
        label="Si fueras el jugador B y recibieras 3 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
    )
    
    sent_amount_2_2 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6],
        doc="""Amount sent if you are B""",
        label="Si fueras el jugador B y recibieras 6 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
    )
    
    sent_amount_2_3 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        doc="""Amount sent if you are B""",
        label="Si fueras el jugador B y recibieras 9 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
    )
    
    sent_amount_2_4 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        doc="""Amount sent if you are B""",
        label="Si fueras el jugador B y recibieras 12 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
    )
    
    sent_amount_2_5 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        doc="""Amount sent if you are B""",
        label="Si fueras el jugador B y recibieras 15 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
    )
    
    sent_amount_2_6 = models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        doc="""Amount sent if you are B""",
        label="Si fueras el jugador B y recibieras 18 puntos, ¿cuánto enviarías de vuelta al Jugador A?",
    )

    def sent_amount_2_choices(self):
        return currency_range(c(0), self.sent_amount_1 * Constants.multiplier, c(1))

    def set_payoffs(self):
        
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.sent_amount_1 == 0:
            p1.payoff = 10
            p2.payoff = 0
        elif self.sent_amount_1 == 1:
            p1.payoff = Constants.endowment - self.sent_amount_1 + self.sent_amount_2_1
            p2.payoff = self.sent_amount_1 * Constants.multiplier - self.sent_amount_2_1
        elif self.sent_amount_1 == 2:
            p1.payoff = Constants.endowment - self.sent_amount_1 + self.sent_amount_2_2
            p2.payoff = self.sent_amount_1 * Constants.multiplier - self.sent_amount_2_2
        elif self.sent_amount_1 == 3:
            p1.payoff = Constants.endowment - self.sent_amount_1 + self.sent_amount_2_3
            p2.payoff = self.sent_amount_1 * Constants.multiplier - self.sent_amount_2_3
        elif self.sent_amount_1 == 4:
            p1.payoff = Constants.endowment - self.sent_amount_1 + self.sent_amount_2_4
            p2.payoff = self.sent_amount_1 * Constants.multiplier - self.sent_amount_2_4
        elif self.sent_amount_1 == 5:
            p1.payoff = Constants.endowment - self.sent_amount_1 + self.sent_amount_2_5
            p2.payoff = self.sent_amount_1 * Constants.multiplier - self.sent_amount_2_5
        else:
            p1.payoff = Constants.endowment - self.sent_amount_1 + self.sent_amount_2_6
            p2.payoff = self.sent_amount_1 * Constants.multiplier - self.sent_amount_2_6


class Player(BasePlayer):
    pass
