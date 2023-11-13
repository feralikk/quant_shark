import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

from city import CityGrid

GRID_FILENAME = "city_vizualize/city_grid.png"
TOWERS_FILENAME = "city_vizualize/city_towers.png"
PATHS_FILENAME = "city_vizualize/city_paths.png"

class CityVisualizer:
    def __init__(self, city: CityGrid) -> None:
        """
        Инициализация объекта CityVisualizer.

        Parameters:
        - city: Объект CityGrid, представляющий город.
        """
        self.city = city

    def visualize_grid(self) -> None:
        """
        Визуализация сетки города.
        """
        grid = np.array(self.city.grid)

        # Определение своей цветовой карты
        colors = ["black", "blue", "red", "white"]
        cmap = ListedColormap(colors)

        plt.imshow(grid, cmap=cmap, interpolation="nearest")

        # Добавление границ для каждой ячейки
        for i in range(self.city.n + 1):
            plt.axhline(i - 0.5, color="black", linewidth=1)

        for j in range(self.city.m + 1):
            plt.axvline(j - 0.5, color="black", linewidth=1)

        plt.title("City Grid")
        plt.xlabel("Columns")
        plt.ylabel("Rows")

        plt.savefig(GRID_FILENAME)

    def visualize_towers(self) -> None:
        """
        Визуализация башен и радиуса действия.
        """
        tower_coordinates = self.city.get_tower_coordinates()

        for i, j in tower_coordinates:
            plt.scatter(j, i, c="red", marker="x", label="Towers")

            # Ограничиваем координаты радиуса в пределах размеров сетки
            x_start = max(0, j - self.city.tower_radius)
            x_end = min(self.city.m - 1, j + self.city.tower_radius)
            y_start = max(0, i - self.city.tower_radius)
            y_end = min(self.city.n - 1, i + self.city.tower_radius)

            square = plt.Rectangle(
                (x_start, y_start),
                x_end - x_start,
                y_end - y_start,
                color="blue",
                fill=False,
                linestyle="dashed",
                linewidth=2,
            )
            plt.gca().add_patch(square)

        plt.title("City Grid with Towers and Coverage Radius (Square)")
        plt.xlabel("Columns")
        plt.ylabel("Rows")

        plt.savefig(TOWERS_FILENAME)

    def visualize_paths(self, paths: dict) -> None:
        """
        Визуализация путей между башнями.

        Parameters:
        - paths: Словарь путей между башнями.
        """
        # Используем разные цвета для разных путей
        path_colors = plt.cm.rainbow(np.linspace(0, 1, len(paths)))

        for (start, end_dict), color in zip(paths.items(), path_colors):
            for end, path in end_dict.items():
                plt.plot(
                    [path[0][1], path[-1][1]],
                    [path[0][0], path[-1][0]],
                    marker="o",
                    markersize=6,
                    linestyle="dashed",
                    color=color,
                )

                path_x, path_y = zip(*path)
                plt.plot(
                    path_y,
                    path_x,
                    marker=None,
                    markersize=6,
                    linewidth=2,
                    linestyle="dashed",
                    color=color,
                )

        plt.title("City Grid with Towers, Coverage Radius, and Paths")
        plt.xlabel("Columns")
        plt.ylabel("Rows")

        plt.savefig(PATHS_FILENAME)
