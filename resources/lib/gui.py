# import xbmcgui
# import xbmc

# class SkipModalDialog(xbmcgui.WindowDialog):
#     def __init__(self, skip_time, duration=10):
#         super().__init__()
#         self.duration = duration
#         self.skip_time = skip_time
#         self.setup_ui()

#     def setup_ui(self):
#         # Dimensions de la fenêtre
#         width, height = 300, 200
#         pos_x = (1280 - width) // 2  # Centré horizontalement
#         pos_y = (720 - height) // 2  # Centré verticalement
        
#         # Ajouter un fond
#         self.background = xbmcgui.ControlImage(pos_x, pos_y, width, height, "special://home/addons/skin.estuary/media/dialogs/dialog-bg.png")
#         self.addControl(self.background)

#         # Ajouter un bouton "Skip"
#         self.skip_button = xbmcgui.ControlButton(pos_x + 50, pos_y + 50, 200, 50, "Skip", alignment=0x00000001 | 0x00000010)
#         self.addControl(self.skip_button)
#         self.setFocus(self.skip_button)
    
#     def onControl(self, control):
#         if control == self.skip_button:
#             # Aller au timecode spécifié lorsque le bouton est cliqué
#             player = xbmc.Player()
#             if player.isPlaying():
#                 player.seekTime(self.skip_time)
#             self.close()


import xbmc
import xbmcgui
import xbmcaddon

class SkipButtonDialog(xbmcgui.WindowXMLDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.skip_time = kwargs.get('skip_time', 0)  # Temps en secondes pour le saut

    def onInit(self):
        self.getControl(2703).setLabel("Skip Intro")

    def onClick(self, controlId):
        if controlId == 2703:
            xbmc.Player().seekTime(self.skip_time)  # Passer au timecode
            self.close()  # Fermer la fenêtre

    def onAction(self, action):
        # Gérer les actions utilisateur (comme la fermeture avec Esc)
        if action == xbmcgui.ACTION_NAV_BACK:
            self.close()