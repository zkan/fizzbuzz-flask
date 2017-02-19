from flask import Flask, render_template, request

from fizzbuzz import fizzbuzz


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = '?'

    if request.method == 'POST':
        number = int(request.form.get('number'))
        result = fizzbuzz(number)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
