import requests
from config import BASE_URL, API_KEY
from dtos.sensor_data import SensorData
from models.plant import Plant

class Fetcher:
    def __init__(self):
        self.base_url = BASE_URL
        self.api_key = API_KEY

    def get_latest_sensors(self) -> SensorData:
        r = requests.get(url=f'{self.base_url}/api/plants',
                         headers={'X-Api-Key': self.api_key})
        data: list[Plant] = r.json()
        print(f"Fetched sensor data: {data}")

        ids = [x['waterlevel'] for x in sorted(data, key=lambda item: item["id"])]
        while len(ids) < 4:
            ids.append(0) # 0 = Plant is wet; 1 = Plant is dry

        return SensorData(s1=ids[0], s2=ids[1], s3=ids[2], s4=ids[3])