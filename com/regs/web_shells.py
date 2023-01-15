import click, uuid
from com.plugins import db
def reg_web_shell(app):
    @app.shell_context_processor
    def config_shell_context():
        return dict(db=db)
def reg_web_commands(app):
    @app.cli.command()
    # @click.option('--admin_code', prompt=True, help='管理员账号')
    # @click.option('--admin_password', prompt=True, help='管理员密码', hide_input=True, confirmation_prompt=True)
    def init():
        from com.models import SysUser
        click.echo('执行数据库初始化......')
        db.create_all()
        click.echo('数据库初始化完毕！')
        click.echo('创建超级管理员')
        SysUser.create_admin()