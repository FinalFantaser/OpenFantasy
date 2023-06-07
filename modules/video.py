from modules.module import Module
import sys
import sdl2.ext

class Video(Module):
    def init(self, config: dict = (), params: dict = ()):
        self.info('Метод init')

        sdl2.ext.init()
        self.window = sdl2.ext.Window(
            title='OpenFantasy',
            size=(
                int(config['video']['resolution_width']),
                int(config['video']['resolution_height']),
            )
        )