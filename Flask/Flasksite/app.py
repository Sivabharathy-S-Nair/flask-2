from flask import Flask
run=Flask(__name__)
@run.route('/')
def demo():
    return '<h1> this is for you </h1>'
run.run(debug=True)
