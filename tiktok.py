
def tk(link):
	import requests
	import json

	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url": link}

	headers = {
		"X-RapidAPI-Key": "c0a036af42msh77e0b69d3927b52p136525jsn108b4b137199",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	result = response.text
	rest = json.loads(result)

	return {"video": rest['video'][0]}
