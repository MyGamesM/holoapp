from flask import Flask, render_template #, redirect, url_for
from getData import getData

app = Flask(__name__)

getDataApp = getData(url="https://api.holotools.app/v1/channels?limit=50")
data = getDataApp.get()
count = getDataApp.getCount()

@app.route("/")
def home():
	return render_template("index.html", count=count, data=data)

@app.route("/idol<id>")
def idol(id):
	return render_template(
		"base_idol.html",
		icon=data[int(id)]['photo'],
		name=data[int(id)]['name'],
		subcount=data[int(id)]['subscriber_count'],
		viewcount=data[int(id)]['view_count'],
		yt=data[int(id)]['yt_channel_id'],
		twt=data[int(id)]['twitter_link']
	)

if __name__ == "__main__":
	app.run(debug=True)