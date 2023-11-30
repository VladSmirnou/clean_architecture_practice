from use_cases.calculate_result import CalculateResult
from use_cases.interfaces.presenter_interface import OutputBoundaryInterface
from use_cases.interfaces.calculate_result_and_save_interface import \
    CalculateResultAndSaveInterface
from use_cases.dto.input_dto import InputDto
from use_cases.dto.output_dto import OutputDto
from use_cases.interfaces.repo_interface import RepositoryInterface


class CalculateResultAndSave(CalculateResult, CalculateResultAndSaveInterface):
    repository: RepositoryInterface

    def __init__(self,
                 presenter: OutputBoundaryInterface,
                 repository: RepositoryInterface) -> None:
        super().__init__(presenter=presenter)
        self.repository = repository

    def calculate_result_and_save(self, input_dto: InputDto) -> dict:
        output: int = self.get_result(input_dto)
        self.repository.save_calculation(
            input_dto.to_dict() | {'output': output}
        )
        return self.presenter.present(OutputDto(output=output))
