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
api.add_url_rule('/user/get/<code>', view_func=UserAPI.as_view('get'), methods=['GET', 'POST'])