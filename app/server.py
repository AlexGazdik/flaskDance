from flask import Flask
from flask import render_template
from covidpull import dataPull
from qtod import getQuote

app = Flask(__name__)
# quot = getQuote()


@app.route('/')
@app.route('/index')
def index():
    name = "Covid Data"
    users = ['Aaron', 'John', 'Corey', "Jason"]
    return render_template('index.html', title='Welcome', username = name,
    fl1 = dataPull(10)[0], fl2 = dataPull(10)[1], co1 = dataPull(6)[0], co2 = dataPull(6)[1], members = users)
    
@app.route('/zen')
def zen():
    return render_template('zen.html', title="welcome")


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=81, debug=True)