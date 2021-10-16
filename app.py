from flask import Flask, render_template, redirect, url_for, request, flash
import os
import redis
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)
r = redis.Redis(host=os.environ['REDIS_HOST'],
                port=os.environ['REDIS_PORT'],
                password='')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/post', methods=['GET'])
def post():
    return render_template('post.html')


@app.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        return redirect(f"get_value/{request.form['key']}")
    return render_template('get.html')


@app.route('/get_value/<key>', methods=['GET'])
def get_value(key):
    flash(f'Key:{key} Value:{r.get(key)}')
    return render_template('index.html')


@app.route('/add_value', methods=['POST'])
def add_value():
    r.set(request.form['key'], request.form['value'])
    flash(f"The Pair {request.form['key']}:{request.form['value']} has been stored successfully!")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
