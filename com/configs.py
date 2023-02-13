import os
import logging
dev_db = os.getenv('DEV_DB', 'mysql+pymysql://sims:Sims2023@localhost:3306/sims')
uat_db = os.getenv('UAT_DB', 'mysql+pymysql://sims:Sims2023@localhost:3306/sims')
pro_db = os.getenv('PRO_DB', 'mysql+pymysql://sims:Sims2023@localhost:3306/sims')
base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
'''
全局配置
'''
class GlobalConfig():
    # import secrets
    # print(secrets.token_hex())
    SECRET_KEY = os.getenv('SECRET_KEY')  # secrets.token_hex()
    LOG_LEVEL = logging.DEBUG
    LOG_PATH = os.path.join(base_dir, 'logs\\log')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
开发环境
'''
class DevConfig(GlobalConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOP_DATABASE_URL', dev_db)
    LOG_LEVEL = logging.ERROR
'''
测试环境
'''
class UatConfig(GlobalConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('UAT_DATABASE_URL', uat_db)
    WTF_CSRF_ENABLED = False
    TESTING = True
    LOG_LEVEL = logging.ERROR
'''
正式环境
'''
class ProConfig(GlobalConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCT_DATABASE_URL', pro_db)
    LOG_LEVEL = logging.ERROR

config_dict = {
    'dev_config': DevConfig,
    'uat_config': UatConfig,
    'pro_config': ProConfig
}