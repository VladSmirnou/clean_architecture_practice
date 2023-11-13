from use_cases.use_case import UseCase
from use_cases.dto.input_dto import InputDto, InputDtoRetrieve
from use_cases.interfaces.cli_repo_interface import I_InMemoryRepository
from use_cases.interfaces.cli_presenter_interface import IOutputBoundary
from infrastructure.cli_app.interfaces.controller_interface import ICliController


class CliController(ICliController):
    use_case_obj: UseCase

    def __init__(self,
                 presenter: IOutputBoundary,
                 repository: I_InMemoryRepository) -> None:
        self.use_case_obj = UseCase(
            presenter=presenter,
            repository=repository
        )

    def process_data(self, data: dict) -> str:
        match data:
            case {'amount_of_results': _, 'tail_or_head_flag': _}:
                return self.use_case_obj.retrieve_prev_calculations(
                    input_dto=InputDtoRetrieve.from_dict(data)
                )
            case {'save': bool(), **rest}:
                return self.use_case_obj.calculate_result_and_save(
                    input_dto=InputDto.from_dict(rest)
                )
            case _:
                return self.use_case_obj.calculate_result(
                    input_dto=InputDto.from_dict(data)
                )
