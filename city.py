import random
from collections import deque


class CityGrid:
    def __init__(
        self, n: int, m: int, coverage_threshold: float, tower_radius: int
    ) -> None:
        """
        Инициализация сетки города.

        Parameters:
        - n (int): Количество строк в сетке.
        - m (int): Количество столбцов в сетке.
        - coverage_threshold (float): Порог покрытия для случайного заполнения блоков.
        - tower_radius (int): Радиус действия башни.
        """
        self.n = n
        self.m = m
        self.grid = [[0 for _ in range(m)] for _ in range(n)]
        self.tower_radius = tower_radius

        self.populate_randomly(coverage_threshold)

    def populate_randomly(self, coverage_threshold: float) -> None:
        """
        Заполнение сетки блоками случайным образом.

        Parameters:
        - coverage_threshold (float): Порог покрытия для случайного заполнения блоков.
        """
        for i in range(self.n):
            for j in range(self.m):
                if random.random() < coverage_threshold:
                    self.grid[i][j] = 1  # Заблокированный блок
                else:
                    self.grid[i][j] = 0  # Доступный блок

    def optimize_towers(self) -> None:
        """
        Оптимизация расположения башен в сетке.
        """
        while True:
            best_block = None
            best_coverage = 0

            for i in range(self.n):
                for j in range(self.m):
                    if self.grid[i][j] == 0 or self.grid[i][j] == 3:
                        coverage = self.evaluate_coverage(i, j, self.tower_radius)
                        if coverage > best_coverage:
                            best_block = (i, j)
                            best_coverage = coverage

            if best_block is not None:
                i, j = best_block
                self.place_tower(i, j, self.tower_radius)
            else:
                break

    def evaluate_coverage(self, i: int, j: int, tower_radius: int) -> int:
        """
        Оценка, сколько блоков может охватить башня.

        Parameters:
        - i (int): Координата строки башни.
        - j (int): Координата столбца башни.
        - tower_radius (int): Радиус действия башни.

        Returns:
        - int: Количество блоков, которые может охватить башня.
        """
        coverage = 0
        tower_counter = 0

        def is_tower(x, y):
            return self.grid[x][y] == 2

        def is_available(x, y):
            return self.grid[x][y] == 0

        if not self.get_tower_coordinates():
            tower_counter = 1

        for x in range(max(0, i - tower_radius), min(self.n, i + tower_radius + 1)):
            for y in range(max(0, j - tower_radius), min(self.m, j + tower_radius + 1)):
                if is_tower(x, y):
                    tower_counter += 1
                elif is_available(x, y):
                    coverage += 1

        if tower_counter == 0:
            coverage = 0

        return coverage

    def place_tower(self, i: int, j: int, tower_radius: int) -> bool:
        """
        Размещение башни с учетом радиуса действия.

        Parameters:
        - i (int): Координата строки башни.
        - j (int): Координата столбца башни.
        - tower_radius (int): Радиус действия башни.

        Returns:
        - bool: True, если башню удалось разместить, иначе False.
        """
        if not self.is_block_available(i, j):
            return False  # Нельзя разместить башню на заблокированном блоке

        self.grid[i][j] = 2  # Символ для башни

        for x in range(max(0, i - tower_radius), min(self.n, i + tower_radius + 1)):
            for y in range(max(0, j - tower_radius), min(self.m, j + tower_radius + 1)):
                if self.grid[x][y] == 0:
                    self.grid[x][y] = 3  # Символ для радиуса действия

        return True

    def is_block_available(self, i: int, j: int) -> bool:
        """
        Проверка доступности блока в сетке.

        Parameters:
        - i (int): Координата строки блока.
        - j (int): Координата столбца блока.

        Returns:
        - bool: True, если блок доступен, иначе False.
        """
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.grid[i][j] in {0, 3}
        return False

    def distance(self, block1: tuple, block2: tuple) -> int:
        """
        Расстояние между двумя блоками.

        Parameters:
        - block1 (tuple): Координаты первого блока (i, j).
        - block2 (tuple): Координаты второго блока (i, j).

        Returns:
        - int: Расстояние между блоками.
        """
        i1, j1 = block1
        i2, j2 = block2
        return abs(i1 - i2) + abs(j1 - j2)

    def get_tower_coordinates(self) -> list:
        """
        Получение координат всех башен в сетке.

        Returns:
        - list: Список координат башен.
        """
        tower_coordinates = []
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 2:
                    tower_coordinates.append((i, j))
        return tower_coordinates

    def find_all_shortest_paths(self) -> dict:
        """
        Поиск всех кратчайших путей между башнями в сетке.

        Returns:
        - dict: Словарь, содержащий кратчайшие пути между парами башен.
        """
        tower_coordinates = self.get_tower_coordinates()
        paths = {}

        for i, start in enumerate(tower_coordinates):
            paths[start] = {}
            for j, end in enumerate(tower_coordinates):
                if i != j:
                    path = self.find_shortest_path(start, end)
                    if path:
                        paths[start][end] = path

        return paths

    def find_shortest_path(self, start: tuple, end: tuple) -> list:
        """
        Поиск кратчайшего пути между двумя блоками в сетке.

        Parameters:
        - start (tuple): Координаты начального блока (i, j).
        - end (tuple): Координаты конечного блока (i, j).

        Returns:
        - list: Кратчайший путь в виде списка координат блоков.
        """
        queue = deque([(start, [])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == end:
                return path

            if current not in visited:
                visited.add(current)
                neighbors = self.get_neighbors_within_radius(current, self.tower_radius)
                for neighbor in neighbors:
                    queue.append((neighbor, path + [current]))

        return None

    def get_neighbors_within_radius(self, position: tuple, radius: int) -> list:
        """
        Получение координат соседей в пределах радиуса действия.

        Parameters:
        - position (tuple): Координаты центрального блока (i, j).
        - radius (int): Радиус действия.

        Returns:
        - list: Список координат соседей.
        """
        i, j = position
        neighbors = []

        for x in range(max(0, i - radius), min(self.n, i + radius + 1)):
            for y in range(max(0, j - radius), min(self.m, j + radius + 1)):
                if self.grid[x][y] == 2:
                    neighbors.append((x, y))

        return neighbors
