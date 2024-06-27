# Import tkinter and necessary modules
import tkinter as tk
from tkinter import ttk
from src.helpers import set_background, clear_widgets
import os
import random
import string


# Initialize Coin-Score
coin = 0


# Load file from given file_path or return an empty list if it doesn't exist
def load_file(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words


# Load content of file into a text widget
def load_file_to_text_widget(file_path, text_widget):
    words = load_file(file_path)
    text = "\n".join(words)

    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, text)
    text_widget.config(state=tk.DISABLED)


# Load two random words from a list of words
def load_random_words(words):
    return random.sample(words, 2)


# Check if a sentence contains all target words
def check_sentence(sentence, target_words):
    words = sentence.lower().split()
    for word in target_words:
        if word.lower() not in [w.strip(string.punctuation) for w in words]:
            return False
    return True


# Process user input sentence, update coin score and display feedback
def process_sentence(event):
    global coin
    sentence = entry.get()
    if check_sentence(sentence, target_words):
        coin += 1
        result_label.config(text="Well done, word pirate! +1 coin")
        coin_label.config(text=str(coin))
        display_new_words()
    else:
        result_label.config(text="Poor job! Try again.")


# Display two new random words
def display_new_words():
    global target_words
    target_words = load_random_words(words)
    word1_label.config(text=target_words[0])
    word2_label.config(text=target_words[1])
    entry.delete(0, tk.END)


# Add a new word to the file and update display
def add_word_to_file(event):
    new_word = entry.get().strip().lower()
    if new_word:
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(new_word + '\n')
        else:
            with open(file_path, 'r') as file:
                words = file.read().splitlines()

            words.append(new_word)
            words = sorted(set(words))

            with open(file_path, 'w') as file:
                for word in words:
                    file.write(word + '\n')

        entry.delete(0, tk.END)
        result_label.config(text=f"'{new_word}' added.")


# Create wordlist page with text widget displaying file content
def create_page_wordlist(root):
    clear_widgets(root)
    set_background(root, image_file_path3)

    back_button = tk.Button(root, text="<<", font=("Baloo", 14, "bold"), bg="white", fg="black",
                            command=lambda: create_homepage(root, image_file_path1="image/homepage.jpg"), bd=0)
    back_button.place(relx=0.775, rely=0.9)

    exit_button = tk.Button(text="X X", font=("Baloo", 10, "bold"), bg="white", fg="black", command=root.destroy, bd=0)
    exit_button.place(relx=0.08, rely=0.89)

    frame = ttk.Frame(root)
    frame.place(relwidth=0.8, relheight=0.45, relx=0.1, rely=0.35)

    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, state=tk.DISABLED, bg="white", fg="black", font=("Baloo", 14))
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=text_widget.yview)
    load_file_to_text_widget(file_path, text_widget)

    global coin_label
    coin_label = tk.Label(root, text=str(coin), font=("Baloo", 20, "bold"), bg="white", fg="black")
    coin_label.place(relx=0.85, rely=0.07)


# Create add words page with entry widget and feedback labels
def create_page_add_words(root):
    clear_widgets(root)
    set_background(root, image_file_path4)

    back_button = tk.Button(root, text="<<", font=("Baloo", 14, "bold"), bg="white", fg="black",
                            command=lambda: create_homepage(root, image_file_path1="image/homepage.jpg"), bd=0)
    back_button.place(relx=0.775, rely=0.9)

    exit_button = tk.Button(text="X X", font=("Baloo", 10, "bold"), bg="white", fg="black", command=root.destroy, bd=0)
    exit_button.place(relx=0.08, rely=0.89)

    global entry
    entry = tk.Entry(root, width=30, font=("Baloo", 14), bg="white", fg="black")
    entry.place(relx=0.5, rely=0.5, anchor='center')

    tip_label = tk.Label(root, text="Type your word and press enter:", font=("Baloo", 14), bg="white", fg="black")
    tip_label.place(relx=0.5, rely=0.45, anchor='center')

    global result_label
    result_label = tk.Label(root, text="", font=("Baloo", 14), bg="white", fg="black")
    result_label.place(relx=0.5, rely=0.55, anchor='center')

    entry.bind("<Return>", add_word_to_file)

    global coin_label
    coin_label = tk.Label(root, text=str(coin), font=("Baloo", 20, "bold"), bg="white", fg="black")
    coin_label.place(relx=0.85, rely=0.07)


# Create learning journey page with labels and entry for sentences
def create_page_learning_journey(root):
    clear_widgets(root)
    set_background(root, image_file_path2)

    back_button = tk.Button(root, text="<<", font=("Baloo", 14, "bold"), bg="white", fg="black",
                            command=lambda: create_homepage(root, image_file_path1="image/homepage.jpg"), bd=0)
    back_button.place(relx=0.775, rely=0.9)

    exit_button = tk.Button(text="X X", font=("Baloo", 10, "bold"), bg="white", fg="black", command=root.destroy, bd=0)
    exit_button.place(relx=0.08, rely=0.89)

    global coin_label
    coin_label = tk.Label(root, text=str(coin), font=("Baloo", 20, "bold"), bg="white", fg="black")
    coin_label.place(relx=0.85, rely=0.07)

    global word1_label
    word1_label = tk.Label(root, text="", font=("Baloo", 16), bg="white", fg="black")
    word1_label.place(relx=0.1, rely=0.46, anchor='w')

    global word2_label
    word2_label = tk.Label(root, text="", font=("Baloo", 16), bg="white", fg="black")
    word2_label.place(relx=0.9, rely=0.46, anchor='e')

    global entry
    entry = tk.Entry(root, width=360-20, font=("Baloo", 14), bg="white", fg="black")
    entry.place(x=10, y=screen_height * 0.6, width=360-20)
    entry.bind("<Return>", process_sentence)

    tip_label = tk.Label(root, text="Enter your sentence and press enter", font=("Baloo", 14), bg="white", fg="black")
    tip_label.place(relx=0.5, rely=0.55, anchor='center')

    global result_label
    result_label = tk.Label(root, text="", font=("Baloo", 14), bg="white", fg="black")
    result_label.place(relx=0.5, rely=0.7, anchor='center')

    display_new_words()


# Create homepage and score display
def create_homepage(root, image_file_path1):
    set_background(root, image_file_path1)

    newpage_button = tk.Button(root, text="AHOY! LEARNING\n JOURNEY AHEAD", font=("Baloo", 14, "bold"), bg="white", fg="black",
                               command=lambda: create_page_learning_journey(root), bd=0)
    newpage_button.place(relx=0.7, rely=0.3, anchor='center')

    newpage_button2 = tk.Button(root, text="SPOTTING ALL THE\n PRECIOUS WORDS", font=("Baloo", 14, "bold"), bg="white", fg="black",
                               command=lambda: create_page_wordlist(root), bd=0)
    newpage_button2.place(relx=0.7, rely=0.525, anchor='center')

    newpage_button3 = tk.Button(root, text="ADD WORDS TO\n TREASURE CHEST", font=("Baloo", 14, "bold"), bg="white", fg="black",
                               command=lambda: create_page_add_words(root), bd=0)
    newpage_button3.place(relx=0.7, rely=0.75, anchor='center')

    global coin_label
    coin_label = tk.Label(root, text=str(coin), font=("Baloo", 20, "bold"), bg="white", fg="black")
    coin_label.place(relx=0.85, rely=0.07)

    exit_button = tk.Button(text="X X", font=("Baloo", 10, "bold"), bg="white", fg="black", command=root.destroy, bd=0)
    exit_button.place(relx=0.08, rely=0.89)


# create gui for Wortschatzl
root = tk.Tk()
root.title("Wortschatzl")

screen_width = 360
screen_height = 800
root.geometry(f'{screen_width}x{screen_height}+550+0')

# define paths
file_path = "worte.txt"
image_file_path1 = "image/homepage.jpg"
image_file_path2 = "image/page_learning_journey.jpg"
image_file_path3 = "image/page_wordlist.jpg"
image_file_path4 = "image/page_add_words.jpg"

words = load_file(file_path)
target_words = []

create_homepage(root, image_file_path1)

root.mainloop()
