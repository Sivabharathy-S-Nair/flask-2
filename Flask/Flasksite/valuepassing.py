from flask import Flask, render_template
run=Flask(__name__)
@run.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username)
run.run(debug=True)
