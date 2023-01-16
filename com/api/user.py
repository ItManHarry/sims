from flask import Blueprint
from flask_cors import CORS
from com.models import SysUser
from com.plugins import csrf
api_user = Blueprint('api_user', __name__)
# 添加跨域支持
CORS(api_user)
# 剔除csrf保护
csrf.exempt(api_user)
@api_user.route('/get_info/<id>', methods=['GET', 'POST'])
def get_info(id):
    user = SysUser.query.get(id)
    if user:
        return {'code': 1,
                'message': 'S',
                'info': {'name': user.name}
        }
    else:
        return {
            'code': 0,
            'message': '用户不存在！'
        }