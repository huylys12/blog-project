from flask import Flask, render_template
import requests

posts = requests.get('https://api.npoint.io/f93148253becf328fcf9').json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for post in posts:
        if int(post['id']) == index:
            requested_post = post
            break
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
