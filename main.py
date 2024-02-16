from flask import Flask, request, url_for, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = '12345_yandex'


@app.route('/')
def index():
    param = {
        'title': "подстановка "
    }

    return render_template('base.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
