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
    "Houtbay": "41.23.92.249",
    "Cape Town City": "196.213.34.97",
    "N1 City": "196.213.52.201",
    "Neelsie": "196.213.52.57",
    "Bredasdorp": "196.213.52.41",
    "Caledon": "196.213.53.249",
    "Century City": "196.214.155.153",
    "Stellenbosch Commercial Secondary": "196.213.221.97",
    "Gardens": "196.214.143.241",
    "Piketberg": "41.23.75.161",
    "Willowbridge": "196.214.140.97",
    "Wellington": "41.23.128.233",
    "Tulbagh": "41.23.128.9",
    "Strand": "196.214.137.177",
    "StillBay": "41.23.103.73",
    "Stellenbosch": "196.213.107.113",
    "Springbok": "41.23.200.201",
    "Somerset West": "196.214.137.137",
    "Robertson": "196.214.137.193",
    "Promenade": "196.214.154.129",
    "Malmesbury": "41.23.102.65",
    "Khayelitsha": "41.23.92.121",
    "Greenpoint": "41.23.102.97",
    "Myhouse": "41.23.101.101"
}

fttb_pings = list()


def main():
    for branch in fttb_data:
        count = 1
        response = requests.get(
            url=f'http://13.244.137.122/?ip={fttb_data[branch]}&count={count}')
        fttb_pings.append(
            {
                "Branch": branch,
                "result": response.json(),
                "count": count,
                "datetime": datetime.now().isoformat()
            })
    print(json.dumps(fttb_pings))
    secret = os.environ["SOME_SECRET"]
    if secret == '1234':
        print(f'the secret is {secret} and correct')
    else:
        print('the secret is not correct')


if __name__ == "__main__":
    main()
