from resources.lib.service import SkippTvService
from resources.lib.gui import SkipButtonDialog
from resources.lib.api import API
import xbmc
import xbmcaddon

if __name__ == '__main__':
    addon = xbmcaddon.Addon()
    skippTvService = SkippTvService()
    monitor = xbmc.Monitor()
    api = API()

    while not monitor.abortRequested():
            # Sleep/wait for abort for 10 seconds
            if monitor.waitForAbort(10):
                # Abort was requested while waiting. We should exit
                break
            
            # Vérifie si un événement de lecture commence
            player = xbmc.Player()
            if player.isPlaying():
                print("Playback detected. Waiting for media info...")

                try:
                    # Récupère les informations sur le média
                    media_type = player.getVideoInfoTag().getMediaType()
                    print(f"Media type detected: {media_type}")

                    if media_type == "episode":
                        # Récupère les informations détaillées sur la vidéo
                        video_info = player.getVideoInfoTag()
                        season = video_info.getSeason()
                        episode = video_info.getEpisode()
                        tmdbid = xbmc.Player().getPlayingItem().getProperty("TmdbId") or "-1"

                        if season is not None and episode is not None:
                            title = video_info.getTVShowTitle()
                            if title is not None:
                                skippTvService.send_notification("SkippTv", "Épisode de série détecté, recherche...")
                                response_api = None
                                if tmdbid != "-1":
                                    response_api = api.getByTmdbIdAndDatas(tmdbid, season, episode)
                                else:
                                    response_api = api.getByTitle(title.lower().replace(' ', '_')+"_"+str(season).zfill(2)+"_"+str(episode).zfill(2))

                                if response_api is not None:
                                    timecode_start_in_seconds = skippTvService.convert_timecode_to_seconds(response_api['intro_start_at'])
                                    timecode_end_in_seconds = skippTvService.convert_timecode_to_seconds(response_api['intro_end_at'])
                                    while player.getTime() < timecode_start_in_seconds:
                                        skippTvService.log("Wait for intro start")
                                        xbmc.sleep(1000)
                                    dialog = SkipButtonDialog("DialogSkip.xml", addon.getAddonInfo("path"), "default", skip_time = timecode_end_in_seconds)
                                    dialog.doModal()
                                else:
                                    skippTvService.log("Pas de résultats")
                            else:
                                skippTvService.log("Impossible de récupérer le titre de la série")
                        else:
                            skippTvService.log("Impossible de récupérer les détails de l'épisode.")
                except Exception as e:
                    skippTvService.log(f"Erreur en récupérant les informations vidéo : {str(e)}")
                while player.isPlaying():
                    xbmc.sleep(500)

