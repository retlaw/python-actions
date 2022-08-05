from urllib import response
import requests

def main():
  response = requests.get(url='http://13.244.137.122/?ip=196.213.34.97&count=1')
  print(response.json())

if __name__ == "__main__":
  main()
