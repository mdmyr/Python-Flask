# revision on the flask app creation.

from flask import Flask
from printthis import printthis


app=Flask(__name__)
print('OUT SID THE MAIN')
printthis(dir(app))



@app.route('/home')
def home():
    return 'You are home'



def helloWorld():
    return 'Hello World'
app.add_url_rule('/','hello',helloWorld)



@app.route('/')
def main():
   # return 'This is a  simple return'
    return "List"
if __name__ == '__main__':
    app.run(debug=True)
