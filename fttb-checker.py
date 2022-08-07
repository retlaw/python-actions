import requests
from datetime import datetime
import json
import os

fttb_data = {
    "Grabouw": "41.23.75.105",
    "Long Street": "196.213.32.201",
    "Vredendal": "41.23.143.57",
    "Ottery": "41.23.103.65",
    "De Doorns": "41.23.102.17",
    "Epping": "196.213.35.201",
    "Vredenburg": "41.23.102.241",
    "Moorreesburg": "41.23.88.129",
    "Paarl": "196.214.43.137",
    "Houtbay": "41.23.92.249"
}
fttb_pings = list()


def main():
    for branch in fttb_data:
        count = 1
        response = requests.get(
            url=f'http://13.244.137.122/?ip={fttb_data[branch]}&count={count}')
        fttb_pings.append({
            branch: {
                "result": response.json(),
                "count": count,
                "datetime": datetime.now().isoformat()
            }})
    print(json.dumps(fttb_pings))
    secret = os.environ["SOME_SECRET"]
    print(f'the secret is {secret}')


if __name__ == "__main__":
    main()
