from flask import Flask, render_template, redirect, request
import os
import redis


app = Flask(__name__)
r = redis.Redis(host=os.environ['REDIS_HOST'],
                port=os.environ['REDIS_PORT'],
                password=os.environ['REDIS_PASSWORD'])


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', brand_name=os.environ['BRAND_NAME'])


@app.route('/post', methods=['GET'])
def post():
    return render_template('post.html')


@ app.route('/get', methods=['GET', 'POST'])
def get():
    if request.method == 'POST':
        return redirect(f"get_value/{request.form['key']}")
    return render_template('get.html')


@ app.route('/get_value/<key>', methods=['GET'])
def get_value(key):
    return r.get(key)


@ app.route('/add_value', methods=['POST'])
def add_value():
    r.set(request.form['key'], request.form['value'])

    return 'Done!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
