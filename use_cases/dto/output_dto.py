from dataclasses import dataclass
from typing import TypeVar, Generic


T = TypeVar("T")


@dataclass(frozen=True)
class OutputDto(Generic[T]):
    output: T
