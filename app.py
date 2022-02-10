from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_world():
    return "<p>Hello, World!</p>"

#これより下には何もかかない
if __name__== '__main__':
  app.run()
