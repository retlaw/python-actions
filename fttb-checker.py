import requests
from datetime import datetime
import json
import os


fttb_data = {
    "Vangate": "196.214.166.153",
    "Zevenwagcht": "96.214.167.153",
    "Riversdale": "196.214.168.129",
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
    "Stellenbosch Commercial Primary": "41.164.74.137",
    "Stellenbosch Commercial Secondary": "196.213.221.97",
    "Worcester Commercial": "41.164.154.201",
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
    "TableBayMall": "196.213.222.81",
    "Parow": "41.164.182.209",
    "Cape Gate": "196.213.53.169",
    "Tygervalley": "196.213.209.145",
    "Worcester": "196.213.216.249",
    "Somerset Mall": "196.213.55.233",
    "Kenilworth": "196.213.53.25",
    "Rondebosch": "196.214.137.185",
    "Watergate": "196.214.159.113",
    "Tokai": "196.214.144.81",
    "Vineyard": "196.214.148.145",
    "Villiersdorp": "41.23.103.9",
    "LongBeachMall": "196.214.63.121",
    "Junxion Mall": "41.23.74.217",
    "Ceres": "41.23.74.161",
    "ClanWilliam": "41.23.74.105",
    "Brackenfell": "196.214.43.33"
}

fttb_pings = list()
fttb_pings_failures = list()


def main():
    for branch in fttb_data:
        count = 1
        response = requests.get(
            url=f'http://13.244.243.42/?ip={fttb_data[branch]}&count={count}')
        # print("result" in response.json())
        fttb_pings.append(
            {
                "Branch": branch,
                "IP": fttb_data[branch],
                "response": response.json(),
                "count": count,
                "datetime": datetime.now().isoformat()
            })
        if "result" in response.json():
            fttb_pings_failures.append(
                {
                    "Branch": branch,
                    "IP": fttb_data[branch],
                    "response": response.json(),
                    "count": count,
                    "datetime": datetime.now().isoformat()
                })

    # print(json.dumps(fttb_pings))
    print(json.dumps(fttb_pings_failures))
    # secret = os.environ["SOME_SECRET"]
    # if secret == '1234':
    #     print(f'the secret is {secret} and correct')
    # else:
    #     print('the secret is not correct')


if __name__ == "__main__":
    main()
