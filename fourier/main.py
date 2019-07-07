import pygame, sys, math
from figures import *


class sine_func:
    def __init__(self, size):
        self.width, self.height = size
        self.t = 0
        self.x = 1
        self.y = 0

    def update(self):
        self.t += math.pi * 2 / 180
        self.x = math.cos(self.t) * radius
        self.y = math.sin(self.t) * radius
        return (int(self.x + start_x - radius * 2), int(-self.y + start_y))


class sine_wave:
    def __init__(self, size):
        self.width, self.height = size
        self.points = [start_y]

    def update(self, new_point):
        self.points = [new_point] + self.points
        if len(self.points) > start_x * (n_x - 1):
            self.points = self.points[0 : start_x * (n_x - 1)]

    def draw(self, surface):
        x = start_x
        start = False
        for point in self.points:
            x += 1
            if not start:
                start = (x, point)
            else:
                end = (x, point)
                pygame.draw.line(surface, (200, 2, 200), start, end)
                start = end


class compact_wave(sine_wave):
    def __init__(self, size):
        super().__init__(size)
        self.ruler = ruler(
            (255, 255, 255),
            (start_x, start_y + radius * 1.2),
            (start_x * n_x - 62, start_y + radius * 1.2),
            20,
        )

    def draw(self, surface):
        super().draw(surface)
        self.ruler.draw(surface)


size = (1024, 700)
n_x = 5
start_x = size[0] // n_x
n_y = 4
start_y = size[1] // n_y
radius = 50


class main:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = size

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

        self.sine_func = sine_func(self.size)
        self.sine_wave = compact_wave(self.size)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.real, self.imag = self.sine_func.update()
        self.sine_wave.update(self.imag)

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        pygame.draw.circle(
            self._display_surf,
            (200, 200, 2),
            (start_x - radius * 2, start_y),
            radius,
            1,
        )
        pygame.draw.circle(self._display_surf, (200, 2, 200), (self.real, self.imag), 5)
        pygame.draw.line(
            self._display_surf,
            (200, 2, 200),
            (self.real, self.imag),
            (start_x, self.imag),
        )
        self.sine_wave.draw(self._display_surf)
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
    theApp = main()
    theApp.on_execute()
