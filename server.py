from flask import Flask
import random


app = Flask(__name__)

correct_number = str(random.randint(0, 9))
print(correct_number)


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
    return'Guess a number between 0 and 9'


@app.route('/<number>')
def response_pages(number):
    if number == correct_number:
        return "<h1 style='color: green'>That is Correct!!!😎</h1>"
    elif number > correct_number:
        return "<h1 style='color: blue'>Your guess is Too Hiiiigh!😜</h1>"
    else:
        return "<h1 style='color: red'>Your guess is Too Loooow!😣</h1>"


# intro_page('https://media1.giphy.com/media/bmrxNoGqGNMAM/200.webp?cid=ecf05e47kykh4urnjbgsz6olbxb3mc3m6nl5l4v1hesv85j9&rid=200.webp&ct=g')

if __name__ == "__main__":
    app.run(debug=True)
