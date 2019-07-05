import pygame, sys, math


class sine_wave:
    def __init__(self, size):
        self.t = 0
        self.width, self.height = size
        self.x = 1
        self.y = 0

    def update(self):
        self.t += math.pi * 2 / 60
        self.x = math.cos(self.t) * 50
        self.y = math.sin(self.t) * 50
        return (int(self.x + self.width // 2), int(-self.y + self.height // 2))


class main:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

        self.sine_wave = sine_wave(self.size)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        pygame.draw.circle(
            self._display_surf,
            (200, 200, 2),
            (self.size[0] // 2, self.size[1] // 2),
            50,
        )
        pygame.draw.circle(
            self._display_surf, (200, 2, 200), self.sine_wave.update(), 5
        )
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
