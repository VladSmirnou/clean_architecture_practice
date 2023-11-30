from use_cases.dto.input_dto import InputDtoRetrieve
from use_cases.interfaces.get_saved_results_interface import \
    GetSavedResultInterface
from infrastructure.flask_app.interfaces.\
    get_saved_result_controller_interface import \
    GetSavedResultControllerInterface


class GetSavedResultController(GetSavedResultControllerInterface):
    use_case_obj: GetSavedResultInterface

    def __init__(self, use_case: GetSavedResultInterface) -> None:
        self.use_case_obj = use_case

    def process_data(self, data: dict) -> dict:
        return self.use_case_obj.retrieve_prev_calculations(
                input_dto=InputDtoRetrieve.from_dict(data)
            )
