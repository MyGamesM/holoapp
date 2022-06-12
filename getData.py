import os
from pprint import pp
import requests

os.system("cls")

class getData():
	def __init__(self, url: str) -> None:
		self.url = url
		self.count = 0

	def get(self):
		def get1(offset):
			data = requests.get(f"{self.url}?limit=50&offset={offset}").json()
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
				data['channels'][i]['id'] = i + offset + 1

			data = data['channels']

			return data

		data = get1(0) + get1(50)
		return data

	def getCount(self) -> int:
		self.count = 0
		self.get()
		return self.count

if __name__ == "__main__":
	app = getData(url="https://api.holotools.app/v1/channels")
	pp(len(app.get()))