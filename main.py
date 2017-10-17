from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:1234@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
 

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title, body):
        self.title = title
        self.body = body

#blogs = []

@app.route("/", methods=[ "GET"])
def index():

    return render_template('blog.html', title="Build A Blog!!!!!") 
    
@app.route("/blog", methods=["POST", "GET"])   
def blog():

    
    if request.method == 'POST':
        blog_title = request.form['blog_title']
        body = request.form['body']
        new_blog = Blog(blog_title, body)

        db.session.add(new_blog)

        db.session.commit()
    #last_blog_entry = Blog.query.filter_by(id=10)
    blogs = Blog.query.all()
    
    return render_template('blog.html', title="Build A Blog", blogs=blogs) 
    return redirect('each-blog.html')
    return last_blog_entry 
    

@app.route("/newpost", methods=["POST", "GET"])    
def newpost():
    return render_template('newpost.html')


if __name__ == '__main__':
    app.run()