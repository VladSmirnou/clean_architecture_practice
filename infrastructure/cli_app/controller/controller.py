from use_cases.dto.input_dto import InputDto, InputDtoRetrieve
from infrastructure.cli_app.interfaces.controller_interface import \
    ICliController
from use_cases.interfaces.use_case_interface import I_InputBoundary


class CliController(ICliController):
    use_case_obj: I_InputBoundary

    def __init__(self, use_case: I_InputBoundary) -> None:
        self.use_case_obj = use_case

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
