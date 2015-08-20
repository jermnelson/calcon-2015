__author__ = "Jeremy Nelson"
__license__ = "GPLv3"

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/abstract")
def abstract():
    
    return render_template('abstract.html')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20159, debug=True) 
