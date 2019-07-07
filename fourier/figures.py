import pygame, sys, math


class arrow:
    def __init__(self, start, end):
        self.length = int(
            math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
        )
        self.start = start
        self.end = end
        self.angle = math.atan2((start[1] - end[1]), (end[0] - start[0]))
        self.width = self.length // 100

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


class grid:
    def __init__(self, color, start, width, size):
        self.color = color
        self.vertical = [
            ((i, start[0]), (i, start[0] + size))
            for i in range(start[0], start[0] + size + width, width)
        ]
        self.horizontal = [
            ((start[1], i), (start[1] + size, i))
            for i in range(start[1], start[1] + size + width, width)
        ]

    def draw(self, surface):
        for i in self.vertical + self.horizontal:
            pygame.draw.line(surface, self.color, i[0], i[1])


class ruler:
    def __init__(self, color, start, end, measure):
        if abs(math.atan2((start[1] - end[1]), (end[0] - start[0]))) not in [
            math.pi,
            0,
            math.pi / 2,
            math.pi * 3 / 2,
        ]:
            raise IndexError
        self.color = color
        self.measure = measure
        self.start = start
        self.end = end
        self.length = int(
            math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
        )

    def draw(self, surface):
        myfont = pygame.font.SysFont("Andale Mono.ttf", 15)
        pygame.draw.line(surface, self.color, self.start, self.end)
        count = 0
        if self.start[1] == self.end[1]:
            for i in range(self.start[0], self.end[0] + 1, self.length // self.measure):
                pygame.draw.line(
                    surface, self.color, (i, self.start[1] - 5), (i, self.start[1] + 5)
                )
                textsurface = myfont.render(str(count), False, self.color)
                textRect = textsurface.get_rect()
                textRect.center = (i, self.start[1] + 15)
                surface.blit(textsurface, textRect)
                count += 1
        else:
            for i in range(self.start[1], self.end[1] + 1, self.length // self.measure):
                pygame.draw.line(
                    surface, self.color, (self.start[1] - 5, i), (self.start[1] + 5, i)
                )
                textsurface = myfont.render(str(count), False, self.color)
                textRect = textsurface.get_rect()
                textRect.center = (self.start[1] + 15, i)
                surface.blit(textsurface, textRect)
                count += 1


class main:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

        self.ruler = ruler((255, 255, 255), (250, 250), (300, 250), 2)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.on_cleanup()

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.ruler.draw(self._display_surf)
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

