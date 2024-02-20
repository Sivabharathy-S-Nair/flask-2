from flask import Flask, render_template
run=Flask(__name__)
@run.route('/books')
def book():
    books=[{'name':'book1','author':'abc','cover':'https://templates.mediamodifier.com/5db698f47c3dc9731647a4e9/fiction-novel-book-cover-template.jpg'},{'name':'book2','author':'abc1','cover':'https://templates.mediamodifier.com/5db698f47c3dc9731647a4e9/fiction-novel-book-cover-template.jpg'},{'name':'book3','author':'abc2','cover':'https://templates.mediamodifier.com/5db698f47c3dc9731647a4e9/fiction-novel-book-cover-template.jpg'}]
    return render_template('objectrendering.html',books=books)
run.run(debug=True)
