import os
import sys
import pytest
import json

# Add the parent directory to the sys.path to allow for package imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, User, Tree

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()
        # Add a dummy user for testing foreign key constraints
        test_user = User(username='testuser', email='test@example.com', password='password')
        db.session.add(test_user)
        db.session.commit()

    yield client

    with app.app_context():
        db.drop_all()

def test_get_trees_empty(client):
    """Test getting trees when there are none."""
    response = client.get('/api/trees')
    assert response.status_code == 200
    assert response.json == []

def test_create_tree(client):
    """Test creating a new tree."""
    response = client.post('/api/trees', data=json.dumps({
        'lat': 36.7753,
        'lon': 3.0602,
        'guardian_id': 1
    }), content_type='application/json')
    assert response.status_code == 201
    assert response.json['lat'] == 36.7753

def test_get_trees_after_creation(client):
    """Test getting trees after one has been created."""
    client.post('/api/trees', data=json.dumps({
        'lat': 36.7753,
        'lon': 3.0602,
        'guardian_id': 1
    }), content_type='application/json')

    response = client.get('/api/trees')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['lat'] == 36.7753

def test_get_specific_tree(client):
    """Test getting a specific tree by its ID."""
    # Create a tree first
    client.post('/api/trees', data=json.dumps({
        'lat': 36.7753,
        'lon': 3.0602,
        'guardian_id': 1
    }), content_type='application/json')

    # Get the tree with id 1
    response = client.get('/api/trees/1')
    assert response.status_code == 200
    assert response.json['id'] == 1
    assert response.json['lat'] == 36.7753

def test_create_tree_missing_data(client):
    """Test creating a tree with missing data."""
    response = client.post('/api/trees', data=json.dumps({
        'lat': 36.7753
    }), content_type='application/json')
    assert response.status_code == 400
    assert response.json == {'error': 'Missing data'}
