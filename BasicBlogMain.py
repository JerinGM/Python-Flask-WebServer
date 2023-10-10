from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("basic.html")

@app.route('/blog')
def blog():
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("BasicBlogIndex.html", posts=all_posts)


@app.route('/blog/<num>')
def get_blog(num):
    nnumb = None
    title = {}
    body = {}
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    num = int(num)
    for i in range(3):
        if all_posts[i]['id'] == 1 and num == 1:
            nnumb = 1
            print(nnumb)
            title = all_posts[i]['title']
            body = all_posts[i]['body']
            print(title)
            print(body)
            return render_template("postIndex.html", number=nnumb, title=title, body=body)
        elif all_posts[i]['id'] == 2 and num == 2:
            nnumb = 2
            title = all_posts[i]['title']
            body = all_posts[i]['body']
            return render_template("postIndex.html", number=nnumb, title=title, body=body)
        elif all_posts[i]['id'] == 3 and num == 3:
            nnumb = 3
            title = all_posts[i]['title']
            body = all_posts[i]['body']
            return render_template("postIndex.html", number=nnumb, title=title, body=body)




if __name__ == "__main__":
    app.run(debug=True)
