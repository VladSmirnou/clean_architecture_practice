from use_cases.interfaces.cli_presenter_interface import IOutputBoundary
from use_cases.dto.output_dto import OutputDto
from infrastructure.cli_app.interfaces.view_interface import ICliView


class CliPresenter(IOutputBoundary):
    cli_view_obj: ICliView

    def __init__(self, cli_view_obj: ICliView) -> None:
        self.cli_view_obj = cli_view_obj

    def present(self, output_dto: OutputDto) -> str:
        match output_dto:
            case OutputDto(output=int(value)):
                return self.cli_view_obj.render(
                    'The result is: %(output)d', {'output': value}
                )
            case OutputDto(output=dict()):
                result_list = [f'{key} = {val}' for key, val in output_dto.output.items()]
                return self.cli_view_obj.render(
                    'You saved results: %(output)s', {'output': str(result_list)}
                )
