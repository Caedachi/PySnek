class Sneklet:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def get_position(self) -> tuple[int, int]:
        return (self.y, self.x)


class Snek:
    def __init__(self, start_y: int, start_x: int):
        self.head: Sneklet = Sneklet(start_y, start_x)
        self.body: list[Sneklet] = [self.head]
    
    def consume_food(self, y: int, x: int):
        self._extend_snek(y, x)
    
    def move(self, y: int, x: int):
        self.body.pop(0)
        self._extend_snek(y, x)
    
    def _extend_snek(self, y: int, x: int):
        self.head = Sneklet(y, x)
        self.body.append(self.head)

    def get_head(self) -> Sneklet:
        return self.head

    def get_body(self) -> list[Sneklet]:
        return self.body

    def get_tail(self) -> Sneklet:
        return self.body[0]

    def get_illegal_moves(self) -> set[tuple[int, int]]:
        # omit the tail of the body to allow nipping at the tail
        return set([_.get_position() for _ in self.get_body()[1:]])
