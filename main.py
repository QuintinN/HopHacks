from flask import Flask
from flask import render_template
from flask import request
import sqlite3
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
database_name = "database.db" 

@app.route('/send_message')
def send_message(ID,last_message):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO messages (ID,message,time) VALUES (?, ?, ?) ",
              (ID,last_message,datetime.now()))
    conn.commit()
    conn.close()

    return "Jack"

@app.route('/')
def index():
	return render_template('index.html')    

@app.route("/delete_all")
def delete_all(ID):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("DELETE from messages where ID=?",(ID,))
    conn.commit()
    conn.close()

@app.route("/sms", methods = ['GET', 'POST'])
def sms_reply():
    message = request.values.get("Body", None)
    resp = MessagingResponse()
    resp.message(message)
    return str(resp)

def select_all(ID):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * from messages where ID=?",(ID,))

    rows = c.fetchall()
    for row in rows:
        print(row)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run(debug=True)
