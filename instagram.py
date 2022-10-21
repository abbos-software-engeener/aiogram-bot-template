
import json
import requests


def instadownloader(link1):

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link1}

    headers = {
		"X-RapidAPI-Key": "bed6c00b1bmshe7c84a926f67cb7p1fd048jsndac77f352b66",
		"X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
	}

    response = requests.request("GET", url, headers=headers, params=querystring)
    rest = json.loads(response.text)

    if 'error' in rest:
        return 'Bad'
    else:
        dict = {}
        if rest['Type'] == 'Post-Image':
            dict['type'] = 'image'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Post-Video':
            dict['type'] = 'video'
            dict['media'] = rest['media']
            return dict
        elif rest['Type'] == 'Carousel':
            dict['type'] = 'carousel'
            dict['media'] = rest['media']
            return dict
        else:
            return 'Bad'
# instadownloader("https://www.instagram.com/reel/Cj2ZqO9oZDK/?igshid=MDJmNzVkMjY=")