
import os
import logging
from optparse import OptionParser

import pyglet
from pyglet import gl

# resources setup
DATA_PATH = os.path.join(os.path.abspath(pyglet.resource.get_script_home()), 'data')
pyglet.resource.path.append(DATA_PATH)
pyglet.resource.reindex()

from game.const import APP_NAME, PROJECT_DESC, PROJECT_URL, VERSION, WIDTH, HEIGHT, AUDIO_DRIVERS

class Main(pyglet.window.Window):
    def __init__(self):

        # pyglet setup
        pyglet.options['audio'] = AUDIO_DRIVERS
        pyglet.options['debug_gl'] = False

        parser = OptionParser(description="%s: %s" % (APP_NAME, PROJECT_DESC),
                              epilog='Project website: %s' % PROJECT_URL,
                              version='%prog ' + VERSION,
                              )
        parser.add_option("-f", "--fullscreen",
                          dest="fullscreen",
                          default=False,
                          action="store_true",
                          )
        parser.add_option("-d", "--debug",
                          dest="debug",
                          default=False,
                          action="store_true",
                          )
        self.options, args = parser.parse_args()

        if self.options.debug:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug("Debug enabled")
            logging.debug("Options: %s" % self.options)

        super(Main, self).__init__(width=WIDTH,
                                   height=HEIGHT,
                                   caption=APP_NAME,
                                   visible=True,
                                   )

        if self.options.fullscreen:
            self.set_fullscreen(True)

        # uncomment if you wan to hide the mouse pointer
        # self.set_mouse_visible(False)

        # display FPS on debug
        if self.options.debug:
            self.fps = pyglet.window.FPSDisplay(self)

        # set 60 FPS
        pyglet.clock.schedule_interval(self.update, 1.0/60)
        pyglet.clock.set_fps_limit(60)

        # enable alpha blending (transparent color)
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

        # set a key state handler
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)

        # will be set to True if 'p' is pressed
        self.paused = False

        # game setup
        self.label = pyglet.text.Label("Hello pyglet!",
                                       font_name="Times New Roman",
                                       font_size=14,
                                       anchor_x="center",
                                       anchor_y="center",
                                       )
        self.c = 0

    def update(self, dt):
        """Update game state"""

        # this is an example; don't update the state if paused
        if self.paused:
            return

        self.c += 1
        if self.c > 255:
            self.c = 0
        self.label.color = (self.c, self.c, self.c, 255)

    def on_resize(self, width, height):
        """Calculate the new viewport preserving aspect ratio"""

        aspect = float(WIDTH)/HEIGHT

        self.viewport_width = int(min(width, height*aspect))
        self.viewport_height = int(min(height, width/aspect))
        self.viewport_x_offs = (width-self.viewport_width) // 2
        self.viewport_y_offs = (height-self.viewport_height) // 2

        x = (width-WIDTH) / 2
        gl.glViewport(self.viewport_x_offs,
                      self.viewport_y_offs,
                      self.viewport_width,
                      self.viewport_height,
                      )
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, self.viewport_width, 0, self.viewport_height, -1, 1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity()

        logging.debug("Viewport: %s, %s, %s, %s" % (self.viewport_x_offs,
                                                    self.viewport_y_offs,
                                                    self.viewport_width,
                                                    self.viewport_height,
                                                    ))

        # adjust elements depending on the new viewport
        self.label.x = self.viewport_width // 2
        self.label.y = self.viewport_height // 2

    def on_key_press(self, symbol, mods):
        """
        Enhanced default key press handler.

            - Remove the default handler when not debugging, disables escape -> close
            - P set/uset pause flag
            - CRTL + s save a screenshot
            - CTRL + f toggle fullscreen
        """

        if self.options.debug:
            super(Main, self).on_key_press(symbol, mods)

        if symbol == pyglet.window.key.P:
            self.paused = not self.paused
            logging.debug("Paused: %s" % self.paused)
        elif mods == pyglet.window.key.MOD_CTRL and symbol == pyglet.window.key.S:
            filename = os.path.join(os.path.abspath(pyglet.resource.get_script_home()),
                                                    "screenshot%s.png" % pyglet.clock.tick())
            pyglet.image.get_buffer_manager().get_color_buffer().save(filename)
            logging.debug("Screenshot saved: %s" % filename)
        elif mods == pyglet.window.key.MOD_CTRL and symbol == pyglet.window.key.F:
            self.options.fullscreen = not self.options.fullscreen
            self.set_fullscreen(self.options.fullscreen)
            logging.debug("Fullscreen: %s" % self.options.fullscreen)

    def on_draw(self):
        """Draw the scene"""

        self.clear()

        # draw your elements
        self.label.draw()

        if self.paused:
            # you may want to do something
            pass

        if self.options.debug:
            self.fps.draw()

