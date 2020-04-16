import pygame, sys, random, math, time


def a(arc):
    for i in range(part):
        x = int(center_x+radius*math.cos(angle*i/part))
        y = int(center_y-radius*math.sin(angle*i/part))
        if last:
            pygame.draw.line(surface, (0,0,255), last, (x,y))
        else:
            pygame.draw.line(surface, (0,0,255), (x,y), (x,y))
        last = (x,y)

class cycle:
    def __init__(self, pos, surface):
        self.center_x, self.center_y = pos[0], pos[1]
        self.start_angle = random.random()*2*math.pi
        self.angle = 20*math.pi
        self.radius = 200
        self.part = int(self.angle*200/math.pi)
        self.radiusm = self.radius/self.part
        self.cycle = 0
        self.last = None
        self.surface = surface

    def arc(self):
        self.last = None
        self.radius = 200
        for i in range(self.part):
            x = int(self.center_x+self.radius*math.cos(self.start_angle+self.angle*i/self.part))
            y = int(self.center_y-self.radius*math.sin(self.start_angle+self.angle*i/self.part))
            self.radius -= self.radiusm
            if self.last:
                if i< self.part:
                    pygame.draw.line(self.surface, (0,0,255), self.last, (x,y))
            self.last = (x,y)




class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True
        self.cycle = cycle((256,256), self._display_surf)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.cycle.start_angle += 0.1

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.cycle.arc()
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
