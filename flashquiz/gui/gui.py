import pygame


class GUI:
    def __init__(self, opts):
        self.screen, self.clock = None, None
        self.window_name = opts.title
        self.dimensions = (opts.w, opts.h)

    def init_screen(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption(self.window_name)
