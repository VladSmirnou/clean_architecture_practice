from pydantic import BaseModel


class InputDto(BaseModel):
    number_one: int
    number_two: int
    operator: str

    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


class InputDtoRetrieve(BaseModel):
    amount_of_results: int
    tail_or_head_flag: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
