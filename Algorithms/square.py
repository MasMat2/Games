import pygame, sys, time

vertex = {}

for i in range(4):
    for j in range(4):
        con = []
        if i>0:
            con += [(i-1,j)]
        if i<3:
            con += [(i+1,j)]
        if j>0:
            con += [(i,j-1)]
        if j<3:
            con += [(i,j+1)]
        vertex[(i,j)] = (con)

paths = []
def recur(point, path):
    if point == (0,0):
        paths.append(path)
        return 0
    for i in vertex[point]:
        if i not in path:
            recur(i, list(path)+[(i)])
    return None

recur((3,3), [(3,3)])

print(len(paths))
def draw(surface, path):
    top, left = 60,60
    f = (left+3*60, top+3*60)
    for point in path:
        end = (left + point[0]*60, top + point[1]*60)
        pygame.draw.line(surface, (0,0,255), f, end)
        f = end
class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True
        self.path = (path for path in paths)
        self.lazt_path = None
        self.go = 1

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.KEYDOWN:
            self.go = 1
            if event.key == pygame.K_SPACE:
                self.go = 1

    def on_loop(self):
        if self.go:
            self.lazt_path = next(self.path)

    def on_render(self):
        if self.go:
            self._display_surf.fill((0,0,0))
            draw(self._display_surf, self.lazt_path)
            pygame.display.update()
            self.go = 0

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
