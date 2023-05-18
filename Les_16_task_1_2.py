# Урок N16. Классы и объекты
#
# Задание N1. Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# ● top_up(X) -пополнить на X
# ● count_1000() -выводит сколько целых тысяч осталось в кассе
# ● take_away(X) -забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

# class Cashbox:
#
# 	def __init__(self, nums=5000):
# 		self.nums = nums
# 	def top_up(self, X):
# 		return f"Итог пополнения: {self.nums + X}"
#
# 	def count_1000(self):
# 		return f"Целых тысяч: {self.nums / 1000}"
#
# 	def take_away(self, X):
# 		if self.nums < X:
# 			return f"Недостаточно денег"
# 		return f"Останется: {self.nums - X}"
#
# h1 = Cashbox(1200)
# print(h1.top_up(3000))
# print(h1.count_1000())
# print(h1.take_away(1000))


# Задание N2. Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s -количество
# клеточек, на которое она перемещается за ход, у этого класс есть методы:
# ● go_up() - увеличивает y на s
# ● go_down() - уменьшает y на s
# ● go_left() - уменьшает x на s
# ● go_right() - увеличивает y на s
# ● evolve() - увеличивает s на 1
# ● degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# ● count_moves(x2, y2) -возвращает минимальное количество действий, за которое
# черепашка сможет добраться до x2 y2 от текущей позиции

# ● count_moves(x2, y2) -возвращает минимальное количество действий, за которое
# черепашка сможет добраться до x2 y2 от текущей позиции

from collections import deque
class Turtle:
    x = 0
    y = 0
    s = 5

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.x -= self.s

    def go_left(self):
        self.x += self.s

    def go_right(self):
        self.y -= self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s < 0:
            return 'error'
        self.s -= 1

    def count_moves(self, x2, y2):
        queue = deque([(self.x, self.y, 0)])  # очередь для BFS
        visited = set([(self.x, self.y)])  # множество посещенных вершин

        while queue:
            x, y, moves = queue.popleft()
            if x == x2 and y == y2:
                return moves

            # генерация соседних вершин
            neighbors = [(x + self.s, y), (x - self.s, y),
                         (x, y + self.s), (x, y - self.s)]

            for nx, ny in neighbors:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))

        return -1  # если путь не найден

turtle = Turtle()
turtle.count_moves(10, 10)