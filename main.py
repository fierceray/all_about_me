from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/leisure')
def get_leisure():
    return render_template('leisure.html')

@app.route('/resume')
def get_resume():
    return render_template('resume.html')


if __name__ == "__main__":
    app.run(debug=True)