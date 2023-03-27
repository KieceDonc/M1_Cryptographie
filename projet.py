import random
from unidecode import unidecode

# Create a deck of cards
def create_deck():
    return [i for i in range(1,55)]

# Shuffle the deck
def shuffle_deck(cards):
    random.shuffle(cards)
    return cards

# Move the joker black
def step_one(deck):
    index_joker_black = deck.index(53)
    if index_joker_black != 53:
        deck[index_joker_black], deck[index_joker_black + 1] = deck[index_joker_black + 1], deck[index_joker_black]
    else:
        deck.insert(1, deck.pop())
    return deck

# Move the joker red
def step_two(deck):
    index_joker_red = deck.index(54)
    if index_joker_red == 53:
        deck.insert(2, deck.pop())
    elif index_joker_red == 52:
        deck.insert(1, deck.pop(52))
    else:
        deck.insert(index_joker_red + 2, deck.pop(index_joker_red))
    return deck

# Cut the deck based on the position of the jokers
def step_three(deck):
    index_joker_black = deck.index(53)
    index_joker_red = deck.index(54)
    max_joker_index = max(index_joker_black, index_joker_red)
    min_joker_index = min(index_joker_black, index_joker_red)
    deck = deck[max_joker_index + 1:] + deck[min_joker_index:max_joker_index + 1] + deck[:min_joker_index]
    return deck

# Cut the deck based on the value of the last card
def step_four(deck):
    last_card = deck[-1]
    if last_card == 54:
        last_card = 53
    deck = deck[last_card:-1] + deck[:last_card] + [deck[-1]]
    return deck

# Get the card (m) based on the value of the first card (m = deck[first_card])
def step_five(deck):
    first_card = deck[0]
    if first_card == 54:
        first_card = 53
    m = deck[first_card]
    if m == 54 or m == 53:
        return None
    else:
        if m > 26:
            m -= 26
    return m

# Encrypt the message
def encrypt(deck, message):
    key_code = ""
    while len(key_code) < len(message):
        deck = step_one(deck)
        deck = step_two(deck)
        deck = step_three(deck)
        deck = step_four(deck)
        m = step_five(deck)
        if m != None:
            key_code += chr(m + 64)
    encrypted_text = ""
    for i in range(len(message)):
        c = ord(key_code[i])-64 + ord(message[i])-64
        if c > 26:
            c -= 26
        encrypted_text += chr(c + 64)
    return encrypted_text

# Decrypt the message
def decrypt(deck, encrypted_text):
    key_code = ""
    while len(key_code) < len(encrypted_text):
        deck = step_one(deck)
        deck = step_two(deck)
        deck = step_three(deck)
        deck = step_four(deck)
        m = step_five(deck)
        if m != None:
            key_code += chr(m + 64)
    message = ""
    for i in range(len(encrypted_text)):
        c = (ord(encrypted_text[i])-64) - (ord(key_code[i])-64)
        if c < 1:
            c += 26
        message += chr(c + 64)
    return message

# Remove all non letters characters from the message and convert it to uppercase
def remove_non_letters(message):
    message = message.upper()
    message = [c for c in message if c.isalpha()]
    message = "".join(message)
    message = unidecode(message)
    return message

if __name__ == "__main__":
    # Create a deck of cards and shuffle it    
    deck = create_deck()
    deck = shuffle_deck(deck)

    encrypted_msg = ""
    decrypted_msg = ""

    # Ouvrir le fichier en mode lecture
    with open("fichier.txt", "r") as f:
        # Lire chaque ligne et l'afficher
        for ligne in f:
            # Keep a copy of the original deck
            original_deck = deck.copy()
            
            message = remove_non_letters(ligne)
            print("Message: " + message)
            
            # Encrypt the message
            encrypted = encrypt(deck,message )
            print("Encrypted message: " + encrypted)
            encrypted_msg += encrypted + "\n"

            deck = original_deck.copy()
            # Decrypt the message
            decrypted = decrypt(deck, encrypted)
            print("Decrypted message: " + decrypted)
            print("Does it work ? " + str(message == decrypted))
            decrypted_msg += decrypted + "\n"
    
    f = open("encrypted.txt", "w")
    f.write(encrypted_msg)
    f.close()

    f = open("decrypted.txt", "w")
    f.write(decrypted_msg)
    f.close()