from flask import Flask, render_template, redirect, request, send_from_directory
import os
from werkzeug.utils import secure_filename 
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'

# local host file ===============================
@app.route('/file/<path:file>')
def aksesFile(file):
    return send_from_directory ('file', file)

# all page ======================================
@app.route('/')
def landing_page():
    return render_template('form.html')

@app.route('/home')
def landing_page2():
    return redirect ('/')    

@app.route('/hasil', methods = ['GET','POST'])
def form():
    data_f = request.form
    url = 'https://pokeapi.co/api/v2/pokemon/' + dict(data_f)['name'].lower()
    data = requests.get(url)
    if data.status_code == 404:
        return render_template ('error.html')
    else:
        pokemon = data.json()
        return render_template ('result.html',data=pokemon)


if __name__ == '__main__':
    app.run(
        debug=True
    )
