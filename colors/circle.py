import pygame, sys, math, random


class vortex:
    def __init__(self):
        self.angle = math.pi
        self.radius = 50

    def draw(self, surface, color, pos):
        self.center = pos
        speed = 0.5
        for i in range(100):
            if self.radius > 0.01:
                start = self.center[0]+self.radius*math.cos(self.angle), self.center[1]-self.radius*math.sin(self.angle)
                self.radius -= 0.5
                self.angle += speed
                end = self.center[0]+(self.radius)*math.cos(self.angle), self.center[1]-(self.radius)*math.sin(self.angle)
                pygame.draw.line(surface, color, start, end)


class circle:
    def __init__(self, center=(0,0), radius=100):
        self.center = center
        self.radius = radius
        self.top = self.center[1]-self.radius
        self.left = self.center[0]-self.radius

    def update_pos(self):
        self.center = pygame.mouse.get_pos()
        self.top = self.center[1]-self.radius
        self.left = self.center[0]-self.radius


    def inscrit(self, pos):
        self.update_pos()
        x, y = pos
        distance = ((self.center[0]-x)**2+(self.center[1]-y)**2)**(1/2)
        if distance<self.radius:
            angle = math.atan2((y-self.center[1]), (x-self.center[0]))
            enter = (self.center[0]+self.radius*math.cos(angle), self.center[1]+self.radius*math.sin(angle))
            out = (self.center[0]+self.radius*math.cos(angle+math.pi), self.center[1]+self.radius*math.sin(angle+math.pi))
            return (enter, out)
        return False

    def draw(self, surface, color, pos):
        x, y = pos
        self.vortex = vortex()
        angle = math.atan2((y-self.center[1]), (x-self.center[0]))
        pygame.draw.arc(surface, color, [self.left,self.top,self.radius*2,self.radius*2], -angle, -angle+math.pi+0.01)
        self.vortex.draw(surface, color, self.center)


class lines:
    def __init__(self):
        if random.choice([True, False]):
            self.x = random.random()*512
            self.y = random.choice([0,512])
        else:
            self.x = random.choice([0,512])
            self.y = random.random()*512
        if self.x in [0,512]:
            self.angle = random.random()*math.pi + abs(self.x-1)/(self.x-1)*math.pi/2
        else:
            self.angle =  abs(self.y-1)/(self.y-1)*random.random()*math.pi
        self.empty = 1
        self.speed = 10
        # for i in range(10):
            # angle = random.random()*2*math.pi
            # angle2 = random.random()*2*math.pi
            # angle, angle2 = math.pi/4, math.pi/4
            # z = math.sin(angle2)
            # y = math.cos(angle2)*math.sin(angle)
            # x = math.cos(angle2)*math.cos(angle)
            # print(math.atan2(1/3, (2/3)**(1/2))/math.pi)
            # print(math.pi/4)
            # print(x, y, z)
        angle = random.random()*2*math.pi
        angle2 = random.random()*2*math.pi
        z = math.sin(angle2)
        y = math.cos(angle2)*math.sin(angle)
        x = math.cos(angle2)*math.cos(angle)
        self.color = (x**2*255,y**2*255,z**2*255)
        self.color = [int(random.random()*255) for i in range(3)]
        self.linestop = 512*(2**(1/2))//self.speed
        self.lines = [(self.x, self.y),]

    def inside(self, pos):
        if pos[0]>512 or pos[0]<0:
            return False
        if pos[1]>512 or pos[1]<0:
            return False
        return True


    def move(self, circle):
        if self.inside(self.lines[0]):
            if len(self.lines)>self.linestop:
                self.lines.pop(0)
            self.x += self.speed*math.cos(self.angle)
            self.y -= self.speed*math.sin(self.angle)
            new = circle.inscrit((self.x, self.y))
            if new and self.empty:
                self.lines.append(list(new[0]))
                self.lines.append(new[1])
                self.x, self.y = new[1]
                self.empty = False
            else:
                self.lines.append((self.x, self.y))
            return False
        return True

    def draw(self, surface, circle):
        for i in range(len(self.lines)-1):
            color = [(i/self.linestop)*colori for colori in self.color]
            # color = self.color
            if type(self.lines[i]) == type([]):
                circle.draw(surface, color, self.lines[i])
            else:
                pygame.draw.line(surface, color, self.lines[i], self.lines[i+1])

class main:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0 , 32)
        self._running = True
        self.lines = [lines() for i in range(10)]
        self.circle = circle((200,200))
        self._display_surf.fill((0,0,0))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.lines += [lines()]
        for line in self.lines:
            if line.move(self.circle):
                self.lines.remove(line)

    def on_render(self):
        self._display_surf.fill((0,0,0))
        for line in self.lines:
            line.draw(self._display_surf, self.circle)
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
