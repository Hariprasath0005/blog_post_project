from flask import Flask, render_template
import requests
app = Flask(__name__)

posts = requests.get(" https://api.npoint.io/52ea7b94fe44b03c6197").json()

@app.route("/")
def home():
    return render_template("index.html", all_posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    req_post = None
    for i in posts:
        if i["id"] == index:
            req_post = i
    return render_template("post.html",post = req_post)



if __name__ =='__main__':  
    app.run(debug = True,port=80, host='0.0.0.0')