class CardGame:

  def check_for_ace(card):
    if card.value == 1:
      return True
    else:
      return False
  
  def highest_card(cards):
    card1 = cards[0]
    card2 = cards[1]
    if card1.value > card2.value:
      return f"The highest card is {card1.value} of {card1.suit}."
    else:
      return f"The highest card is {card2.value} of {card2.suit}."

  def cards_total(cards):
    total = 0
    for card in cards:
      total += card.value
    return f"You have a total of {str(total)}"

