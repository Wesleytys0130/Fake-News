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
    # user = request.form['user']
    # session["user"] = user
    # print(session["user"])

    return render_template("Q-ALL.html")

@app.route("/end-ALL",methods = ["POST"] )
def endALL():
    all_ans = [request.form[f"Q{i}"] for i in range(1,7)]
    correct = ["C", "B", "B", "B", "C", "A"]
    # user = session["user"]

    Logo = 0
    Etho = 0
    Patho = 0
    for cor, ans, count in zip(correct, all_ans, range(1,7)):
        if count == 1 or count == 2:
            if cor != ans:
                Logo += 1
            else:
                continue
        elif count == 3 or count == 4:
            if cor != ans:
                Etho += 1
            else:
                continue
        elif count == 5 or count == 6:
            if cor != ans:
                Patho += 1
            else:
                continue

    if Logo == 0 and Etho == 0 and Patho == 0:
        session['music_type'] = 'Blues, Jazz, Soft Rock'
    elif Logo == 0:
        session['music_type'] = 'Country Music, Classical Music, Folk Music'
    elif Etho == 0:
        session['music_type'] = 'Heavy Metal Music'
    elif Patho == 0:
        session['music_type'] = 'Buddhist Scriptures, Singing Bowl Sounds'
    else:
        session['music_type'] = 'Ballad Songs, Pop Songs'
    print(session['music_type'])

    return render_template("end.html")

app.run(port=5001)