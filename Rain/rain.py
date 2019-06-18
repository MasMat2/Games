import pygame, random, sys, copy, time
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)
COLORS = [BLUE, GREEN, YELLOW, PURPLE]


class Rain:
    def __init__(self):
        self.rain_drops = set()
        self.drops_copy = set()

    def new_drop(self, initial):
        self.rain_drops.add(initial)

    def draw(self, current_time):
        print(len(self.rain_drops), len(self.drops_copy))
        for i in self.rain_drops:
            y = int((100) * (current_time - i))
            theGame._display_surf.set_at((100, y), BLACK)
            if y > 254:
                self.drops_copy.add(i)
        for i in self.drops_copy:
            self.rain_drops.discard(i)
        self.drops_copy = set()


class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 254, 254

    def on_init(self):
        # Pygame parameters
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True
        self.time = time.time()
        self.new_drop_time = copy.deepcopy(self.time)
        self.rain = Rain()
        self.rain.rain_drops.add(time.time())

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        current_time = time.time()
        wall_time = current_time - self.time
        drop_time = current_time - self.new_drop_time

        if wall_time > (8 / 100):
            self.time = current_time
            self._display_surf.fill(WHITE)
            self.rain.draw(current_time)
            pygame.display.update()
        if drop_time > (1 / 10):
            self.new_drop_time = current_time
            self.rain.rain_drops.add(time.time())

    def on_render(self):
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theGame = Game()
    theGame.on_execute()
