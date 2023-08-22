from flask import Flask
from flask import request
from flask import redirect
from flask import render_template 
from flask import session
import json
app = Flask(__name__,
            static_folder='public',
            static_url_path='/public/'
            )

#設定 session 密鑰
app.secret_key="asdf"

@app.route("/")
def index():
    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整網址",request.url)
    # print("瀏覽器和作業系統",request.headers.get("user_agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))
    return render_template("index.html")

@app.route("/Q-ALL",methods = ["POST"] )
def getdata():
    user = request.form['user']
    session["user"] = user
    print(session["user"])

    return render_template("Q-ALL.html")

@app.route("/end-ALL",methods = ["POST"] )
def endALL():
    Q1_ans = request.form['Q1']
    Q2_ans = request.form['Q2']
    Q3_ans = request.form['Q3']
    Q4_ans = request.form['Q4']
    Q5_ans = request.form['Q5']
    Q6_ans = request.form['Q6']
    session["Q1"] = Q1_ans
    session["Q2"] = Q2_ans
    session["Q3"] = Q3_ans
    session["Q4"] = Q4_ans
    session["Q5"] = Q5_ans
    session["Q6"] = Q6_ans
    all_ans = [session[f'Q{i}']for i in range(1,7)]
    user = session["user"]

    return render_template("end.html",data = all_ans, usr = session["user"] )


@app.route("/Q1",methods = ["POST"])
def Q1():
    user = request.form['user']
    session["user"] = user
    print(session["user"])
    #接收 GET 方法的 Query String
    # Q1_ans = request.args.get('Q1','')
    # print(Q1_ans)
    return render_template("Q1.html")

@app.route("/Q2",methods = ["POST"] )
def Q2():
    Q1_ans = request.form['Q1']
    session["Q1"] = Q1_ans
    print(session["Q1"])
    return render_template("Q2.html")

@app.route("/Q3",methods = ["POST"] )
def Q3():
    Q2_ans = request.form['Q2']
    session["Q2"] = Q2_ans
    print(session["Q2"])
    return render_template("Q3.html")

@app.route("/Q4",methods = ["POST"] )
def Q4():
    Q3_ans = request.form['Q3']
    session["Q3"] = Q3_ans
    print(session["Q3"])
    return render_template("Q4.html")

@app.route("/Q5",methods = ["POST"] )
def Q5():
    Q4_ans = request.form['Q4']
    session["Q4"] = Q4_ans
    print(session["Q4"])
    return render_template("Q5.html")

@app.route("/Q6",methods = ["POST"] )
def Q6():
    Q5_ans = request.form['Q5']
    session["Q5"] = Q5_ans
    print(session["Q5"])
    return render_template("Q6.html")

@app.route("/end",methods = ["POST"] )
def end():
    Q6_ans = request.form['Q6']
    session["Q6"] = Q6_ans
    print(session["Q6"])
    all_ans = [session[f'Q{i}']for i in range(1,7)]
    user = session["user"]
    return render_template("end.html",data = all_ans, usr = session["user"] )


app.run(port=5001)