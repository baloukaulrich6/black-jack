"""Le but du blackJack est d'additionner les cartes jus cas ce que la somme soit inferieur ou égale à 21
si les cartes dans notre main totalise deux de pus que 21, alors cela s'appelle un Bust et cela signifie que vous perdez immédiatement.
Et peu importe combien vous avez dépassé 21, tant que c'est plus de 21
le valet, la reine et le roi comptent chacun pour 10 et l'autre carte speciale est l'as il peut compter comme un pour votre total
soit comme un 11. Et selon que si vous avez depasse 21 ou si vous avez moin de 21 vous pouvez décider quelle valeur vous voulez que votre As à resprésenter
chaque fois que le score est égale à celui qui distribut les cartes vous avez fait un Draw
si celui qui distribut les cartes a un score inférieur à 16 ou 17 il doit piocher une autre carte
"""

#
import random

def deal_cards():
    """ Renvois une carte alératoire du jeu"""
    cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculte_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21 :
        """Remove() su^rime la premiere occurence d'une liste existante cependant elle ne supprime pas tout les occurrences de l'élément dans la liste"""
        cards.remove(11)
        cards.append(1)
        return

    return sum(cards)
def comparte(user_score, computer_score):
    if user_score == computer_score :
        return "Draw"
    elif computer_score == 0 :
        return "L'utilisateur a perdu et que l'adversaire a un Blackjack"
    elif user_score == 0 :
        return "win whit a blackJack"
    elif user_score > 21 :
        return "you lose"
    elif computer_score > 21 :
        return  'you win'
    elif user_score > computer_score:
        return  'you win'
    else:
        return  'you lose'
def play_blackjack():
    user_cards = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        """Append() permet d'ajouter les élément a une liste mais conserve la forme d'itérable"""
        user_cards.append(deal_cards())
        computer_card.append(deal_cards())
    while not is_game_over:
        user_score = calculte_score(user_cards)
        computer_score = calculte_score(computer_card)
        print(f"vos carte sont {user_cards}, votre score est de : {user_score}")
        print(f"les cartes de la machine sont {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 :
            is_game_over = True
        else:
            user_piocher = input("vouler vous demander une nouvelle carte : type 'y' type 'n' to pass ")
            if user_piocher == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
         computer_card.append(deal_cards())
         computer_score = calculte_score(computer_card)

    print(f"vos carte sont {user_cards}, votre score est de : {user_score}")
    print(f"les cartes de la machine sont {computer_card}, final score: {computer_score}")
    print(comparte(user_score, computer_score))

while input("voulez vous continuer la partie de blackjack? type 'y' or 'n' : ") == 'y' :
    play_blackjack()
