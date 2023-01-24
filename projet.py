import random


def main():
    cards = list(range(1, 55))
    print(cards)
    print(genKeyStepOne(cards))
    genKeyStepOne(cards)
    print(cards)
    print(genKey(10))

# Applique la première opération pour obtenir la clée à partir du flux
# Recule le joker d'une position dans le jeu carte
def genKeyStepOne(cards):
    # On parcourt notre jeu de carte
    for index in range(len(cards)):
        currentCard = cards[index]
        
        # Si la carte est un joker (la valeur contenu est 53 ou 54)
        if  currentCard == 53 or currentCard == 54 :
            # Si le joker n'est pas au début
            if index != 0 :
                # On recule le joker d'une position
                cardToSwap = cards[index - 1]
                cards[index - 1] = currentCard
                cards[index] = cardToSwap
                return cards
                
            # Si le joker est au début
            else : 
                # On met le joker à la position 2 
                cardToSwap = cards[1]
                cards[1] = currentCard
                cards[0] = cardToSwap
                return cards

# Applique la deuxième opération pour obtenir la clée à partir du flux
# Recule le joker rouge de deux positions dans le jeu carte
def genKeyStepTwo(cards):
    # On parcourt notre jeu de carte
    for index in range(len(cards)):
        currentCard = cards[index]
        
        # Si la carte est un joker (la valeur contenu est 54)
        if  currentCard == 54 :
            # Si le joker n'est pas au début
            if index != 0 and index != 1 :
                # On recule le joker de deux positions
                cardToSwap = cards[index - 2]
                cards[index - 2] = currentCard
                cards[index] = cardToSwap
                return cards
                
            # Si le joker est au début
            elif index == 0 : 
                # On met le joker à la position 2 
                cardToSwap = cards[2]
                cards[2] = currentCard
                cards[0] = cardToSwap
                return cards

            # Si le joker est à la deuxième position
            else:
                # On met le joker à la position 3 
                cardToSwap = cards[3]
                cards[3] = currentCard
                cards[1] = cardToSwap
                return cards

# Génère une clée aléatoire d'une longeur donnée en paramètre
def genKey(length):
    # On déclare un tableau vide de longeur donné en paramètre
    key = [0] * length
    
    for index in range(len(key)):
        # On affecte une valeur aléatoire de l'alphabet à la clée (1 = A, ...)
        key[index] = random.randint(1, 27)
    return key


if __name__ == "__main__":
    main()
