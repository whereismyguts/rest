import unittest
from unittest import mock
from manage import app
from test.base import BaseTestCase
from weather_service.info.service import is_temp_cross_zero
from weather_service.info.views import process_weather_data
from flask import request


class TestInfoService(BaseTestCase):
    data = {
        "station_config": {
            'station_id': 234,
            'lat': 45,
            'lon': 45,
        },
        'data': {
            '2016-12-30 10:00 UTC': {
                't_air': 5,
            },
            '2016-12-30 11:00 UTC': {
                't_air': 4,
            },
            '2016-12-30 12:00 UTC': {
                't_air': -10,
            },
            '2016-12-30 13:00 UTC': {
                't_air': 2,
            },
        }
    }
    bad_data = {'bad_key':'bad_value'}
    
    def test_temperature_cross_zero(self):
        result =  is_temp_cross_zero([1,2,3,-6,2,])
        self.assertTrue(result)

    def test_temperature_touch_zero(self):
        result =  is_temp_cross_zero([1,2,0,0,2,])
        self.assertTrue(result)

    def test_temperature_avoid_zero(self):
        result =  is_temp_cross_zero([1,2,3,6,2,])
        self.assertFalse(result)

    
    def test_post_valid_data(self):
        m = mock.MagicMock()
        m.get_json.return_value = self.data
        m.method = "POST"
        with mock.patch("weather_service.info.views.request", m):
            res = process_weather_data()
            self.assertTrue("200 OK" == res.status)

    def test_post_invalid_data(self):
        m = mock.MagicMock()
        m.get_json.return_value = self.bad_data
        m.method = "POST"
        with mock.patch("weather_service.info.views.request", m):
            res = process_weather_data()
            print(res.status)
            self.assertTrue("400 BAD REQUEST" == res.status)

if __name__ == '__main__':
    unittest.main()