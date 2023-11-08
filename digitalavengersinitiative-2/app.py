from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/searchemail', methods=['GET', 'POST'])
def searchemail():
    if request.method == 'POST':
        email = request.form['email']
        try:
            # Use subprocess to run the 'holehe' library with the provided email
            result = subprocess.check_output(['holehe', email], text=True, stderr=subprocess.PIPE)
            return render_template('result.html', result=result)
        except subprocess.CalledProcessError as e:
            return f"Error executing the 'holehe' library: {e}"
    return render_template('home.html')

@app.route('/searchuname', methods=['GET', 'POST'])
def searchname():
    if request.method == 'POST':
        uname = request.form['uname']
        try:
            result = subprocess.getoutput(['C:/Users/rshob/AppData/Local/Programs/Python/Python312/python.exe','sherlock/sherlock', uname])
            return f"{result}"
            # render_template('result.html', result=result)
        except subprocess.CalledProcessError as e:
            return f"Error executing the sherlock library: {e}"
    return render_template('home.html')

@app.route('/searchphone', methods=['GET', 'POST'])
def searchphone():
    if request.method == 'POST':
        phone = request.form['phone']
        try:
            result = subprocess.check_output(['ignorant','91',phone], text=True, stderr=subprocess.PIPE)
            # return f"{result}"
            return render_template('phoneresult.html', result=result)
        except subprocess.CalledProcessError as e:
            return f"Error executing the sherlock library: {e}"
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)