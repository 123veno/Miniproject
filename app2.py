from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('Navbar.html')

if__name__=   '__main__':
    app.run(debug=True)
    
