"""
-------------------------------------------------
    File Name:     api.py
    Description:   API模块，运行后打开浏览器，访问
                   http://127.0.0.1:5000/进入主页。
                   访问 http://127.0.0.1:5000/get 
                   从代理池中获取一个代理。 
                   访问 http://127.0.0.1:5000/count
                   获取代理池中可用代理的总数。
    Author:        Liu
    Date:          2016/12/9
-------------------------------------------------
"""
from flask import Flask, g

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    """Opens a new redis connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'redis_client'):
        g.redis_client = RedisClient()
    return g.redis_client


@app.route('/')
def index():
    return '<h1>Welcome</h1>'


@app.route('/get')
def get_proxy():
    """Get a proxy
    """
    conn = get_conn()
    return conn.pop()


@app.route('/count')
def get_counts():
    """Get the count of proxies
    """
    conn = get_conn()
    return str(conn.queue_len)

if __name__ == '__main__':
    app.run()
