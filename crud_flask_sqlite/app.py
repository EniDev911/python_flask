from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.sqlite"
db = SQLAlchemy(app)

class Book(db.Model):
	"""Create model of book"""
	__tablename__ = 'book'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, unique=True, nullable= False)


db.session.add(Book(id = 2,title = "Torre Oscura",))
db.session.commit()
db.create_all()

books = Book.query.all()
print(books)



@app.route('/')
def index():
	return 'Hello world'

@app.route('/edit')
def edit_book():
	return 'Edit books'

@app.route('/update')
def update_book():
	return 'update books'

@app.route('/delete')
def delete_book():
	return 'delete books'

if __name__ == '__main__':
	app.run(host='localhost', port=3000, debug=True)
