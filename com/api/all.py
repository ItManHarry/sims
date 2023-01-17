from flask import Blueprint
from flask_cors import CORS
from com.plugins import csrf
api = Blueprint('api', __name__)
# 添加跨域支持
CORS(api)
# 剔除csrf保护
csrf.exempt(api)
# 注册路由
from .user import UserAPI
from .auth import AuthAPI
api.add_url_rule('/user/<code>', view_func=UserAPI.as_view('user_api'), methods=['GET'])
api.add_url_rule('/auth/get_token', view_func=AuthAPI.as_view('auth_api'), methods=['POST'])