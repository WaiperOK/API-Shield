from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_pentest', methods=['POST'])
def run_pentest():
    url = request.form['url']
    graphql = request.form.get('graphql')
    command = ["python", "main.py", url]
    if graphql:
        command.insert(1, '--graphql')
    subprocess.run(command)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
