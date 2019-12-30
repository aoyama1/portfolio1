from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',\
        title="ROPE'S sample",\
            message="お名前は？")

@app.route('/', methods=['POST'])
def form():
    field =request.form['field']
    return render_template('index.html', \
        title="ROPE'S sample",\
            message="こんちには、%sさん!" % field)


if __name__ == '__main__':
    app.run()

