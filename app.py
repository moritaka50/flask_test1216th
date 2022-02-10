from flask import Flask

app = Flask(__name__)  

@app.route("/HelloWorld") #URLをきめているもの
def Hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<name>')
def greet(name):
    return name + 'さん、こんばんわ！' 

#これより下には何もかかない
if __name__== '__main__':
  app.run()
