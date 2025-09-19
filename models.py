from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=False, nullable=False)
    confirm_password = db.Column(db.String(40), unique=False, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    qualification = db.Column(db.String(80), unique=False, nullable=False)
    dob = db.Column(db.String(80), unique=False, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)
    scores = db.relationship('Scores', backref='user', lazy=True)

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    chapters = db.relationship('Chapter', backref='subject', lazy=True, cascade="all, delete")

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    quizzes = db.relationship('Quiz', backref='chapter', lazy=True, cascade="all, delete")
    
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.Date, nullable=False)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    time_duration = db.Column(db.Time, nullable=False)
    level = db.Column(db.String(80), nullable=False)
    scores = db.relationship('Scores', backref='quiz', cascade="all, delete", lazy=True)
    questions = db.relationship('Question', backref='quiz', cascade="all, delete", lazy=True)



class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    question = db.Column(db.String(80), unique=True, nullable=False)
    option1 = db.Column(db.String(80), nullable = False)
    option2 = db.Column(db.String(80), nullable = False)
    option3 = db.Column(db.String(80), nullable = False)
    option4 = db.Column(db.String(80), nullable = False)
    answer = db.Column(db.String(80), nullable = False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable = False)

class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_stamp_of_quiz = db.Column(db.DateTime, unique=False, nullable=False)
    total_scored = db.Column(db.Integer, unique=False, nullable=False)
    date_taken = db.Column(db.Date, nullable=False, default=date.today)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable = False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
