import turtle
from flask import Flask, render_template

app = Flask(__name__)  

@app.route("/HelloWorld") #URLをきめているもの
def Hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<name>')
def greet(name):
    return name + 'さん、こんばんわ！' 
    #[RETUN　文字列]の形にする必要がある

#from flask import Flask, render_template

# テンプレートを使う
@app.route('/test')
def test():
    return render_template('index.html')
    
#これより下には何もかかない
if __name__== '__main__':
  app.run(debug=True)
