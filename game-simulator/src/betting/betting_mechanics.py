class BettingMechanics:
    def __init__(self):
        self.pot = 0
        self.bets = {}

    def place_bet(self, player_id, amount):
        if player_id in self.bets:
            self.bets[player_id] += amount
        else:
            self.bets[player_id] = amount
        self.pot += amount

    def resolve_bets(self, winning_player_id):
        winnings = self.pot
        self.pot = 0
        for player_id in self.bets:
            if player_id == winning_player_id:
                return winnings
        return 0