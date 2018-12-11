from flask import Flask, render_template, request, session, Session


app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'super secret key'
# Session(app)

notes = []

@app.route('/', methods=['get', 'post'])
def hello_world():
    headline = 'Hello from me!'
    df = True
    names = ['Alice', 'Bob', 'Peter']
    if session.get('notes') is None:
        session['notes'] = []       # my personal session's var

    if request.method == 'POST':
        note = request.form.get('note')
        # notes.append(note)            # global var
        session['notes'].append(note)   # my session's var
    return render_template('index.html', headline=headline, names=names, test=df, notes=session['notes'])

@app.route('/more')
def more():
    return render_template('more.html')

@app.route('/form', methods=['POST'])       # не откроется напрямую из-за метода
def form():
    name = request.form.get('name')
    return render_template('form.html', name=name)



@app.route('/<string:name>')    # ANY string in URL to var name, and give this var to func
def hello(name):
    return f'Hello {name}!'

@app.route('/bye')
def bye():
    headline = 'Goodbye!'
    return render_template('index.html', headline=headline)


if __name__ == '__main__':
    app.run()
