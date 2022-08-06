import re
from urllib import response
import requests

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
fttb_pings = {}
def main():
  for branch in fttb_data:
    response = requests.get(url=f'http://13.244.137.122/?ip={fttb_data[branch]}&count=1')
    fttb_pings[branch] = response.json()
  print(fttb_pings)

if __name__ == "__main__":
  main()
