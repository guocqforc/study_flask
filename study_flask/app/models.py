# coding:utf-8
from . import db
from flask.ext.login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from . import login_manager

class Role(db.Model):
    # 这个是定义在数据库中使用的表名
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')  # 在User 表中创建了role 属性 在User表中访问role

    # 就是访问 相关联的Role对象的列表
    def __repr__(self):
        return '<Roles %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)  # index 这里创建了一个索引
    email = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 和roles表中的id进行了外界关联
    password_hash = db.Column(db.String(128))

    # sex = db.Column(db.String(12)) # 新增加一个字段看看 migrate 有没有用

    @property
    def password(self):
        raise AttributeError(u'password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Users %r>' % self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
