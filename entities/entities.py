import operator
from typing import Callable


class Calculator:
    # Some business data ...

    # I don't rly know how to
    # generalize this operator choosing
    # mechanism because it comes as a str from the user.
    # I think that mapping is the best way to do that,
    # even tho this dict might grow in time.
    operator_mapping: dict[str, Callable] = {
        '+': operator.add,
        '-': operator.sub,
    }
    # -------------------------
    # Some critical business rules

    def perform_calculations(self,
                             operator: str,
                             number_one: int,
                             number_two: int) -> int:
        return self.operator_mapping[operator](number_one, number_two)
    # -------------------------
