from flask import Flask

app = Flask(__name__)
app.route("/")
def welcome():
  return "Welcome to the best Flask course. This should be an amazing course"

if name == "__main__":
  app.run(host = '0.0.0.0', port = 5000, debug = True)
