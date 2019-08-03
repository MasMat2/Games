import pygame, sys, math


class arrow:
    def __init__(self, color, start, end):
        self.color = color
        self.length = int(
            math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
        )
        self.start = start
        self.end = end
        self.angle = math.atan2((start[1] - end[1]), (end[0] - start[0]))
        self.width = 0

    def rotate(self, x, y):
        r_x = x * math.cos(self.angle) - y * math.sin(self.angle)
        r_y = y * math.cos(self.angle) + x * math.sin(self.angle)
        return (r_x + self.start[0], -r_y + self.start[1])

    def create(self, angle=None):
        triang_height = 10
        self.angle = self.angle + angle if angle else self.angle
        triang_side = 2 * ((triang_height) / (3 ** (1 / 2)))
        self.head = [
            self.rotate(self.length + triang_height, 0),
            self.rotate(self.length, triang_side // 2),
            self.rotate(self.length, -triang_side // 2),
        ]
        self.body = [self.rotate(0, 0), self.rotate(self.length, 0)]

    def draw(self, surface, angle=0):
        self.create(angle)
        pygame.draw.polygon(surface, self.color, self.head)
        pygame.draw.line(surface, self.color, self.body[0], self.body[1])


class grid:
    def __init__(self, color, start, separation, size):
        self.color = color
        self.vertical = [
            ((i, start[1]), (i, start[1] + size))
            for i in range(start[0], start[0] + size + separation, separation)
        ]
        self.horizontal = [
            ((start[0], i), (start[0] + size, i))
            for i in range(start[1], start[1] + size + separation, separation)
        ]
        print(start)

    def draw(self, surface):
        for i in self.vertical + self.horizontal:
            pygame.draw.line(surface, self.color, i[0], i[1])


class ruler:
    def __init__(self, color, start, end, measure, mid_lines=False):
        if abs(math.atan2((start[1] - end[1]), (end[0] - start[0]))) not in [
            math.pi,
            0,
            math.pi / 2,
            math.pi * 3 / 2,
        ]:
            raise IndexError
        self.color = color
        self.start = start
        self.end = end
        self.measure = measure
        self.mid_lines = mid_lines
        self.length = int(
            math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)
        )
        self.unit_length = self.length // (self.measure)

    def get_unit_length(self):
        return self.unit_length

    def draw(self, surface):
        mid_line = 4 if self.mid_lines else 1
        myfont = pygame.font.SysFont("", 15)
        pygame.draw.line(surface, self.color, self.start, self.end)
        count = 0
        if self.start[1] == self.end[1]:
            for i in range(
                self.start[0], self.end[0] + 1, self.length // (self.measure * mid_line)
            ):
                pygame.draw.line(
                    surface, self.color, (i, self.start[1] - 5), (i, self.start[1] + 5)
                )
                if count % mid_line == 0:
                    textsurface = myfont.render(
                        str(count // mid_line), False, self.color
                    )
                    textRect = textsurface.get_rect()
                    textRect.center = (i, self.start[1] + 15)
                    surface.blit(textsurface, textRect)
                count += 1
        else:
            if self.end[1] + 1 < self.start[1]:
                direction = -1
            else:
                direction = 1
            for i in range(
                int(self.start[1]),
                int(self.end[1] + direction),
                direction * self.length // (self.measure * mid_line),
            ):
                pygame.draw.line(
                    surface, self.color, (self.start[0] - 5, i), (self.start[0] + 5, i)
                )
                if count % mid_line == 0:
                    textsurface = myfont.render(
                        str(count // mid_line), False, self.color
                    )
                    textRect = textsurface.get_rect()
                    textRect.center = (self.start[0] - 15, i)
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

