import json as JSON
import requests
import xbmc


class API:
    BASE_API = "https://skipptv.nastream.fr"
    TMDB_DATAS_ENDPOINT = "/byTmdbIdAndDatas/{}/{}/{}"
    TITLE_ENDPOINT = "/byTitle/{}"

    def __init__(self):
        pass

    def getByTmdbIdAndDatas(self, tmdbid, season, episode):
        api_url = self.BASE_API + self.TMDB_DATAS_ENDPOINT.format(tmdbid, season, episode)
        response = requests.get(api_url)
        print(response.json())
        return response.json()

    def getByTitle(self, title):
        api_url = self.BASE_API + self.TITLE_ENDPOINT.format(title)
        response = requests.get(api_url)
        print(response.json())
        return response.json()
