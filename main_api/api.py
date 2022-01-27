import requests
from functools import lru_cache
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class ApiCallToVerifyVehicle:
    @lru_cache(maxsize=4096)
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{self.make}?format=json'
        try:
            self.response = requests.get(self.url, verify=False).json()["Results"]
        except Exception as e:
            raise e

    @lru_cache(maxsize=1024)
    def DoesExist(self) -> bool:
        for r in self.response:
            if r["Model_Name"] == self.model.upper():
                return True
        return False

