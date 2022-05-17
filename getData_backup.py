import os
import requests

os.system("cls")

class getData():
	def __init__(self, url: str) -> None:
		self.url = url

		self.get()

	def get(self):
		data = requests.get(self.url).json()
		self.count = data['count']

		del data['count']
		del data['total']

		for i in range(self.count):
			del data['channels'][i]['bb_space_id']
			del data['channels'][i]['description']
			del data['channels'][i]['published_at']
			del data['channels'][i]['video_count']
			del data['channels'][i]['video_original']

		data = data['channels']

		return data

	def getCount(self):
		return self.count

if __name__ == "__main__":
	app = getData(url="https://api.holotools.app/v1/channels?limit=50")