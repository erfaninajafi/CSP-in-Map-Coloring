import argparse
from enum import Enum
from CSP import CSP
from Solver import Solver
from map_generator import generate_borders_by_continent
from graphics import draw
import random

class Continent(Enum):
    asia = "Asia"
    africa = "Africa"
    america = "America"
    europe = "Europe"

    def __str__(self):
        return self.value
    

def main():
    """
    Command-line arguments:
    - -m, --map: Specify the map to solve the coloring problem on. Must be one of [Asia, Africa, America, Europe].
    - -lcv, --lcv: Enable least constraint value (LCV) as an order-type optimizer.
    - -mrv, --mrv: Enable minimum remaining values (MRV) as an order-type optimizer.
    - -ac3, --arc-consistency: Enable arc consistency as a mechanism to eliminate the domain of variables achieving an optimized solution.
    - -ND, --Neighborhood-distance: The value determines the threshold for neighboring regions' similarity in color, with a default of 1 ensuring adjacent regions have distinct colors; increasing it, for instance to 2, extends this dissimilarity to the neighbors of neighbors.
    """
    parser = argparse.ArgumentParser(
        prog="Map Coloring",
        description="Utilizing CSP to solve map coloring problem",
    )

    parser.add_argument(
        "-m",
        "--map",
        type=Continent,
        choices=list(Continent),
        help="Map must be: [Asia, Africa, America, Europe]",
    )
    parser.add_argument(
        "-lcv",
        "--lcv",
        action="store_true",
        help="Enable least constraint value (LCV) as a order-type optimizer"
    )
    parser.add_argument(
        "-mrv",
        "--mrv",
        action="store_true",
        help="Enable minimum remaining values (MRV) as a order-type optimizer"
    )
    parser.add_argument(
        "-ac3",
        "--arc-consistency",
        action="store_true",
        help="Enable arc consistency as a mechanism to eliminate the domain of variables achieving an optimized solution"
    )
    parser.add_argument(
        "-ND",
        "--Neighborhood-distance",
        type=int,
        default=1,
        help="The value determines the threshold for neighboring regions' similarity in color, with a default of 1 ensuring adjacent regions have distinct colors; increasing it, for instance to 2, extends this dissimilarity to the neighbors of neighbors."
    )

    args = parser.parse_args()
    borders = generate_borders_by_continent(continent=str(args.map))
    
    "*** YOUR CODE HERE ***"

    csp = CSP()

    map = generate_borders_by_continent(continent=str(args.map))

    for country , neighbors in map.items():
        csp.add_variable(country , ["red" , "blue" ,"yellow" , "black"])
        for neighbor in neighbors:
            csp.add_constraint(lambda x, y: x != y, [country , neighbor])


    solver = Solver(csp)



    result = solver.backtrack_solver()

    # res = {country: color for country, color in result}
    assignments_number = csp.assignments_number

    draw(solution=result, continent=str(args.map), assignments_number=assignments_number)
    

if __name__ == '__main__':
    main()