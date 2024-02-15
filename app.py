from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World'
    pass_list = ["python", "javascript", "reactJS"]
    return render_template('index.html', title="this is a variable", pass_list=pass_list)