from flask import Flask
import random


app = Flask(__name__)

correct_number = str(random.randint(0, 9))
print(correct_number)

guessed_number = -1


def make_h1(function):
    def wrapper(*args):
        return f'<h1>{function()}</h1>'
    return wrapper


def add_gif(function):
    def wrapper():
        return f'{function()}<img src="https://media1.giphy.com/media/bmrxNoGqGNMAM/200.webp?cid=ecf05e47kykh4urnjbgsz6olbxb3mc3m6nl5l4v1hesv85j9&rid=200.webp&ct=g">'
    return wrapper


@app.route('/')
@add_gif
@make_h1
def intro_page():
    global guessed_number
    guessed_number = -1
    return'Guess a number between 0 and 9'


def add_gif_b(function):
    def wrapper():
        function_result = function()
        if guessed_number == correct_number:
            src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
        elif guessed_number > correct_number:
            src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
        else:
            src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
        return f"{function_result}<img src={src}>"
    return wrapper


def make_h1_b(function):
    def wrapper():
        func_result = function()
        if guessed_number == correct_number:
            color = 'green'
        elif guessed_number > correct_number:
            color = 'blue'
        else:
            color = 'red'
        return f"<h1 style='color: {color}'>{func_result}</h1>"
    return wrapper


@add_gif_b
@make_h1_b
def get_message():
    if guessed_number == correct_number:
        return "That is Correct!!!😎"
    elif guessed_number > correct_number:
        return "Your guess is Too Hiiiigh!😜"
    else:
        return "Your guess is Too Loooow!😣"


@app.route('/<number>')
def response_pages(number):
    global guessed_number
    guessed_number = number
    return get_message()


if __name__ == "__main__":
    app.run(debug=True)
