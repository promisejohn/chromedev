# coding=utf8

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('test.html')

@app.route('/upcook', methods=['POST'])
def upcookie():
    print(request.args.get('cook',''))
    return 'success'

if __name__ == '__main__':
    app.run('0.0.0.0',80)
