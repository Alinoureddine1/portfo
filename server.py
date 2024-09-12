from flask import Flask, render_template, request, redirect, send_file, abort, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
import csv
import git
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

@app.route("/")
def home():
    return render_template('index2.html')

@app.route('/resume.pdf')
def pdfviewer():
    return redirect(url_for('static', filename='resume.pdf'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    filename = 'database.csv'
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as database:
        fieldnames = ['name', 'email', 'subject', 'message']
        writer = csv.DictWriter(database, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = {
                'name': request.form.get('name'),
                'email': request.form.get('email'),
                'subject': request.form.get('subject'),
                'message': request.form.get('message')
            }
            
            # Basic form validation
            if not all(data.values()):
                flash('Please fill in all fields.', 'error')
                return redirect(url_for('home'))
            
            write_to_csv(data)
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            app.logger.error(f"Error in form submission: {str(e)}")
            flash('An error occurred while processing your request. Please try again.', 'error')
            return redirect(url_for('home'))

@app.route('/git_update', methods=['POST'])
def git_update():
    try:
        repo = git.Repo('./portfo')
        origin = repo.remotes.origin
        repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
        origin.pull()
        return 'Update successful', 200
    except Exception as e:
        app.logger.error(f"Error during git update: {str(e)}")
        return f'Error during update: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True)