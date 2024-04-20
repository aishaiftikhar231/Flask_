import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
   random_number=random.randint(1,100)
   return render_tempelate("i.html,num=rand_number")
@app.route('/guess/<name>')
def guess(name):
 if __name__ == '__main__':
    app.run(debug=True)
