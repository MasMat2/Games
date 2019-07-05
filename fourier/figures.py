import pygame, sys, math


class arrow:
    def __init__(self, start, end, win_size):
        self.length = int(
            math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
        )
        self.start = start
        self.end = end
        self.angle = math.atan2((start[1] - end[1]), (end[0] - start[0]))
        self.width = self.length // 100
        self.window_width, self.window_height = win_size

    def rotate(self, x, y):
        r_x = x * math.cos(self.angle) - y * math.sin(self.angle)
        r_y = y * math.cos(self.angle) + x * math.sin(self.angle)
        return (r_x + self.start[0], -r_y + self.start[1])

    def create(self, angle=None):
        self.angle = self.angle + angle if angle else self.angle
        triang_side = 2 * ((self.length // 10) / (3 ** (1 / 2)))
        self.head = [
            self.rotate(self.length, 0),
            self.rotate(self.length * 9 // 10, triang_side // 2),
            self.rotate(self.length * 9 // 10, -triang_side // 2),
        ]
        self.body = [
            self.rotate(0, -self.width),
            self.rotate(0, self.width),
            self.rotate(self.length * 9 // 10, self.width),
            self.rotate(self.length * 9 // 10, -self.width),
        ]
        return self.head, self.body


class main:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

        self.arrow = arrow((256, 256), (300, 300), self.size)
        self.head, self.body = self.arrow.create(math.pi)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        pygame.draw.polygon(self._display_surf, (0, 250, 250), self.head)
        pygame.draw.polygon(self._display_surf, (0, 250, 250), self.body)
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

