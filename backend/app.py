import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app) # This will allow all origins by default

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False) # Hashed password
    wilaya = db.Column(db.String(50), nullable=True)
    rank = db.Column(db.String(50), default='New Planter')
    trees = db.relationship('Tree', backref='guardian', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(50), default='Planted')
    guardian_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'lat': self.lat,
            'lon': self.lon,
            'photo_url': self.photo_url,
            'status': self.status,
            'guardian_id': self.guardian_id
        }

    def __repr__(self):
        return f'<Tree {self.id}>'

@app.route('/')
def index():
    return "Hello, GreenDZ Backend!"

# Get all trees
@app.route('/api/trees', methods=['GET'])
def get_trees():
    trees = Tree.query.all()
    return jsonify([tree.to_dict() for tree in trees])

# Get a specific tree
@app.route('/api/trees/<int:id>', methods=['GET'])
def get_tree(id):
    tree = Tree.query.get_or_404(id)
    return jsonify(tree.to_dict())

# Create a new tree
@app.route('/api/trees', methods=['POST'])
def create_tree():
    data = request.get_json()
    # Basic validation
    if not data or not all(k in data for k in ('lat', 'lon', 'guardian_id')):
        return jsonify({'error': 'Missing data'}), 400

    new_tree = Tree(
        lat=data['lat'],
        lon=data['lon'],
        photo_url=data.get('photo_url'),
        guardian_id=data['guardian_id']
    )
    db.session.add(new_tree)
    db.session.commit()
    return jsonify(new_tree.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
