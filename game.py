import random

"""On cree une fonction de distribution de cards de jeu"""
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards
"""Calucule le scocer de chaque distribution de carte"""
def calcule_distribution(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21 :
        """Ici si tu as le As qui est egale a 11 et que la somme de carte est supperieur a 21 alors la valeur du As est changer en 1 au lieu de 11 au depart"""
        cards.remove(11)
        cards.append(1)
        return
    return sum(cards)
""" une fonction qui va comparer les differentes valeur entre """
def compare (user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0 :
        return "win whit a blackjack"
    elif computer_score == 0:
        return "l'utilisateur a perdu et l'acversaire a un blackjack"
    elif user_score > 21:
        return 'you lose'
    elif computer_score > 21:
        return "you win"
    elif user_score > computer_score :
        return "you win"
    else:
        return "you lose"
""" Dans cette partie on va cree une fonction qui demare le jeux"""
def start_game():
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        """Ici l'utilisateur recupere deux lors de la distribution"""
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over:
        user_score = calcule_distribution(user_cards)
        computer_score = calcule_distribution(computer_cards)
        print(f"vos carte sont {user_cards} et votre score est de {user_score}")
        """     Computer card recuper la premier cater parmi les deux car le distributeur afficher juster un carte et l'autre carte est retourner temp que la partier est en cour"""
        print(f"les carte de la machine sont {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_piocher = input("voulez vous une autre carter : 'y' or 'n' ")
            if user_piocher == 'y':
                user_cards.append(deal_cards())
            else:
                game_over = True
        while computer_score != 0 and computer_score < 17 :
            computer_cards.append(deal_cards())
            computer_score = calcule_distribution(computer_cards)
            print(f"vos carte sont {user_cards} et votre score est de {user_score}")
            print(f"les carte de la machine sont {computer_cards}, final {computer_score}")
            print(compare(computer_score,user_score))

while input("vouler vous continuer la partie : 'y' or 'n' ") == 'y':
    start_game()