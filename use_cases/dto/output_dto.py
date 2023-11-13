from dataclasses import dataclass


@dataclass
class OutputDto:
    output: int | dict
