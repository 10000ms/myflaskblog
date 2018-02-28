#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Victor Lai'

'''
flask project entrance.
'''

# 导入flask扩展
from flask import Flask


app = Flask(__name__)


# 创建Flask应用程序实例
# 需要传入__name__，作用是确定资源所在的路径
app = Flask(__name__)

# 定义路由及视图函数
# Flask中定义路由是由专门的路由装饰器实现的
@app.route("/")
def index():
    return "Hello World!"


@app.route("/user")
def index():
    '''
    用户信息
    '''
    pass


@app.route("/admin")
def index():
    '''
    后台管理信息
    '''
    pass


@app.route("/article")
def index():
    '''
    博文
    '''
    pass


# 启动程序
if __name__ == '__main__':
    app.run()