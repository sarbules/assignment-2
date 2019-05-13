"""
Blackjack card game - simplified version.
"""

import random
import sys

def deal(deck):
    """
    shuffle the deck and draw the first two cards
    """
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand

def play_again():
    again = input("Do you wish to start a new game? (y/n) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        game()
    else:
        print("Bye!")
        exit()

def total(hand):
    """
    calculates the total of cards
    """
    total = 0
    for card in hand:
        total += card
    return total

def hit(hand, deck):
    """
    draw a new card from the deck
    """
    card = deck.pop()
    hand.append(card)
    return hand

def print_results(dealer_hand, player_hand):
    """
    print the final result
    """
    print("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)) + ".")
    print("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)) + ".")
    print("Your total is " + str(total(player_hand)) + " and the dealer's total is " + str(total(dealer_hand)) + ".")

def score(dealer_hand, player_hand):
    """
    indicates the winner
    """
    if total(player_hand) == total(dealer_hand): #dealer wins all ties
        print_results(dealer_hand, player_hand)
        print("Tie! The dealer wins!.\n")
    elif total(dealer_hand) == 21: #blackjack for dealer
        print_results(dealer_hand, player_hand)
        print("The dealer got a blackjack. The dealer wins!\n")
    elif total(player_hand) == 21: #blackjack for player
        print_results(dealer_hand, player_hand)
        print("You got a Blackjack! You win!\n")
    elif total(player_hand) > 21: #total exceed 21 for player; the player loses the game to the dealer
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose!\n")
    elif total(player_hand) < total(dealer_hand): #dealer score is higher
        print_results(dealer_hand, player_hand)
        print("Your score isn't higher than the dealer. You lose!\n")
    elif total(player_hand) > total(dealer_hand): #player score is higher
        print_results(dealer_hand, player_hand)
        print("Your score is higher than the dealer. You win!\n")

def stand_choice(dealer_hand, deck):
    """
    if player reaches the total of 21 or if the player choose to stand
    then the dealer turn begings by revealing the hidden card and the draws
    """
    print("The dealer hidden card is a " + str(dealer_hand[-1]) + " and has a total of "  + str(total(dealer_hand)) + ".")
    while total(dealer_hand) <= 16: #the dealer must hit if the total is 16 or less
        hit(dealer_hand, deck)
        print("Hit! The dealer draws " + str(dealer_hand[-1]) + ". The dealer total is "  + str(total(dealer_hand)) + ".")
        if total(dealer_hand) >= 17: #print stand msg for the dealer
            print("The dealer stands.")

def game():
    choice = ''
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]*4
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print("You draw a " + str(player_hand[0]) + " and a " + str(player_hand[1]) + ". Your total is " + str(total(player_hand)) + ".")
    print("The dealer draws a " + str(dealer_hand[0]) + " and a hidden card.")

    strmsg = ''
    while True:
        try:
            choice = input(f'Hit or stand? (h/s): ').lower()
            if choice == "h":
                while total(player_hand) < 21:
                    hit(player_hand, deck)
                    if total(player_hand) >= 21: #if player reaches 21, the player stands and dealer turn begins by revealing the hidden card
                        stand_choice(dealer_hand, deck)
                    else:
                        strmsg = "Hit! You draw a " + str(player_hand[-1]) + ". Your total is " + str(total(player_hand))
                        choice = input(f'{strmsg}. Hit or stand? (h/s): ').lower()
                        if choice == "s":
                            print("You stand.")
                            stand_choice(dealer_hand, deck)
                            break
                score(dealer_hand, player_hand) #check the score
                play_again()
            elif choice == "s":
                print("You stand.")
                stand_choice(dealer_hand, deck)
                score(dealer_hand, player_hand) #check the score
                play_again()
            else:
                print("Bye!")
                exit()
        except KeyboardInterrupt:
            print('Bye bye...')
            sys.exit()


if __name__ == "__main__":
    print("Welcome to Blackjack.")
    print('-'*75)
    game()
