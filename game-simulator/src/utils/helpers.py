def format_output(message):
    return f"*** {message} ***"

def calculate_odds(winning_outcomes, total_outcomes):
    if total_outcomes == 0:
        return 0
    return winning_outcomes / total_outcomes