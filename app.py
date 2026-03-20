from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'secret123'

db = SQLAlchemy(app)
jwt = JWTManager(app)

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.LargeBinary)
    role = db.Column(db.String(20))
    tenant_id = db.Column(db.Integer)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    action = db.Column(db.String(200))

@app.route('/')
def home():
    return "IAM Project Running"

@app.route('/register', methods=['POST'])
def register():
    data = request.json

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    user = User(
        username=data['username'],
        password=hashed_password,
        role=data['role'],
        tenant_id=data['tenant_id']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if not user or not bcrypt.checkpw(data['password'].encode('utf-8'), user.password):
        return jsonify({"msg": "Invalid credentials"}), 401

    log = Log(username=user.username, action="User logged in")
    db.session.add(log)
    db.session.commit()

    token = create_access_token(identity=f"{user.role}:{user.tenant_id}")
    return jsonify(access_token=token)

@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    data = get_jwt_identity()
    role, tenant = data.split(":")

    if role != 'admin':
        return jsonify({"msg": "Access denied"}), 403

    log = Log(username="admin", action=f"Admin accessed tenant {tenant}")
    db.session.add(log)
    db.session.commit()

    return jsonify({"msg": f"Welcome Admin of Tenant {tenant}"})

@app.route('/logs', methods=['GET'])    
def get_logs():
    logs = Log.query.all()
    result = []

    for log in logs:
        result.append({
            "username": log.username,
            "action": log.action
        })

    return jsonify(result)

# Create DB tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)