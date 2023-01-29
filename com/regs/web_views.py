def reg_web_blueprints(app):
    '''
    注册蓝本
    :param app:
    :return:
    '''
    from com.api.all import api
    from com.cal.all import cal
    from com.views.sys.user import bp_user
    app.register_blueprint(api, url_prefix='/api')      # 对外API
    app.register_blueprint(cal, url_prefix='/tmpls')    # 日历
    app.register_blueprint(bp_user, url_prefix='/user') # 用户