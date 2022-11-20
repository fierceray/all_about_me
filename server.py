from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/leisure')
def get_contact():
    return render_template('contact.html')

@app.route('/resume')
def get_resume():
    return render_template('resume.html')

@app.route('/cert')
def get_cert():
    return render_template('certificate.html')

@app.route('/project')
def get_project():
    return render_template('project.html')

if __name__ == "__main__":
    app.run(debug=True)
