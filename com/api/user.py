from flask.views import MethodView
from com.models import SysUser
class UserAPI(MethodView):
    def get(self, code):
        '''
        更加账号获取用户信息
        :return:
        '''
        user = SysUser.query.filter(SysUser.code == code.lower()).first()
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