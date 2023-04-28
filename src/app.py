from flask import Flask, render_template, request, redirect, url_for
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.debug = False
# Set the allowed file extensions for image uploads

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping', methods=['POST'])
def ping():
    address = request.form['address']
    result = subprocess.run(f'ping -c 4 {address}',shell=True, capture_output=True, text=True )
    return result.stdout

# Add an admin panel with password protection
@app.route('/flag', methods=['GET', 'POST'])
def flag():
    if request.method == 'POST':
        password = request.form['password']

        # Check if the password is correct
        if password == 'RdcQvpwcuwnm3hgGwutjqe4Q':
            return 'FLAG{1_l0v3_CTFs!}'
        else:
            return redirect(url_for('admin'))

    return render_template('admin.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

