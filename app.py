import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/helloworld")  # URLを決めているもの
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/user/<name>')  # URLの中に<>を使うと変数としてアプリで受け取れる
def greet(name): # 変数として受け取る者はメソッド引数に書く
    return name + 'さん、こんばんは！'
    # 「return 文字列」の形にする必要がある


# テンプレートを使う
@app.route('/test')
def test():
    return render_template("index.html")
    # 上の実行結果と下の実行結果は同じ
    # return '<!DOCTYPE html> <html lang="ja"> <head> <meta charset="UTF-8"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Flaskテスト</title> </head> <body> <h1>Flask、こんばんは！</h1> <p>テンプレートを使ってます！</p> </body> </html>'


# テンプレートに変数を渡す
@app.route('/test_val')
def test_val():
    py_name = 'にんじゃわんこ' # 変数
    py_age = 20 # 変数
    return render_template('index_val.html', name=py_name, age=py_age)


@app.route('/list')
def task_list():
    # 「sqlite3でflask_test.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("flask_test.db")
    # 「sqlite3で接続したものを操作してね」ということをcに代入
    c = conn.cursor()
    # ()内のSQL文を実行してね
    c.execute("SELECT * FROM tasks;")
    # 検索結果のデータを取得
    task_list = []
    #print('fetchall()の実行結果',c.fetchall())
    for row in c.fetchall():
        task_list.append({"id":row[0],"task":row[1]})
    # データベースと接続解除
    c.close()
    return render_template("task_list.html",task_list=task_list)

