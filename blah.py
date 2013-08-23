from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('default.html')

if __name__ == '__main__':
    app.run(debug=True)