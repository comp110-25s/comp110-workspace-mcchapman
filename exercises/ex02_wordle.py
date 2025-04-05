"""Wordle"""

__author__ = "730464690"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    N: int = 1
    while N <= 6:
        print(f"=== Turn {N}/6 ===")
        User_guess: str = input_guess(answer_len=len(secret))
        print(emojified(guess=User_guess, answer=secret))
        if User_guess == secret:
            print(f"You won in {N}/6 turns!")
        else:
            N += 1
    else:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, letter: str) -> bool:
    """Check if a word contains a letter"""
    assert len(letter) == 1
    f"len('{letter}') is not 1"
    sequence: int = 0

    while sequence < len(word):
        if word[sequence] == letter:
            sequence += 1
            return True
        else:
            sequence += 1
    return False


def emojified(guess: str, answer: str) -> str:  # the big box for function emojified
    assert len(guess) == len(answer)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    sequence: int = 0
    answer_storage: str = ""  # temp storage box for building your final answer

    while sequence < len(guess):
        if guess
        sequence] == answer[sequence]:
            answer_storage += GREEN_BOX

        elif contains_char(word=answer, letter=guess[sequence]):
            answer_storage += YELLOW_BOX

        else:
            answer_storage += WHITE_BOX
        sequence += 1
    return answer_storage


def input_guess(answer_len: int) -> str:
    while True:
        word: str = input(f"Enter a {answer_len} character word: ")
        if len(word) == answer_len:
            return word
        else:
            print(f"That wasn't {answer_len} chars! Try again: {word}")


if __name__ == "__main__":
    main(secret="codes")
