def reg_web_blueprints(app):
    '''
    注册蓝本
    :param app:
    :return:
    '''
    from com.api.resource import api
    app.register_blueprint(api, url_prefix='/api')  # 对外API