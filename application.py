from flask import Flask, render_template, request



application = Flask(__name__)

@application.route('/')
def home():
    return "<p>hello world</p>"   #render_template('index.html')

@application.route('/leisure')
def get_contact():
    return render_template('contact.html')

@application.route('/resume')
def get_resume():
    return render_template('resume.html')

@application.route('/cert')
def get_cert():
    return render_template('certificate.html')

@application.route('/project')
def get_project():
    return render_template('project.html')

if __name__ == "__main__":
    application.run(debug=True)
