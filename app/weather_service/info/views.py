from weather_service.info import info_bp
from flask import request
from flask import Response
from .service import is_temp_cross_zero


@info_bp.route('/temperature', methods=['POST'])
def process_weather_data():
    if request.method == 'POST':
        try:
            data = request.get_json(force=True)
            temperature_list = [t['t_air'] for t in data['data'].values()]
            result = is_temp_cross_zero(temperature_list)
            return Response(str(result), status=200, mimetype='application/json')
        except:
            return Response(None, status=400, mimetype='application/json')
