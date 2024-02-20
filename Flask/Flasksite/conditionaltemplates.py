from flask import Flask, render_template
run=Flask(__name__)
@run.route('/profile/<username>')
def profile(username):
    return render_template('condition.html',username=username,isActive=False)
run.run(debug=True)
