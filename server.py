from flask import Flask, render_template, request, redirect, send_file, abort
import csv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/resume.pdf')
def pdfviewer():
    try:
        return send_file('static/resume.pdf', 
                         download_name='resume.pdf',
                         as_attachment=False,
                         mimetype='application/pdf')
    except FileNotFoundError:
        abort(404, description="Resume not found")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except Exception as e:
            return f'Error: {str(e)}', 500
    else:
        return 'Method not allowed', 405

@app.route('/git_update', methods=['POST'])
def git_update():
    try:
        repo = git.Repo('./portfo')
        origin = repo.remotes.origin
        repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
        origin.pull()
        return 'Update successful', 200
    except Exception as e:
        return f'Error during update: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)