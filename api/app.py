from startup import app
from ms_db import db
from datetime import datetime

@app.route("/test")
def test():

    collection = db["bets"]

    item_1 = {
  "date" : f"{datetime.now()}",
  "outcome" : "false"
}

    collection.insert_one(item_1)

    return "success"

@app.route("/")
def hello_word():
    return "<p>Szia, Lajos!</p>"