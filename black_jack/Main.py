import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    print(logo)
    player_cards = deal_cards(cards, 2)
    computer_cards = deal_cards(cards, 2)
    print(f"Your cards are : {player_cards} , Total Score {sum(player_cards)}")
    print(f"Computer's first card : {computer_cards[0]}")
    need_third_card = input("Type 'y' if you need a third card,type 'n' to pass : ")
    if need_third_card.lower() == 'y':
        player_cards.extend(deal_cards(cards, 1))
        if sum(computer_cards) < 17:
            computer_cards.extend(deal_cards(cards,1))
        judge(player_cards, computer_cards)
    else:
        if sum(computer_cards) < 17:
            computer_cards.extend(deal_cards(cards,1))
        judge(player_cards, computer_cards)


def deal_cards(list , number_cards):
    return random.sample(list,number_cards)


def check_eleven(cards):
    return list(map(lambda x: x.replace(11,1),cards))


def judge(player_cards,computer_cards):
    print(f"Your cards are : {player_cards} , Total Score {sum(player_cards)}")
    print(f"Computer cards are : {computer_cards} , Total Score {sum(computer_cards)}")
    #checking if any of them have gone above 21
    if sum(player_cards) > 21:
        if 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
            print(f"Your cards are : {player_cards} , Total Score {sum(player_cards)}")
        else:
            print("You went over you loose!!")
            return
    elif sum(computer_cards) > 21:
        if 11 in computer_cards:
            computer_cards.remove(11)
            computer_cards.append(1)
            print(f"Computer cards are : {computer_cards} , Total Score {sum(computer_cards)}")
        else:
            print("Computer went over, you Win!!")
            return
    if sum(player_cards) > sum(computer_cards):
        print("You Win!!")
    elif sum(player_cards) == sum(computer_cards):
        print("Draw!!")
    else:
        print("You Loose!!!")


run_game = True
while(run_game):
    user_input = input("Do you want to play a game of BlackJack: 'y' or 'n' : ")
    if user_input.lower() == 'y':
        play_game()
    else:
        run_game = False

