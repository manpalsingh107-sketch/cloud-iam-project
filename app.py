from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'secret123'

db = SQLAlchemy(app)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))
    tenant_id = db.Column(db.Integer)

@app.route('/')
def home():
    return "IAM Project Running"

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(
        username=data['username'],
        password=data['password'],
        role=data['role'],
        tenant_id=data['tenant_id']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()

    if not user:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=user.role)
    return jsonify(access_token=token)

@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    role = get_jwt_identity()
    if role != 'admin':
        return jsonify({"msg": "Access denied"}), 403
    return jsonify({"msg": "Welcome Admin"})

# Create DB tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)