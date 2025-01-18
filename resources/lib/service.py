import time
import xbmc
import xbmcaddon

class SkippTvService:
    def __init__(self):
        print("Initialisation du service SkippTv")

    def log(self, message):
        xbmc.log(f"[SkippTV] {message}", level=xbmc.LOGINFO)