from flask import Flask
from com.configs import config_dict
from com.regs.web_log import setup_log
from com.regs.web_global import reg_web_global_path, reg_web_global_context
from com.regs.web_plugins import reg_web_plugins
from com.regs.web_shells import reg_web_shell, reg_web_commands
from com.regs.web_views import reg_web_blueprints

def create_app(config=None):
    if config is None:
        config = 'dev_config'
    # 实例化应用
    app = Flask(__name__)
    # 装载配置
    app.config.from_object(config_dict[config])
    # 配置日志
    setup_log(config_dict[config])
    # 配置全局路径
    reg_web_global_path(app)
    # 配置全局模板函数
    reg_web_global_context(app)
    # 配置插件
    reg_web_plugins(app)
    # 配置shell
    reg_web_shell(app)
    # 配置自定义命令
    reg_web_commands(app)
    # 注册蓝本
    reg_web_blueprints(app)
    return app