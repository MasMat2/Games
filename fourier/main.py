import pygame, sys, math
from figures import *


class sine_func:
    def __init__(self):
        self.t = 0
        self.x = 1
        self.y = 0

    def update(self, x_scale=190, frequency=3):
        self.t += math.pi * 2 / (x_scale / frequency)
        self.x = math.cos(self.t) * radius
        self.y = math.sin(self.t) * radius
    
    def normal(self):
        return int(self.x), int(-self.y)
    
    def polar(self):
        return self.y, self.t


class sine_wave:
    def __init__(self, size):
        self.width, self.height = size
        self.points = [start_y]

    def update(self, new_point):
        self.points = [new_point] + self.points
        if len(self.points) > start_x * (n_x - 1) - 60:
            self.points = self.points[0 : start_x * (n_x - 1) - 60]

    # draw sine wave through joined
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


class compact_grid:
    def __init__(self):
        x, y = 47, 350
        width = 200
        self.grid = grid((0, 100, 100), (x, y), 20, width)
        self.arrow = rot_arrow((255, 255, 255), (x + width // 2, y + width // 2), 0, 0)

    def update(self, normal):
        module, argument = normal
        self.arrow.move(module, argument)

    def draw(self, surface):
        self.grid.draw(surface)
        self.arrow.draw(surface)


class compact_wave(sine_wave):
    def __init__(self, size):
        super().__init__(size)
        top, bottom, left, right = start_y - radius,start_y + radius, start_x, start_x * n_x - 60
        self.ruler = [
            ruler(
                (255, 255, 255),
                (left, bottom),
                (right, bottom),
                4,
                True,
            ),
            arrow(
                (255, 255, 255),
                (left, bottom),
                (right, bottom),
            ),
        ]
        self.ruler1 = [
            ruler(
                (255, 255, 255),
                (left, bottom),
                (left, top),
                2,
            ),
            arrow(
                (255, 255, 255),
                (left, bottom),
                (left, top),
            ),
        ]
        self.rulers = (self.ruler, self.ruler1)

    def update(self, normal):
        real, imag = normal
        self.real = real + start_x - radius * 2
        self.imag = imag + start_y
        super().update(self.imag)

    def draw(self, surface):
        pygame.draw.circle(
            surface, (200, 200, 2), (start_x - radius * 2, start_y), radius, 1
        )
        pygame.draw.circle(surface, (200, 2, 200), (self.real, self.imag), 5)
        pygame.draw.line(
            surface, (200, 2, 200), (self.real, self.imag), (start_x, self.imag)
        )
        super().draw(surface)
        for ruler, arrow in self.rulers:
            ruler.draw(surface)
            arrow.draw(surface)


size = (1025, 700)
n_x = 5
start_x = size[0] // n_x
n_y = 4
start_y = size[1] // n_y
radius = 50

ruler_measure = 4
unit_length = (start_x * (n_x - 1) - 60) // ruler_measure

func =sine_func()

class main:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = size

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True
        self.compact_grid = compact_grid()
        self.compact_wave = compact_wave(self.size)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        func.update(unit_length, frequency=3)
        self.compact_grid.update(func.polar())
        self.compact_wave.update(func.normal())

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.compact_grid.draw(self._display_surf)
        self.compact_wave.draw(self._display_surf)
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
