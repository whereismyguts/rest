# Wheather rest-api
The service provides an API to work with wheather data
## Usage
### Methods
There is one method implemented by now.

```
POST /info/temperature
```
Defines the fact that temperature measured on client station passed through zero value at least one time
#### Input
name  | description
------------  | ----------
`station_config` | Contains station info, such as id, latitude and longitude
`data` | List of temperature values with timestamps
#### Output
`True` if air temperature value passed through zero value

otherwise `False`
#### Example
```
 {
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
```
## Docker
Service work on 5000 port. Run command in root directory:
```
docker-compose up --build
```
## Achitecture
<img src="./Wheather service scheme.svg">
