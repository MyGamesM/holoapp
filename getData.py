import os
from pprint import pp
import requests

os.system("cls")

class getData():
	def __init__(self, url: str) -> None:
		self.url = url
		self.count = 0

	def get(self) -> list:
		def get(offset):
			data = requests.get(f"{self.url}channels?limit=50&offset={offset}").json()
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

		data = get(0) + get(50)

		return data

	def getLive(self) -> dict:
		data = requests.get(f"{self.url}live?max_upcoming_hours=48").json()
		# ?channel_id=34&max_upcoming_hours=168&lookback_hour=0&hide_channel_desc=1
		# channel_id={34}

		del data['ended']
		del data['upcoming']

		for i in range(len(data['live'])):
			del data['live'][i]['id']
			del data['live'][i]['bb_video_id']
			del data['live'][i]['live_start']
			del data['live'][i]['live_end']
			del data['live'][i]['live_viewers']
			del data['live'][i]['channel']['bb_space_id']
			del data['live'][i]['channel']['description']
			del data['live'][i]['channel']['published_at']
			del data['live'][i]['channel']['video_count']

		return data

	def getCount(self) -> int:
		self.count = 0
		self.get()
		return self.count

if __name__ == "__main__":
	app = getData(url="https://api.holotools.app/v1/")
	pp(app.getLive())