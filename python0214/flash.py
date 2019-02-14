"""
Flask 使用装饰器
from flsk import Flask
创建一个应用
注册路由
启动应用
"""


from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def index():
    return "首页"
@app.route('/wzk')
def wzkinfo():
    return "王增柯"
@app.route("/wzk/pay")
def pay():
    # return "<h1>充值页面</h1>"
    return render_template('pay.html',name="wzk")

app.run()