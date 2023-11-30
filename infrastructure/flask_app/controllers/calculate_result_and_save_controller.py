from use_cases.dto.input_dto import InputDto
from use_cases.interfaces.calculate_result_and_save_interface import \
    CalculateResultAndSaveInterface
from infrastructure.flask_app.interfaces.\
    calculate_result_and_save_controller_interface import \
    CalculateResultAndSaveControllerInterface


class CalculateResultAndSaveController(
    CalculateResultAndSaveControllerInterface
):
    use_case_obj: CalculateResultAndSaveInterface

    def __init__(self, use_case: CalculateResultAndSaveInterface) -> None:
        self.use_case_obj = use_case

    def process_data(self, data: dict) -> dict:
        return self.use_case_obj.calculate_result_and_save(
            input_dto=InputDto.from_dict(data)
        )
