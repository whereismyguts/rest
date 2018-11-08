#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os

from flask_script import Manager
from weather_service.app import create_app


app = create_app(os.getenv('APP_CONFIG') or 'dev')
manager = Manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
