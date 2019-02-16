from flask import Flask
from flask import render_template 

app = Flask(__name__)

@app.route('/send_message')
def send_message(ID,last_message):
    return "Jack"

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
