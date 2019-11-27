from app import db

class Build(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	buildName = db.Column(db.String(144), nullable=False)
	score = db.Column(db.Integer)

	def __init__(self, name):
		self.buildName = name
		self.score = 0
