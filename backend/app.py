from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

### articles section ###


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

# get all articles


@app.route('/get', methods=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    result = articles_schema.dump(all_articles)
    return jsonify(result)


# get single article by id


@app.route('/get/<id>/', methods=['GET'])
def get_article(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)


# add an article


@app.route('/add', methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)

    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)


# update an article


@app.route('/update/<id>/', methods=['PUT'])
def update_article(id):
    article = Articles.query.get(id)

    article.title = request.json['title']
    article.body = request.json['body']

    db.session.commit()
    return article_schema.jsonify(article)


# delete an article


@app.route('/delete/<id>/', methods=['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article)


#### end section ####

### books section ####


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    points = db.Column(db.Integer)
    rentedBooks = db.Column(db.String(100))

    def __init__(self, id, name, points, rentedBooks):

        self.id = id
        self.name = name
        self.points = points
        self.rentedBooks = rentedBooks


class MemberSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'points', 'rentedBooks')


member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

### add member route


@app.route('/add_member', methods=['POST'])
def addMember():
    id = request.json['id']
    name = request.json['name']
    points = request.json['points']
    rentedBooks = request.json['rentedBooks']

    member = Member(id, name, points, rentedBooks)

    db.session.add(member)
    db.session.commit()
    return member_schema.jsonify(member)


### get a member route


@app.route('/get_member/<id>', methods=['GET'])
def getMember(id):
    member = Member.query.get(id)
    print(member)
    db.session.commit()

    return member_schema.jsonify(member)


### edit member route


@app.route('/edit_member/<id>', methods=['PUT'])
def editMember(id):
    member = Member.query.get(id)

    member.id = request.json['id']
    member.name = request.json['name']
    member.points = request.json['points']
    member.rentedBooks = request.json['rentedBooks']

    db.session.commit()

    return member_schema.jsonify(member)


#### end section ####

### books section ####


class Books(db.Model):
    bookID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    authors = db.Column(db.String(50))
    average_rating = db.Column(db.Float)
    isbn = db.Column(db.Integer)
    isbn13 = db.Column(db.Integer)
    language_code = db.Column(db.String(10))
    num_pages = db.Column(db.Integer)
    ratings_count = db.Column(db.Integer)
    text_reviews_count = db.Column(db.Integer)
    publication_date = db.Column(db.String(10))
    publisher = db.Column(db.String(25))
    quantity = db.Column(db.Integer)
    rented = db.Column(db.String(3))

    def __init__(self, bookID, title, authors, average_rating, isbn, isbn13,
                 language_code, num_pages, ratings_count, text_reviews_count,
                 publication_date, publisher, quantity, rented):

        self.bookID = bookID
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date = publication_date
        self.publisher = publisher
        self.quantity = quantity
        self.rented = rented


class BookSchema(ma.Schema):
    class Meta:
        fields = ('bookID', 'title', 'authors', 'average_rating', 'isbn',
                  'isbn13', 'language_code', 'num_pages', 'ratings_count',
                  'text_reviews_count', 'publication_date', 'publisher',
                  'quantity', 'rented')


book_schema = BookSchema()
books_schema = BookSchema(many=True)

# add a book route


@app.route('/add_book', methods=['POST'])
def add_book():
    bookID = request.json['bookID']
    title = request.json['title']
    authors = request.json['authors']
    average_rating = request.json['average_rating']
    isbn = request.json['isbn']
    isbn13 = request.json['isbn13']
    language_code = request.json['language_code']
    num_pages = request.json['  num_pages']
    ratings_count = request.json['ratings_count']
    text_reviews_count = request.json['text_reviews_count']
    publication_date = request.json['publication_date']
    publisher = request.json['publisher']
    quantity = request.json['quantity']
    rented = request.json['rented']

    book = Books(bookID, title, authors, average_rating, isbn, isbn13,
                 language_code, num_pages, ratings_count, text_reviews_count,
                 publication_date, publisher, quantity, rented)

    db.session.add(book)
    db.session.commit()
    return article_schema.jsonify(book)


# get all books


@app.route('/get_books', methods=['GET'])
def get_books():
    books = Books.query.all()
    result = books_schema.dump(books)
    return jsonify(result)


# update a book


@app.route('/update_book/<id>', methods=['PUT'])
def update_book(id):
    book = Books.query.get(id)
    """ book.bookID = request.json['bookID']
    book.title = request.json['title']
    book.authors = request.json['authors']
    book.average_rating = request.json['average_rating']
    book.isbn = request.json['isbn']
    book.isbn13 = request.json['isbn13']
    book.language_code = request.json['language_code']
    book.num_pages = request.json['  num_pages']
    book.ratings_count = request.json['ratings_count']
    book.text_reviews_count = request.json['text_reviews_count']
    book.publication_date = request.json['publication_date']
    book.publisher = request.json['publisher'] """
    book.quantity = request.json['quantity']
    book.rented = request.json['rented']

    db.session.commit()

    return article_schema.jsonify(book)


# get a book by ID


@app.route('/get_book/<id>', methods=['GET'])
def getBook(id):
    book = Books.query.get(id)
    result = book_schema.dump(book)
    return jsonify(result)


# delete a book


@app.route('/delete_book/<id>', methods=['DELETE'])
def delete_book(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return book_schema.jsonify(book)


#### end section ####
if __name__ == "__main__":
    app.run(debug=True)