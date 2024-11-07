from .command import Command
import pynvim

@pynvim.plugin
class NeovimSpotify:
    def __init__(self, nvim):
        self.nvim = nvim
        self.cmd = Command(nvim)

    @pynvim.command("Spotify", sync=True)
    def hello_world(self):
        self.nvim.out_write("Hello, World!\n")

