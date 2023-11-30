from use_cases.dto.input_dto import InputDto
from use_cases.interfaces.calculate_result_interface import \
    CalculateResultInterface
from infrastructure.cli_app.interfaces.\
    calculate_result_controller_interface import \
    CalculateResultControllerInterface


class CalculateResultController(CalculateResultControllerInterface):
    use_case_obj: CalculateResultInterface

    def __init__(self, use_case: CalculateResultInterface) -> None:
        self.use_case_obj = use_case

    def process_data(self, data: dict) -> dict:
        return self.use_case_obj.calculate_result(
            input_dto=InputDto.from_dict(data)
        )
