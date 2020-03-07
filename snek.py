class Snek:
    def __init__(self, start_y, start_x):
        self.head = Sneklet(start_y, start_x)
        self.body = [self.head]
    
    def consume_food(self, y, x):
        self._extend_snek(y, x)
    
    def move(self, y, x):
        self.body.pop(0)
        self._extend_snek(y, x)
    
    def _extend_snek(self, y, x):
        self.head = Sneklet(y, x)
        self.body.append(self.head)

    def get_head(self):
        return self.head

    def get_body(self):
        return self.body

    def get_tail(self):
        return self.body[0]

    def get_illegal_moves(self):
        # omit the tail of the body to allow nipping at the tail
        return set([_.get_position() for _ in self.get_body()[1:]])


class Sneklet:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def get_position(self):
        return (self.y, self.x)
