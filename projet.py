import random

def main():
    cards = list(range(1, 55))
    print(cards)
    #genKeyStepOne(cards)
    #genKeyStepTwo(cards)
    genKeyStepThree(cards)


# Applique la première opération pour obtenir la clée à partir du flux
# Recule le joker d'une position dans le jeu carte
def genKeyStepOne(cards):
    printBeginningStep("1",cards)
    # On parcourt notre jeu de carte
    for index in range(len(cards)):
        currentCard = cards[index]
        
        # Si la carte est un joker (la valeur contenu est 53 ou 54)
        if  currentCard == 53 or currentCard == 54 :
            # Si le joker n'est pas au début
            if index != 0 :
                # On recule le joker d'une position
                # TODO Revoir les consignes pour bien comprendre le swap & l'ordre des cartes
                cardToSwap = cards[index - 1]
                cards[index - 1] = currentCard
                cards[index] = cardToSwap
                return cards
                
            # Si le joker est au début
            else : 
                # On met le joker à la position 2 
                # TODO Revoir les consignes pour bien comprendre le swap & l'ordre des cartes
                cardToSwap = cards[1]
                cards[1] = currentCard
                cards[0] = cardToSwap
                return cards

# Applique la deuxième opération pour obtenir la clée à partir du flux
# Recule le joker rouge de deux positions dans le jeu carte
def genKeyStepTwo(cards):
    printBeginningStep("2",cards)
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
                # On met le joker à la troisième position
                # TODO Revoir les consignes pour bien comprendre le swap & l'ordre des cartes
                cardToSwap = cards[2]
                cards[2] = currentCard
                cards[0] = cardToSwap
                return cards

            # Si le joker est à la deuxième position
            else:
                # On met le joker à la deuxième position
                # TODO Revoir les consignes pour bien comprendre le swap & l'ordre des cartes
                cardToSwap = cards[1]
                cards[1] = currentCard
                cards[1] = cardToSwap
                return cards

# Applique la troisième opération pour obtenir la clée à partir du flux
# On recherche d'abord la position des deux jokers
# Pour chaque joker, on intervertit le paquet en dessous du joker par celui du dessus
def genKeyStepThree(cards):
    printBeginningStep("3",cards)
    
    # Détermine la position des jokers dans le jeu de carte
    firstJokeyIndex = findCardIndex(cards, 53)
    secondJokeyIndex = findCardIndex(cards, 54)
    
    # Détermine la position des jokers 
    # Le premier index décrit l'index du premier joker dans le jeu de carte
    # Le second index décrit l'index du second joker après avoir intervertit le paquet
    firstIndex = -1
    secondIndex = -1
    if firstJokeyIndex < secondJokeyIndex :
        firstIndex = firstJokeyIndex
        secondIndex = secondJokeyIndex - firstIndex - 1
    else:
        firstIndex = secondJokeyIndex
        secondIndex = firstJokeyIndex - firstIndex - 1

    cards = invertByIndex(cards, firstIndex)
    print(cards)
    cards = invertByIndex(cards, secondIndex)
    print(cards)

# Génère une clée aléatoire d'une longeur donnée en paramètre
def genKey(length):
    # On déclare un tableau vide de longeur donné en paramètre
    key = [0] * length
    
    for index in range(len(key)):
        # On affecte une valeur aléatoire de l'alphabet à la clée (1 = A, ...)
        key[index] = random.randint(1, 27)
    return key

# Intervertit le jeu de cartes selon l'index d'une carte
def invertByIndex(cards, index):
    if index == 0:
        cards = [*cards[index + 1:], cards[index]]
    elif index == 53:
        cards = [cards[index], *cards[0:index-1]]
    else :
        cards = [*cards[index + 1:], cards[index], *cards[0:index-1]]

    return cards

# Recherche l'index d'une carte dans le jeu
def findCardIndex(cards, cardValue):
    # Recherche la position d'un joker 
        founded = False
        index = -1
        while not founded:
            index += 1
            currentCard = cards[index]
            founded = currentCard == cardValue or index > 53

        if index > 53 :
            print("Erreur pour la recherche de "+str(cardValue)+"dans ")
            print(cards)
            return -1 
        else :
            return index

# Affiche le début d'uneopération pour obtenir la clée à partir du flux et le jeu de cartes
def printBeginningStep(stepIndex, cards):
    separator = "-------------------------------------------------------------------------"
    print(separator+"\n")
    print("Début partie "+stepIndex+":\n")
    print(cards)
    print("")
    print(separator)
    
if __name__ == "__main__":
    main()
