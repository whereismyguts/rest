from weather_service.info import info_bp
from flask import request
from .controller import InfoComputation


def process_weather_data(data):
    return [t['t_air'] for t in data['data'].values()]


@info_bp.route('/temperature', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            temperature_list = process_weather_data(data)
            result = InfoComputation.is_temp_crossing_zero(temperature_list)
            return str(result)
        except Exception as e:
            return str(e)

    if request.method == 'GET':
        return "Route is working. #TODO: remove get method"
