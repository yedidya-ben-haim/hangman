# Git: https://github.com/yedidya-ben-haim/hangman.git

import random

LIST_OF_WORD = ["music", "guitar", "piano", "drum", "song",
    "river", "ocean", "beach", "mountain", "forest",]

def word_choose(list_of_word):
    return random.choice(list_of_word)

def count_of_guesses(word) -> int:
    return len(word)-1

def make_hidden_word_list(word) -> list:
    hidden_word_list = []
    for letter in word:
        hidden_word_list.append("_")
    return hidden_word_list

def print_word_status(word_status):
    result_string = "".join(word_status)
    return result_string

def is_valid_input(letter, guessed_letters):
    """
    פונקציה שבודקת האם הקלט תקין לפי הכללים.
    מחזירה True אם הקלט תקין, או הודעת שגיאה אם לא.
    """
    # בדיקה 1: האם הוכנס תו אחד בלבד?
    if len(letter) != 1:
        return "שגיאה: עליך להקיש אות אחת בלבד."

    # בדיקה 2: האם התו הוא אות באנגלית?
    # הפונקציה isalpha בודקת אם מדובר באות, והבדיקה isascii מוודאת שזה אנגלית
    if not letter.isalpha() or not letter.isascii():
        return "שגיאה: הקלט חייב להיות אות באנגלית (A-Z)."

    # בדיקה 3: האם האות כבר נוחשה?
    # אנחנו נמיר הכל ל-lower כדי ש- 'A' ו- 'a' ייחשבו כאותה אות
    if letter.lower() in guessed_letters:
        return f"You already guessed the letter. '{letter}', Try another letter."

    # אם עברנו את כל הבדיקות
    return True

def get_guess(guessed_letters):
    """
    פונקציה שמנהלת את קבלת הקלט מהמשתמש עד שהוא מכניס תו תקין.
    """
    while True:
        user_input = input("Guess the letter: ").strip()  # strip מסיר רווחים מיותרים

        result = is_valid_input(user_input, guessed_letters)

        if result is True:
            return user_input.lower()
        else:
            print(result)  # הדפסת הודעת השגיאה שחזרה מהפונקציה

def check_letter_in_word(word_to_guess, new_guess):
    if new_guess in word_to_guess:
        return True
    else:
        return False

def word_status_update(new_guess, word_status, word_to_guess):
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == new_guess:
            word_status[i] = new_guess
    return word_status

def check_win(word_status):
    if "_" not in word_status:
        return True
    else:
        return False

def ending_message(win_status, word_status):
    if win_status:
        return (f'Well done, you guessed the word'
                f' the word is {print_word_status(word_status)}')
    else:
        return (f'guessing is over,'
                f'game over, '
                f'try again!')



def main():

    word_to_guess = word_choose(LIST_OF_WORD)
    word_status = make_hidden_word_list(word_to_guess)
    max_tries = count_of_guesses(word_to_guess)
    guessed = []
    guess_the_word = False

    print("Welcome to the guessing game! 🎮")

    while max_tries > 0 and guess_the_word == False:

        print(f"You have {max_tries} tries")
        print(f"the word is {print_word_status(word_status)}")
        new_guess = get_guess(guessed)
        guessed.append(new_guess)

        if check_letter_in_word(word_to_guess, new_guess):
            print(f"Nice guess, right!")
            word_status = word_status_update(new_guess, word_status, word_to_guess)
            if check_win(word_status):
                guess_the_word = True

        else:
            print("Wrong guess")
            max_tries -=1

    print(ending_message(guess_the_word, word_status))



















if __name__ == "__main__":
    main()