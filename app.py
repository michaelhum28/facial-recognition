from flask import Flask
from flask import render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python_script')
def run_python_script():
    result = subprocess.run(['python', 'FaceMeshModule.py'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True)
