from dataclasses import dataclass
from typing import TypeVar, Generic
import datetime


T = TypeVar("T")


@dataclass(frozen=True)
class OutputDto(Generic[T]):
    output: T
    date: datetime.date = datetime.date.today()
