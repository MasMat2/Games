import pygame, random, sys


class Draw:
    def __init__(self, size, frag):
        self.size = size
        self.rect_width = self.size[0] / 100.0
        self.rect_height = self.size[1] / 100.0
        self.frag = frag
        self.lenght = [0] * self.frag
        self.square = [0] * self.frag

    def new_line(self):
        return random.random()

    def new_square(self, lenght):
        return lenght ** 2

    def create_squares(self, tests):
        for i in range(tests):
            lenght = self.new_line()
            square = self.new_square(lenght)
            self.lenght[int(lenght * self.frag)] += 1
            self.square[int(square * self.frag)] += 1

    def get_odds(self, odd):
        limit = int(odd * 100)
        acum = 0
        for i in range(limit):
            acum += self.square[i]
        acum1 = 0
        for i in range(self.frag):
            acum1 += self.square[i]
        return acum / acum1

    def draw(self, surface, pos, frequency, color):
        pygame.draw.rect(
            surface,
            color,
            (
                pos,
                self.size[1] - frequency * self.rect_height,
                self.rect_width,
                frequency * self.rect_height,
            ),
        )


class main:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)
        self.draw = None
        self.frag = 100

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.draw = Draw(self.size, self.frag)

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        tests = 5000
        pos = 0
        self.draw.create_squares(tests)
        rect_width = self.size[0] // self.frag
        for i in range(self.frag):
            self.draw.draw(self._display_surf, pos, self.draw.lenght[i], (0, 100, 255))
            self.draw.draw(self._display_surf, pos, self.draw.square[i], (0, 255, 100))
            pos += rect_width
        self.draw.draw(self._display_surf, rect_width * 50, 100, (100, 0, 255))
        pygame.display.update()
        print(self.draw.get_odds(0.25))

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        self.on_loop()
        self.on_render()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = main()
    theApp.on_execute()
