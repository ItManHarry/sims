from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from com.plugins import db
from datetime import datetime
import uuid

class BaseModel():
    id = db.Column(db.String(32), primary_key=True)                     # 表主键ID
    active = db.Column(db.Boolean, default=True)                        # 是否使用(默认已使用)
    createtime_utc = db.Column(db.DateTime, default=datetime.utcnow)    # 创建时间(UTC标准时间)
    createtime_loc = db.Column(db.DateTime, default=datetime.now)       # 创建时间(本地时间)
    create_id = db.Column(db.String(32))                                # 创建人员
    updatetime_utc = db.Column(db.DateTime, default=datetime.utcnow)    # 更新时间(UTC标准时间)
    updatetime_loc = db.Column(db.DateTime, default=datetime.now)       # 更新时间(本地时间)
    update_id = db.Column(db.String(32))                                # 更新人员

    @property
    def created_by(self):
        return SysUser.query.get(self.create_id)

    @property
    def updated_by(self):
        return SysUser.query.get(self.update_id)
'''
系统用户
'''
class SysUser(BaseModel, db.Model, UserMixin):
    name = db.Column(db.String(32))                         # 用户姓名
    code = db.Column(db.String(32), unique=True)            # 用户账号
    pwd = db.Column(db.String(128))                         # 用户密码
    is_admin = db.Column(db.Boolean, default=False)         # 是否超级管理员(默认否)
    email = db.Column(db.String(32))                        # 电子邮箱
    phone = db.Column(db.String(24))                        # 电话号码
    logs = db.relationship('SysLog', back_populates='user') # 系统操作日志

    def set_password(self, password):
        self.pwd = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.pwd, password)

    @staticmethod
    def create_admin():
        admin = SysUser.query.filter(SysUser.code == 'admin').first()
        if admin is None:
            admin = SysUser(id=uuid.uuid4().hex, name='Administrator', code='admin', is_admin=True)
            admin.set_password('Sims2022$')
            db.session.add(admin)
            db.session.commit()
            print('超级管理员创建成功！！！')
        else:
            print('超级管理员已创建，不要重复创建！！！')
'''
系统操作日志
'''
class SysLog(BaseModel, db.Model):
    url = db.Column(db.String(64))              # 菜单url
    operation = db.Column(db.Text)              # 操作内容
    user_id = db.Column(db.String(32), db.ForeignKey('sys_user.id'))
    user = db.relationship('SysUser', back_populates='logs')