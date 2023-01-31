from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/geoff/')
def hello_geoff():  # put application's code here
    return 'Hello Geoff!'


@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}<h1>'.format(escape(word.capitalize()))


@app.route('/add/<int:n1>,<int:n2>/')
def add(n1, n2):
    return '<h1>{}<h1>'.format(n1 + n2)




if __name__ == '__main__':
    app.run()
