from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_view():
  heading_1 = "Hello,World"
  return render_template('hello.html', title='flask now!', heading_1=heading_1)


if __name__ == '__main__':
  app.run()
