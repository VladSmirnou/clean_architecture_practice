from use_cases.dto.input_dto import InputDto, InputDtoRetrieve
from infrastructure.flask_app.interfaces.controller_interface import \
    IFlaskController
from use_cases.interfaces.use_case_interface import I_InputBoundary


# Такое ощущение, что этот контроллер здесь лишний, т.к.
# приходится роутить реквест еще раз. Скорее всего надо
# просто вызывать use_cases прямо с роутов или как-то еще, но
# пока оставлю так.
class FlaskController(IFlaskController):
    use_case_obj: I_InputBoundary

    def __init__(self, use_case: I_InputBoundary) -> None:
        self.use_case_obj = use_case

    def process_data(self, data: dict) -> dict:
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
