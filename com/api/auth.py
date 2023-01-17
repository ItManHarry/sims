from flask.views import MethodView
from flask import request, jsonify, current_app, g
from authlib.jose import jwt, JoseError
from com.models import SysUser
class AuthAPI(MethodView):

    def post(self):
        '''
        获取令牌
        :return:
        '''
        grant_type = request.form.get('grant_type')
        username = request.form.get('username')
        password = request.form.get('password')
        if grant_type is None or grant_type != 'password':
            return {
                'code': 400,
                'message': "Grant type must be 'password'!"
            }
        user = SysUser.query.filter(SysUser.code == username.lower()).first()
        if user is None or not user.validate_password(password):
            return {
                'code': 400,
                'message': 'Either user name or password is wrong!'
            }
        token = generate_token(user)
        response = jsonify(code=200, message='success', access_token=token, token_type='Bearer')
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response

def generate_token(user):
    '''
    生成令牌: JWT(Json Web Token)
    :param user:
    :return:
    '''
    # 签名算法
    header = {'alg': 'HS256'}
    # 签名秘钥
    key = current_app.config['SECRET_KEY']
    # 签名附带信息
    payload = {'userid': user.id}
    token = jwt.encode(header=header, payload=payload, key=key)
    # 生成的token为字节类型，需要转换为字符串类型
    return token.decode(encoding='utf-8')

def validate_token(token):
    '''
    验证令牌
    :param token:
    :return:
    '''
    key = current_app.config['SECRET_KEY']
    try:
        payload = jwt.decode(token, key)
        print(payload)
    except JoseError:
        return False
    user = SysUser.query.get(payload['userid'])
    if user is None:
        return False
    g.current_user = user   # 存储user对象到g
    return True