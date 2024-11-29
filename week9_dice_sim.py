# 3rd party modules
import pygal as pg
from pygal.style import Style

# Import custom modules
from week9_dice import Die


def main():
    # Create dice
    die1: Die = Die(20)
    die2: Die = Die(20)

    # Simulate rolling and adding the results
    number_of_rolls: int = 1000000

    results: list = []
    for roll in range(number_of_rolls):
        result = die1.roll() + die2.roll()
        results.append(result)

    # Analyze the results from the rolls - key(sum): value(frequency)
    counts: dict = {}
    max_result: int = die1.get_sides() + die2.get_sides()
    for sum_value in range(2, max_result + 1):
        counts[sum_value] = results.count(sum_value)

    # Create a graph of the results using pygal
    # Colors for graph
    my_style: Style = Style(
        colors = ("red",),
        background = "blue",
        plot_blackground="white",
        foreground="red",
        foreground_strong="white",
        foreground_subtle="blue",

    )

    # Create a graph of the results using pygal
    graph: pg.Bar = pg.Bar(style=my_style)
    graph.title = f"Results of Rolling Two {die1.get_sides()}-side Dice {number_of_rolls} Times"

    graph.x_labels = counts.keys()
    graph.x_title = "Results"
    graph.y_title = "Frequency"
    graph.add("Sum", counts.values())

    graph.render_to_file("dice_sim.svg")


if __name__ == "__main__":
    main()