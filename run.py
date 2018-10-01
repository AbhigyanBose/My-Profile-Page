from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    'This is the landing page of the Website'
    return '<h1>Initial Commit</h1>'

if __name__=='__main__':
    app.run(debug=True)
