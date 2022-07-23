class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def check_for_ace(self):
    if self.value == 1:
      return True
    else:
      return False
