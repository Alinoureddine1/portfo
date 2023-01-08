from flask import Flask, render_template, request, redirect
from flask import send_file, current_app as app
import csv
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('index.html')





# @app.route('/resume')
# def show_static_pdf():
#     with open('templates/resume.pdf') as static_file:
#         return send_file(static_file, attachment_filename='resume.pdf')

@app.route('/resume.pdf') 
def pdfviewer():
    return redirect("/static/resume.pdf") #the pdf itself



@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt',mode ='a') as database:
        email = data["email"]
        subject = data["subject"]
        message=data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode ='a',newline ='') as database2:
        email = data["email"]
        subject = data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database2, delimiter=',',  quotechar='"', quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'