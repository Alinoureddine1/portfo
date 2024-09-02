from flask import Flask, render_template, request, redirect, send_file, abort, url_for
import csv
import git

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/resume.pdf')
def pdfviewer():
    return redirect(url_for('static', filename='resume.pdf'))

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
        except:
            return 'Did not save to database', 500
    return 'Something went wrong', 400


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