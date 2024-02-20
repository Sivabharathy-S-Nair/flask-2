from flask import Flask, render_template
run=Flask(__name__)
@run.route('/books')
def book():
    books=['book1','book2','book3']
    return render_template('loop.html',books=books)
run.run(debug=True)
