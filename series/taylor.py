import pygame, sys, time, math

height, width = 512, 512
lenght = 1

def f(x):
    rx = 0
    for i in range(lenght//100):
        rx += ((-1)**(i%2)*(x**(i*2)))/math.factorial(i*2)
    k = lenght//100
    rx += (((-1)**(k%2)*(x**(k*2)))/math.factorial(k*2))*(lenght%100)/100
    return rx


def draw(surface, func, color):
    last = None
    for x in range(width):
        y = func((x-width//2)/16)*16
        if last:
            pygame.draw.line(surface, color, last, (x, height//2-y))
            last = (x, height//2-y)
        else:
            last = (x, height//2-y)


class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (height, width)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        #
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     self.blobs.touch(event.pos)
        #     self.render = -math.inf
        #
        # if event.type == pygame.MOUSEBUTTONUP:
        #     self.blobs.select()
        #     self.render = 0
        #
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RETURN:
        #         self.blobs.ch_mode(1)
        #         self.render = 0



    def on_loop(self):
        pass

    def on_render(self):
        global lenght
        self._display_surf.fill((0,0,0))
        draw(self._display_surf, math.cos, (0,250,100))
        draw(self._display_surf, f, (0, 255, 255))
        lenght += 1
        pygame.display.update()
        print(lenght)

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while ( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theThing = main()
    theThing.on_execute()
