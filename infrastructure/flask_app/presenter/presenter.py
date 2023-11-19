from use_cases.interfaces.presenter_interface import IOutputBoundary
from use_cases.dto.output_dto import OutputDto


class FlaskPresenter(IOutputBoundary):
    def present(self, output_dto: OutputDto) -> dict:
        return {'response': output_dto.output}
