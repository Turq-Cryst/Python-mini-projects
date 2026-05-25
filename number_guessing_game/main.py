from typing import Final
import random

LOWER_LIMIT: Final[int] = 0
HIGHER_LIMIT: Final[int] = 100

random_num: int = random.randint(LOWER_LIMIT, HIGHER_LIMIT)
attempts: int = 0

def bot_message(msg: str) -> None:
    print(f'Bot: {msg}')

bot_message('WELCOME TO THE NUMBER GUESSING GAME')
bot_message(f'GUESS A NUMBER BETWEEN {LOWER_LIMIT} & {HIGHER_LIMIT}')

while True:
    try:
        guess: int = int(input("You: "))
    except (ValueError, TypeError) as e:
        bot_message(f'{e}, please use numbers only in the form of digits')
        continue
    except Exception:
        bot_message('Unexpected error. Try again with numbers only in the form of digits')

    if guess > random_num:
        attempts += 1
        bot_message('Guess too high.')
    elif guess < random_num:
        attempts += 1
        bot_message('Guess too low')
    else:
        attempts += 1
        bot_message('Correct. You WIN!')
        break

bot_message(f'Score (no. of attempts): {attempts}')
