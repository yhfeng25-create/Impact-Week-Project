from flask import Flask

# 创建应用实例
app = Flask(__name__)

# 首页路由
@app.route('/')
def home():
    return "✅ 我的第一个动态网站运行成功！Impact Week Project"

# 第二个页面
@app.route('/about')
def about():
    return "👋 这是关于页面"

# 运行程序
if __name__ == '__main__':
    app.run(debug=True)