import time
from random import shuffle


def start_message():
    print("Let's play BINGO!")
    time.sleep(5)


def call_number():
    numbers = list(range(1, 91))
    shuffle(numbers)
    for num in numbers:
        print(num)
        time.sleep(5)


if __name__ == "__main__":
    start_message()
    call_number()
