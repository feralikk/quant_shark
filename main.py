import argparse

from city import CityGrid
from visualizer import CityVisualizer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", type=int, default=10, help="Количество строк")
    parser.add_argument("-m", type=int, default=10, help="Количество столбцов")
    parser.add_argument(
        "--coverage_threshold", type=float, default=0.3, help="Порог покрытия"
    )
    parser.add_argument(
        "--tower_radius", type=int, default=3, help="Радиус действия башни"
    )

    args = parser.parse_args()

    n = args.n
    m = args.m
    coverage_threshold = args.coverage_threshold
    tower_radius = args.tower_radius

    city = CityGrid(n, m, coverage_threshold, tower_radius)

    city.optimize_towers()

    paths = city.find_all_shortest_paths()

    for start, end_dict in paths.items():
        for end, path in end_dict.items():
            print(
                f"Кратчайший путь между башней {start} и башней {end}: {path + [end]}"
            )

    visualizer = CityVisualizer(city)
    visualizer.visualize_grid()

    visualizer.visualize_towers()

    visualizer.visualize_paths(paths)
