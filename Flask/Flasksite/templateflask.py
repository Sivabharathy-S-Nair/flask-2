from flask import Flask, render_template
run=Flask(__name__)
@run.route('/')
def index():
    return render_template('index.html')
run.run(debug=True)
