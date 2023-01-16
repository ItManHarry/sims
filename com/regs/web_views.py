
def reg_web_blueprints(app):
    '''
    注册蓝本
    :param app:
    :return:
    '''
    from com.api.user import api_user
    app.register_blueprint(api_user, url_prefix='/api/user')