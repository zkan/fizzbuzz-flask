from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', result='?')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
