class DecisionLogic:
    def make_decision(self, game_state):
        # Logic to decide the next action based on the game state
        if game_state['player_hand_value'] > 21:
            return 'bust'
        elif game_state['player_hand_value'] == 21:
            return 'win'
        elif game_state['dealer_hand_value'] < 17:
            return 'hit'
        else:
            return 'stand'

    def evaluate_risk(self, decision, game_state):
        # Assess the risk of a given decision
        if decision == 'hit':
            if game_state['player_hand_value'] + 10 > 21:
                return 'high risk'
            else:
                return 'low risk'
        elif decision == 'stand':
            return 'no risk'
        return 'unknown risk'