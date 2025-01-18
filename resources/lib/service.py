import xbmc
import xbmcaddon
import xbmcgui

class SkippTvService:
    def __init__(self):
        self.addon = xbmcaddon.Addon()
        print("Initialisation du service SkippTv")

    def log(self, message):
        xbmc.log(f"[SkippTV] {message}", level=xbmc.LOGINFO)

    def send_notification(self, title, message):
        xbmcgui.Dialog().notification(title, message, icon=self.addon.getAddonInfo('icon'), time=5000)

    def convert_timecode_to_seconds(self, timecode):
        # Séparer les heures, minutes et secondes
        parts = timecode.split(':')
        hours, minutes, seconds = map(int, parts)
        # Convertir en secondes
        return hours * 3600 + minutes * 60 + seconds