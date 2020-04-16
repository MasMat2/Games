import pygame, sys, math, time

# Create rolling surface
# Create vector
class Vector:
    def __init__(self, magnitude, direction):
        self.set_magnitude(magnitude)
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction

    def set_magnitude(self, magnitude):
        self.magnitude = magnitude

    def get_x(self):
        return math.cos(self.direction) * self.magnitude

    def get_y(self):
        return math.sin(self.direction) * self.magnitude

    def add_vector(self, vector):
        x = self.magnitude * math.cos(self.direction) + vector.magnitude * math.cos(
            vector.direction
        )
        y = self.magnitude * math.sin(self.direction) + vector.magnitude * math.sin(
            vector.direction
        )
        self.magnitude = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        self.direction = math.atan2(y, x)


# Create ball
class Ball_Physics:
    def __init__(self, surface):
        self.radius = 10
        self.color = (0, 100, 250)
        self.gravity = Vector(0.1, 3 * math.pi / 2)
        self.acceleration = Vector(0, 0)
        self.surface = surface
        self.position = [self.surface.get_width() // 2, 0]

    def move(self):
        self.position[0] += self.acceleration.get_x()
        self.position[1] += self.acceleration.get_y()

    def fall(self):
        self.acceleration.add_vector(self.gravity)

    def touch(self, n):
        medium_angle = 0
        for j in range(2):
            for i in range(n):
                angle = (math.pow(-1, j)) * (i / float(n)) * math.pi * 2
                x = (self.radius - 1) * math.cos(angle) + self.position[0]
                y = (self.radius - 1) * math.sin(angle) + self.position[1]
                try:
                    if self.surface.get_at((int(x), -int(y))) not in [
                        (0, 0, 0),
                        self.color,
                    ]:
                        print(angle % (math.pi * 2))
                        medium_angle += angle % (math.pi * 2)
                        if j:
                            return medium_angle / 2
                        else:
                            break
                except IndexError:
                    pass
        return False

    def bounce(self, angle):
        self.acceleration.magnitude *= 1
        self.acceleration.direction = -angle

    def check_collision(self):
        angle = self.touch(100)
        if angle:
            self.bounce(angle)

    def update(self):
        self.check_collision()
        self.fall()
        self.move()

    def translate_position(self):
        return (int(self.position[0]), -int(self.position[1]))


class Ball(Ball_Physics):
    def __init__(self, surface):
        super().__init__(surface)


class main:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = (512, 512)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, 0, 32)
        self._display_surf
        self._running = True
        self.ball = Ball(self._display_surf)
        self.ball.update()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        pygame.draw.polygon(
            self._display_surf,
            (0, 250, 100),
            (
                (0, self.size[1] - 400),
                (self.size[0], self.size[1] - 200),
                (self.size[0], self.size[1]),
                (self.size[0], self.size[1]),
                (0, self.size[1]),
            ),
        )
        pygame.draw.circle(
            self._display_surf,
            self.ball.color,
            self.ball.translate_position(),
            self.ball.radius,
            0,
        )
        pygame.display.update()
        self.ball.update()

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
