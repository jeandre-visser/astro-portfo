import csv
from flask import Flask, redirect, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# Dynamically accept string parameters
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')


# Write the form data to database.txt
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')

# Write to a csv file
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # Write to csv file
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# Create route to submit form data
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        
        return redirect('/thankyou')
    else:
        return 'Something went wrong. Try again!'