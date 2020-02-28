# revision on the flask app creation.

from flask import Flask
from printthis import printthis


app=Flask(__name__)
printthis(dir(app))

@app.route('/')


def main():
    return 'This is a  simple return'
    prinththis(print(dir(app)))

if __name__ == '__main__':
    app.run()
