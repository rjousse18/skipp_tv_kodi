from resources.lib.service import SkippTvService
import xbmc

if __name__ == '__main__':
    skippTvService = SkippTvService()
    monitor = xbmc.Monitor()


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
                                final_endpoint = (
                                    f"https://skipptv.nastream.fr/byTitle/{title.lower().replace(' ', '_')}_"
                                    f"{str(season).zfill(2)}_{str(episode).zfill(2)}"
                                )
                                if tmdbid != "-1":
                                    final_endpoint = (
                                        f"https://skipptv.nastream.fr/byTmdbIdAndDatas/{tmdbid}/"
                                        f"{season}/{episode}"
                                    )
                                skippTvService.log(f"Final endpoint: {final_endpoint}")
                                # self.send_notification("Final endpoint", final_endpoint)
                            else:
                                skippTvService.log("Impossible de récupérer le titre de la série")
                        else:
                            skippTvService.log("Impossible de récupérer les détails de l'épisode.")
                except Exception as e:
                    skippTvService.log(f"Erreur en récupérant les informations vidéo : {str(e)}")
                while player.isPlaying():
                    xbmc.sleep(500)

