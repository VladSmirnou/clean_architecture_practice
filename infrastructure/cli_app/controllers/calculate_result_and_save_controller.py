from use_cases.dto.input_dto import InputDto
from use_cases.interfaces.calculate_result_and_save_interface import \
    CalculateResultAndSaveInterface
from infrastructure.cli_app.interfaces.\
    calculate_result_and_save_conroller_interface import \
    CalculateResultAndSaveControllerInterface


# На данный момент эти контроллеры дублируют друг друга. Пока не понятно,
# является ли это 'true' или 'false' duplication, но, мне кажется,
# что они разойдутся в исполнении в будущем.
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
