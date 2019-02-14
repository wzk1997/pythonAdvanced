from flask import Flask,render_template

app=Flask(__name__)

@app.route('/index')
def index():
    return "<h1>这是第一个页面</h1>"
@app.route("/HT")
def redis():
    return render_template('pay.html')
app.run()