import xbmc
import xbmcgui
import xbmcplugin

class SkippTv(xbmc.Monitor):
    def __init__(self):
        print("Launch skipp")
        super().__init__()
        self.player = xbmc.Player()

    def onPlayBackStarted(self):
        # Triggered when playback starts
        print("Hey SKIPP TV IS ON !!")
        # video_info = self.get_video_info()
        # if self.check_conditions(video_info):
        #     self.show_skip_button()

    # def get_video_info(self):
    #     # Retrieve current playing video information
    #     if self.player.isPlayingVideo():
    #         video_file = self.player.getPlayingFile()
    #         return xbmc.getInfoLabel('ListItem.Property(tagline)')  # Example of fetching tags
    #     return None

    # def check_conditions(self, video_info):
    #     # Add logic to check tags/conditions
    #     return "specific_tag" in video_info

    # def show_skip_button(self):
    #     dialog = xbmcgui.Dialog()
    #     if dialog.yesno("Skip Section", "Do you want to skip this section?"):
    #         self.skip_to(300)  # Skip to 5 minutes (300 seconds)

    # def skip_to(self, time):
    #     self.player.seekTime(time)