import turtle


class Snake:
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    MOVE_DISTANCE = 20

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.segments = []
        self.refresh()

    def refresh(self):
        print("Snake reset")
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()

        self.segments = []
        self.add_segment(self.start_x, self.start_y)
        self.head = self.segments[0]
        self.direction = None

    def add_segment(self, x, y):
        t = turtle.Turtle("square")
        t.hideturtle()
        t.penup()
        t.speed(0)
        t.goto(x, y)
        t.color("red")
        t.showturtle()
        self.segments.append(t)

    def extend(self):
        self.add_segment(1000, 1000)

    def key_up(self):
        self.direction = Snake.UP

    def key_down(self):
        self.direction = Snake.DOWN

    def key_left(self):
        self.direction = Snake.LEFT

    def key_right(self):
        self.direction = Snake.RIGHT

    def move(self):
        head_x = self.head.xcor()
        head_y = self.head.ycor()

        if self.direction == Snake.UP:
            head_y += Snake.MOVE_DISTANCE
        if self.direction == Snake.DOWN:
            head_y -= Snake.MOVE_DISTANCE
        if self.direction == Snake.LEFT:
            head_x -= Snake.MOVE_DISTANCE
        if self.direction == Snake.RIGHT:
            head_x += Snake.MOVE_DISTANCE

        index = len(self.segments) - 1
        while index > 0:
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
            index -= 1

        self.head.goto(head_x, head_y)

    def check_self_collision(self):
        for seg in self.segments:
            if seg == self.head:
                continue
            elif self.head.distance(seg) < 20:
                return True

        return False

    def check_walls_collision(self, screen_width, screen_height):
        half_width = screen_width / 2
        half_height = screen_height / 2
        x = self.head.xcor()
        y = self.head.ycor()

        if x > half_width or x < -half_width or y > half_height or y < -half_height:
            return True
        else:
            return False
