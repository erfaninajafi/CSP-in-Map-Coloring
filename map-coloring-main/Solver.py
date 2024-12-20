from collections import deque
from typing import Callable, List, Tuple
from CSP import CSP


class Solver(object):

    def __init__(self, csp: CSP, domain_heuristics: bool = False, variable_heuristics: bool = False, AC_3: bool = False) -> None:
        """
        Initializes a Solver object.

        Args:
            csp (CSP): The Constraint Satisfaction Problem to be solved.
            domain_heuristics (bool, optional): Flag indicating whether to use domain heuristics. Defaults to False.
            variable_heuristics (bool, optional): Flag indicating whether to use variable heuristics. Defaults to False.
            AC_3 (bool, optional): Flag indicating whether to use the AC-3 algorithm. Defaults to False.
        """
        self.domain_heuristic = domain_heuristics
        self.variable_heuristic = variable_heuristics
        self.AC_3 = AC_3
        self.csp = csp

        

    def backtrack_solver(self) -> List[Tuple[str, str]]:
        def consistent(x , y) : return True if x != y else False

        if self.csp.is_complete():
            return self.csp.assignments
        var = self.select_unassigned_variable()
        removed_color = {}
        for item in self.ordered_domain_value(var):
            if self.csp.is_consistent(var, item):

                if self.csp.assign(var, item):
                    if var in self.csp.var_constraints:
                        for neighbor in self.csp.var_constraints[var]:
                            removed_color[neighbor] = self.arc_reduce(var, neighbor[1], consistent(var , neighbor))
                            

                    if self.backtrack_solver():
                        return self.csp.assignments
                    

                self.csp.unassign([], var)

        return None

            
            


    def select_unassigned_variable(self) -> str:
        """
        Selects an unassigned variable using the MRV heuristic.

        Returns:
            str: The selected unassigned variable.
        """
        if self.variable_heuristic:
            return self.MRV()
        return self.csp.unassigned_var[0]
    

    def ordered_domain_value(self, variable: str) -> List[str]:
        """
        Returns a list of domain values for the given variable in a specific order.
        Args:
            variable (str): The name of the variable.
        Returns:
            List[str]: A list of domain values for the variable in a specific order.
        """
        # Function implementation goes here
        if self.domain_heuristic:
            return self.LCV(variable)
        return self.csp.variables[variable]

        

    def arc_reduce(self, x, y, consistent) -> List[str]:
        """
        Reduce the domain of variable x based on the constraints between x and y.
        Parameters:
        - x: The first variable.
        - y: The second variable.
        - consistent: A function that checks the consistency between two values.
        Returns:
        - The reduced domain of variable x if the domain is reduced, None otherwise.
        """
        "*** YOUR CODE HERE ***"
                


    def apply_AC3(self) -> List[Tuple[str, str]]:
        """
        Applies the AC3 algorithm to reduce the domains of variables in the CSP.
        Returns:
            A list of tuples representing the removed values from the domain of variables.
        """
        "*** YOUR CODE HERE ***"



    def MRV(self) -> str:
        """
        Selects the variable with the Minimum Remaining Values (MRV) heuristic.
        Returns:
            str: The variable with the fewest remaining values.
        """
        "*** YOUR CODE HERE ***"
        variables = []
        for unassigned_var in self.csp.unassigned_var:
            variables.append((unassigned_var, len(self.csp.variables[unassigned_var])))

        variables.sort(key=lambda var: var[1])
        return variables[0][0]


    def LCV(self, variable: str) -> List[str]:
        """
        Orders the values of a variable based on the Least Constraining Value (LCV) heuristic.

        Args:
            variable (str): The variable for which to order the values.

        Returns:
            List[str]: A list of values sorted based on the number of constraints they impose.
        """
        "*** YOUR CODE HERE ***"
        ordered_domain = []

        for color in self.csp.variables[variable]:
            counter = 0
            for y in self.csp.unassigned_var:   
                if (variable, y) in self.csp.constraints and color in self.csp.variables[y]:
                    counter += 1
            ordered_domain.append((color, counter))
        ordered_domain.sort(key=lambda var: var[1])
        return [value[0] for value in ordered_domain]
