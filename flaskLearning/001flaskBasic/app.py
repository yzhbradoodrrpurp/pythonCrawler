# 从flask模块中导入三个函数。
# Flask()是用于处理路由的函数。
# render_template()是用于渲染HTML模版并返回给客户端的函数。
# request是一个对象，它包含了客户端向服务器发送的所有http请求相关的数据，如表单数据、URL 参数、请求头等。
from flask import Flask, render_template, request
# 这是一个能够得到当前时间的模块。
import datetime

# 创建了一个 Flask 应用实例并将其赋值给 app 变量。这个实例是与 Flask 框架交互的主要接口。
# __name__是一个Python自带的特殊变量，之前有提到过。
app = Flask(__name__)


'''
路由的概念：
在Web开发中，路由是指将客户端发来的请求(URL)与服务器上的某个处理函数(通常称为视图函数或控制器)相匹配的过程。
简单来说，路由就是定义 URL 和处理这些 URL 的代码之间的关系。

当一个用户在浏览器中输入一个URL，比如 https://example.com/about，
服务器需要根据这个URL知道该执行哪个处理函数，这个过程就是路由匹配。
开发者通过定义 URL 模式与处理函数的关联，来确保正确的函数被调用。
'''


'''
@app.route()的作用就是定义一个路由。
注意路由一定不能重复，否则不知道访问哪一个处理函数。并且函数名也不能重复。
@app.route('/')定义了访问根目录(/)时候的路由，当用户访问根目录时会执行homepage函数。
函数一定要有一个返回值。
'''
@app.route('/')
def homepage():
    return 'This is the student website of UC Berkeley.'


'''
当用户访问根目录下的任意字符串目录时，会执行log_in_name()函数。
<NAME>会将用户输入的字符串保存为名为NAME的变量，
log_in_name()可以接收这个变量，只用在括号中加上NAME。
'''
@app.route('/login/<name>')
def log_in_name(name):
    present_hour = int(datetime.datetime.now().hour)

    if 6 <= present_hour <= 10:
        return f"Good morning, {name}."
    elif 10 < present_hour <= 13:
        return f"Good noon, {name}."
    elif 13 < present_hour <= 18:
        return f"Good afternoon, {name}."
    elif 18 < present_hour <= 24:
        return f"Good evening, {name}."
    elif 0 < present_hour < 6:
        return f"It's late into the night, {name}. Wish you a good sleep."


'''
<int:identity>的意思是接收一个类型为int的数值，保存到名为identity的变量里。
也就是说当访问整型目录目录下的login目录下的任意整型目录时会执行log_in_identity()函数。
其余用法和上述一致。
'''
@app.route('/login/<int:identity>')
def log_in_identity(identity):
    present_hour = int(datetime.datetime.now().hour)

    if 6 <= present_hour <= 10:
        return f"Good morning, {identity}."
    elif 10 < present_hour <= 13:
        return f"Good noon, {identity}."
    elif 13 < present_hour <= 18:
        return f"Good afternoon, {identity}."
    elif 18 < present_hour <= 24:
        return f"Good evening, {identity}."
    elif 0 < present_hour < 6:
        return f"It's late into the night, {identity}. Wish you a good sleep."


'''
也可以不用<>，这样就不能接收目录名。
'''
@app.route('/ta')
def ta():
    office_hours = "from 9:30 a.m. to 7:30 p.m."
    staffs = ["Chandler", "Joey", "Ross", "Monica", "Phoebe", "Rachel"]
    staffs_majors = {
        "Chandler": "Finance and Economics",
        "Joey": "Acting and Marketing",
        "Ross": "Archaeology and Biology",
        "Monica": "Hygienics and Food Security",
        "Phoebe": "Music and Astrology",
        "Rachel": "Management"
    }

    # 可以通过如下方式向html文件里传入变量，和向函数里传递变量如出一辙。
    return render_template("ta.html", office_hours=office_hours, staffs=staffs, staffs_majors=staffs_majors)


'''
下面介绍的是表单提交。
'''
@app.route('/submission')
def register():
    return render_template("submission.html")


'''
下面介绍接收表单。
接收表单的路径必须和submission中form标签内的action路径一致。
methods接收一个列表，不写的时候默认为只有GET。
'''
@app.route('/results_from_submission', methods=["GET", "POST"])
def results_from_submission():

    if request.method == "POST":
        # 这个语句能够将你提交的内容转化为一个字典，赋值给results。
        results = request.form
        return render_template("results.html", results=results)


if __name__ == '__main__':
    # 运行app变量。
    app.run()
