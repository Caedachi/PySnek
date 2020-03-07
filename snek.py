class Snek:
    def __init__(self, start_y, start_x):
        self.head = Sneklet(start_y, start_x, 1)
        self.body = [self.head]
    
    def consume_food(self, y, x):
        self.head = Sneklet(y, x, len(self.body) + 1)
        self.body.append(self.head)
    
    def move(self, y, x):
        self.head = Sneklet(y, x, len(self.body))
        self.tick()
        self.body.append(self.head)

    def get_head(self):
        return self.head 

    def get_body(self):
        return self.body

    def get_illegal_moves(self):
        return set([_.get_position() for _ in self.get_body()])

    def tick(self):
        for sneklet in self.body:
            sneklet.tick()
        
        for i, sneklet in enumerate(self.body):
            if sneklet.get_remaining_ticks() == 0:
                self.body.pop(i)


class Sneklet:
    def __init__(self, y, x, ticks):
        self.y = y
        self.x = x
        self.ticks = ticks

    def get_position(self):
        return (self.y, self.x)

    def get_remaining_ticks(self):
        return self.ticks

    def tick(self):
        self.ticks -= 1
