import os
from pprint import pp
import requests

os.system("cls")

class getData():
	def __init__(self, url: str) -> None:
		self.url = url
		self.count = 0

	def get1(self):
		data = requests.get(self.url).json()
		count = data['count']
		self.count += data['count']

		del data['count']
		del data['total']

		for i in range(count):
			del data['channels'][i]['bb_space_id']
			del data['channels'][i]['description']
			del data['channels'][i]['published_at']
			del data['channels'][i]['video_count']
			del data['channels'][i]['video_original']
			# del data['channels'][i]['photo']
			data['channels'][i]['id'] = i + 1

		data = data['channels']

		return data

	def get2(self):
		data = requests.get(f"{self.url}&offset=50").json()
		count = data['count']
		self.count += data['count']

		del data['count']
		del data['total']

		for i in range(count):
			del data['channels'][i]['bb_space_id']
			del data['channels'][i]['description']
			del data['channels'][i]['published_at']
			del data['channels'][i]['video_count']
			del data['channels'][i]['video_original']
			# del data['channels'][i]['photo']
			data['channels'][i]['id'] = 51 + i

		data = data['channels']

		return data

	def get(self):
		data = self.get1() + self.get2()

		return data

	def getCount(self):
		self.count = 0
		self.get()
		return self.count

if __name__ == "__main__":
	app = getData(url="https://api.holotools.app/v1/channels?limit=50")
	pp(app.getCount())