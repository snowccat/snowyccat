from flask import Flask,render_template,request

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "<h1>資管二A 411146318 劉增泰</h1><br>"
    X += "<a href=/about>增泰個人網頁<a><br>"
    X += "<a href=/today>興趣何倫碼測驗結果<a><br>"
    X += "<a href=/mis>相關工作<a><br>"
    X += "<a href=/welcome>個人履歷<a><br>"
    return X

@app.route("/about")
def about():
    return render_template("about.html")    

@app.route("/mis")
def course():
    return render_template("account.html") 

@app.route("/today")
def today():
    return render_template("today.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run()
