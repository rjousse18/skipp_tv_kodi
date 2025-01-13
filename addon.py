import time
import xbmc

class SkippTv(xbmc.Player):
    def __init__(self):
        print("Launch skipp")
        super(SkippTv, self).__init__()

    def onPlayBackStarted(self):
        # Triggered when playback starts
        print("Hey SKIPP TV IS ON !!")
        self.get_video_infos()
        # if self.check_conditions(video_info):
        #     self.show_skip_button()isPlayingVideo

    def get_video_infos(self):
        print("Je passe dans la fonction")
        print(self.isPlayingVideo())
        print(xbmc.Player().isPlayingVideo())
        # Retrieve current playing video information
        # if self.isPlayingVideo():
        video_info = self.getVideoInfoTag()
        print("slkdslkfjdskfjdslkj")
        print(video_info.__dict__)
            
    # def check_conditions(self, video_info):
    #     # Add logic to check tags/conditions
    #     return "specific_tag" in video_info

    # def show_skip_button(self):
    #     dialog = xbmcgui.Dialog()
    #     if dialog.yesno("Skip Section", "Do you want to skip this section?"):
    #         self.skip_to(300)  # Skip to 5 minutes (300 seconds)

    # def skip_to(self, time):
    #     self.player.seekTime(time)

skippTv = SkippTv()

if __name__ == '__main__':
    monitor = xbmc.Monitor()
    
    while not monitor.abortRequested():
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break
        if xbmc.Player().isPlayingVideo():
            print("hehehehehe playing video !")
            print(xbmc.Player().getVideoInfoTag().getTagLine())
            print(xbmc.Player().getVideoInfoTag().getDbId())
            print(xbmc.Player().getVideoInfoTag().getGenre())
            print(xbmc.Player().getVideoInfoTag().getIMDBNumber())
            print(xbmc.Player().getVideoInfoTag().getSeason())
            print(xbmc.Player().getVideoInfoTag().getEpisode())
        xbmc.log("hello addon! %s" % time.time(), level=xbmc.LOGDEBUG)
