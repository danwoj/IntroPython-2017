import os

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'total' not in session:
        session['total'] = 0
    if request.method == 'POST':
        # Handle the form submission
        number = int(request.form['number'])
        session['total'] += number
    return render_template('add.jinja2', session=session)

@app.route('/save', methods=['POST'])
def save():
       total = session.get('total', 0)
       code = base64.b32encode(os.urandom(8)).decode().strip('=')

       saved_total = SavedTotal(value=total, code=code)
       saved_total.save()

       return render_template('save.jinja2', code=code)

if __name__ == "__main__":
       port = int(os.environ.get("PORT", 6738))
       app.run(host='localhost', port=port)