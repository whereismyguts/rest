from flask_testing import TestCase
from manage import app


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('weather_service.config.TestingConfig')
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass

        