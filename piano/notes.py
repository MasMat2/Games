import pygame, sys


class piano:

    def __init__(self, surface):
        self.counter = 0
        self.surface = surface
        self.ratio = 4/5
        self.limits = [int(self.ratio*x) for x in self.surface.get_size()]
        self.left, self.top = (int((1-self.ratio)*x/2) for x in self.surface.get_size())

        self.sound_gen = self.sound_gen()
        white = pygame.mixer.Sound('white.wav')

        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)

        # self.channel1.play(white, loops = -1)

    def sound_gen(self):
        sounds = 'do re mi fa sol la si'.split(' ')
        while True:
            for sound in sounds:
                yield pygame.mixer.Sound(sound + '.wav')

    def sounds(self):
        if self.counter % 60 == 0:
            self.channel2.play(next(self.sound_gen))
            self.counter = 0
        self.counter += 1

    def draw_keys(self):
        separation = self.limits[0]//7
        for i in range(7):
            rect = (i*separation+self.left,self.top, separation-1, 200)
            pygame.draw.rect(self.surface, (255,255,255), rect, 0)
        for i in range(6):
            width = 20
            if i == 2:
                continue
            rect = (separation*(i+1/2)+ self.left+width/2 ,self.top, separation-width, 100)
            pygame.draw.rect(self.surface, (0,0,0), rect, 0)




class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 256)

    def on_init(self):
        pygame.init()
        pygame.mixer.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True

        # do = pygame.mixer.Sound('do.mp3')
        # do.play()

        self.piano = piano(self._display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.piano.sounds()

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.piano.draw_keys()
        pygame.display.update()

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
    theApp = main()
    theApp.on_execute()
