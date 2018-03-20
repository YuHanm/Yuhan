from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Fianna'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost:3306/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(16), nullable=False, server_default='', unique=True)
    user = db.relationship('User', backref='role',lazy='select')
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'),nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username

def create():
    admin_role = Role(name='Admin')
    YuHan_role = Role(name="YuHan")
    user_role = Role(name='User')
    Yz_role = Role(name='333')
   # db.session.add(Yz_role)
   #  user_john = User(username='you', role=Yz_role)
   #  db.session.add(user_john)
    #修改数据
    # admin = Role.query.filter_by(name='Administrator2').first()
    # admin.name = 'Admin'
    # ad = Role.query.filter_by(name='Administrator').first()
    # db.session.delete(ad)
    # db.session.commit()

    #print(admin_role)
    Role.query.all()

if __name__ == '__main__':
    create()