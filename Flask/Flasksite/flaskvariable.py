from flask import Flask
run=Flask(__name__)
@run.route('/profile/<username>')
def demo(username):
    return '<h1> this is for you %s</h1>' % username
run.run(debug=True)
