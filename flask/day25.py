

from flask import Flask

app=Flask(__name__) # Flask instance named app
@app.route('/')
def hello():
        return 'welcom back sri'
@app.route('/place')
def first():
        return 'Bengeluru'
@app.route('/phone')
def second():
        return '8787485785'

if __name__ == '__main__':
        app.run(debug=True)

