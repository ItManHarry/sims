from flask.views import MethodView
from com.models import SysUser
class UserAPI(MethodView):
    def get(self, code):
        '''
        根据账号获取用户信息
        :return:
        '''
        user = SysUser.query.filter(SysUser.code == code.lower()).first()
        if user:
            return {'code': 200,
                    'message': 'S',
                    'info': {'name': user.name}
            }
        else:
            return {
                'code': 400,
                'message': '用户不存在！'
            }