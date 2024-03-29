import random
from tkinter import messagebox
from unidecode import unidecode
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

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

    # Create the main window
    root = tk.Tk()
    root.title("Deck Editor")

    # Create labels and entry
    deck_label = ttk.Label(root, text="Deck:")
    deck_label.grid(row=0, column=0, padx=5, pady=5)

    deck_entry = ttk.Entry(root, width=150)
    deck_entry.grid(row=0, column=1, padx=5, pady=5)
    deck_entry.insert(0, deck)


    def shuffle_deck_entry():
        global deck
        deck_entry.delete(0, tk.END)
        deck = create_deck()
        deck = shuffle_deck(deck)
        deck_entry.insert(0, deck)


    # Create button to randomize deck
    randomize_button = ttk.Button(root, text="Randomize", command=shuffle_deck_entry)
    randomize_button.grid(row=0, column=2, padx=5, pady=5)

    filename = ""
    # Create button to open a file dialog
    def open_file():
        global filename
        filetypes = (("Text files", "*.txt"), ("All files", "*.*"))
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if not filename.endswith(".txt"):
            messagebox.showerror("Error", "Please select a .txt file")
            return
        print(f"Selected file: {filename}")

    open_button = ttk.Button(root, text="Open file", command=open_file)
    open_button.grid(row=1, column=1, padx=5, pady=5)

    

    def encrypt_gui():
        global filename
        global deck
        deck = list(map(int, deck_entry.get().split()))
        if filename == "":
            messagebox.showerror("Error", "Please select a file")
            return
        if sorted(deck) != list(range(1, 55)):
            messagebox.showerror("Error", "The deck is not valid, please make sure the deck is valid, or randomize it")
            return
        
        
        file = open(filename, "r")
        message = [remove_non_letters(line) for line in file.readlines()]
        message = [encrypt(deck, line)+'\n' for line in message]
        file.close()
        print(message)

        file = open(filename, "w")
        file.writelines(message)
        file.close()

        print(f"Encrypted file: {filename}")
        filename = ""

    # Create encrypt and decrypt buttons
    encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_gui)
    encrypt_button.grid(row=2, column=0, padx=5, pady=5)

    # Create encrypt and decrypt buttons
    encrypt_button = ttk.Button(root, text="Encrypt", command=encrypt_gui)
    encrypt_button.grid(row=2, column=0, padx=5, pady=5)

    def decrypt_gui():
        global filename
        global deck
        deck = list(map(int, deck_entry.get().split()))
        if filename == "":
            messagebox.showerror("Error", "Please select a file")
            return
        if sorted(deck) != list(range(1, 55)):
            messagebox.showerror("Error", "The deck is not valid, please make sure the deck is valid, or randomize it")
            return
        file = open(filename, "r")
        message = [remove_non_letters(line) for line in file.readlines()]
        message = [decrypt(deck, line)+'\n' for line in message]
        file.close()
        print(message)

        file = open(filename, "w")
        file.writelines(message)
        file.close()
        
        print(f"Decrypted text: {message}")
        filename = ""

    decrypt_button = ttk.Button(root, text="Decrypt", command=decrypt_gui)
    decrypt_button.grid(row=2, column=2, padx=5, pady=5)

    # Start the main event loop
    root.mainloop()
