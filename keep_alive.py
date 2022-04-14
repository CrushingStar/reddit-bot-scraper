from flask import Flask
from threading import Thread
# needs a server host and something that can ping the website overnight
app = Flask('')

@app.route('/')
def home():
  return "hi"
def run():
  app.run(host='0.0.0.0', port = 8080)
def keep_alive():
  t = Thread(target=run)
  t.start()
