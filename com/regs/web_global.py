from flask_login import current_user
from flask import flash, redirect, url_for, render_template
from com.utils import get_time_today

def reg_web_global_path(app):
    '''
    配置全局路径
    :param app:
    :return:
    '''
    @app.route('/test')
    def test():
        return render_template('test.html')

    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.before_request
    def request_intercept_before():
        if current_user is None:
            flash('登录超时，请重新登录！')
            return redirect(url_for('auth.login'))
        else:
            print('Session正常')

def reg_web_global_context(app):
    @app.context_processor
    def config_template_conext():
        return dict(get_time_today=get_time_today)