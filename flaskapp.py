from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def name():
    return render_template('index.html')

@app.route('/about')
def aftab():
    name="Aftab"
    return render_template('about.html',name=name)
app.run(debug=True)