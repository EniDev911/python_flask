from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/task.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

@app.route('/create-task', methods=['POST'])
def create():
    task = Task(content=request.form['task'], done=False)
    db.session.add(task)
    db.session.commit()
    return 'saved'      


if __name__ == '__main__':
    app.run(debug=True) 


