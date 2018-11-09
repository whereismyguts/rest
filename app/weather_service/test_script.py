import multiprocessing.dummy as multiprocessing
import requests
import json
import time

data = {
    "station_config": {
        'station_id': 234,
        'lat': 45,
        'lon': 45,
    },
    'data': {
        '2016-12-30 10:00 UTC': {
            't_air': 1,
        },
        '2016-12-30 11:00 UTC': {
            't_air': 2,
        },
        '2016-12-30 12:00 UTC': {
            't_air': 3,
        },
        '2016-12-30 13:00 UTC': {
            't_air': 0,
        },
    }
}

t = time.time()



def poll(req):
    response = requests.post(
        'http://127.0.0.1:5000/info/temperature',
        data=json.dumps(req),
    )
    return response


p = multiprocessing.Pool()
results = p.map(lambda r: poll(r), [data]*3000)

p.close()
p.join()

print("\n".join(['%s: %s' % (r, r.text) for r in results]))

print(time.time() - t)
