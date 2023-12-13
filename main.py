from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  # Example blog post data
  posts = [
    {
      "title": "My First Post",
      "date": "2023-12-13",
      "content": "This is my first blog post on App Engine!",
    },
    # Add more posts here...
  ]
  return render_template("index.html", posts=posts)

if __name__ == "__main__":
  app.run(debug=True)
