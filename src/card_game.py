class CardGame:
  def __init__(self, player1_game, player2_game):
    self.player1_game = player1_game
    self.player2_game = player2_game
    self.cardset = [player1_game, player2_game]   

  def highest_card(self):
    if self.player1_game > self.player2_game:
      return self.player1_game
    else:
      return self.player2_game
  
  def cards_total(self):
    total = 0
    for card in self.cardset:
      total += card
    return f"You have a total of {str(total)}"
