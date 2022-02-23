from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/shoujo.html')
def shoujo():
     return render_template('shoujo.html')

@app.route('/josei.html')
def josei():
     return render_template('josei.html')

@app.route('/seinin.html')
def seinin():
     return render_template('seinin.html')

@app.route('/shonen.html')
def shonen():
     return render_template('shonen.html')

@app.route('/thx.html')
def thx():
     return render_template('thx.html')

@app.route('/top.html')
def top():
     return render_template('top.html')
     
@app.route('/contact.html')
def contact():
     return render_template('contact.html')
     

if __name__ == "__main__":
    app.run(debug=True)

#this is just a test