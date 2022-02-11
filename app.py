# flaskからflaskの機能を引っ張ってきてねという命令文
import sqlite3,random
from flask import Flask , render_template
from sympy import Add 

app = Flask(__name__)


@app.route("/")
def top():
    return "はろーふらすく！ここはトップページです！"

@app.route("/hello/<name>")
def hello(name):
    return name + "さん、こんにちは"

# 変数の受け渡し
@app.route("/test")
def test():
    py_name = "にんじゃわんこ"
    py_age = 14
    return render_template("index.html",html_name = py_name ,html_age = py_age)

# 変数の受け渡し練習課題
# @app.route("/color")
# def color():
#     py_color = "黄色"
#     return render_template("color.html",html_color = py_color)

# データベースとの接続練習
# @app.route("/color")
# def color():
#     # 「sqlite3でcolor.dbに接続してね」ということをconnに代入
#     conn = sqlite3.connect("color.db")
#     # 「sqlite3でcolor.dbに接続し、操作できるようにしてね」という事をcに代入
#     c = conn.cursor()
#     #「()の中のSQL文を実行してね」
#     c.execute("SELECT name FROM colors WHERE id = 1;")
#     py_color = c.fetchone() 
#     c.close()
#     return render_template("color.html",html_color = py_color)

#データベースから全件取得してランダムで表示
@app.route("/color")
def color():
    # 「sqlite3でcolor.dbに接続してね」ということをconnに代入
    conn = sqlite3.connect("color.db")
    # 「sqlite3でcolor.dbに接続し、操作できるようにしてね」という事をcに代入
    c = conn.cursor()
    #「()の中のSQL文を実行してね」
    c.execute("SELECT * FROM colors;")
    py_color = c.fetchall() 
    py_color =random.choice(py_color)
    print(py_color)
    c.close()
    return render_template("color.html",html_color = py_color)

@app.route("/list")
def task_list():
    conn = sqlite3.connect("flask_test.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks;")
    # データの整形
    task_list = []
    for row in c.fetchall():
        task_list.append({"id":row[0],"task":row[1]})
    print(task_list)
    c.close()
    return render_template("task_list.html")
　　新しいルートを作る名前は/Add
　　関数の戻り値はとしてadd.



     base.htmlと言うファイルを作っておいてください（中はからでもＯＫです）


# メインファイルだった時のみpythonを実行
if __name__ == "__main__":
    # アプリを実行
    app.run(debug=True)