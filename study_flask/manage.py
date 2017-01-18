# coding:utf-8

import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('flask_config') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_content():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_content))
manager.add_command("db", MigrateCommand)

@manager.command
def test():
    """
    Run the unit tests
    :return:
    """
    import unittest
    tests = unittest.TestLoader().discover('tests') # 后面那个是测试文件所在的文件夹名字
    unittest.TextTestResult(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
