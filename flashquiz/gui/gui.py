import pygame


class GUI:
    def __init__(self, opts):
        self.screen, self.clock = None, None
        self.window_name = opts.title
        self.dimensions = (opts.w, opts.h)
        self.FPS = opts.fps

    def reset_clock(self):
        self.clock = pygame.time.Clock()

    def init_screen(self):
        pygame.init()
        self.reset_clock()
        self.screen = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption(self.window_name)
        return self

    def handle_events(self):
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                return False
        return True

    def refresh(self):
        self.clock.tick(self.FPS)
        pygame.display.update()

    @staticmethod
    def quit():
        pygame.quit()
