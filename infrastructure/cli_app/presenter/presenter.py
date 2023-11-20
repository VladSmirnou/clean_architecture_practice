from use_cases.dto.output_dto import OutputDto
from infrastructure.cli_app.templates.templates import templates
from use_cases.interfaces.presenter_interface import IOutputBoundary
from infrastructure.cli_app.interfaces.view_interface import ICliView


class CliPresenter(IOutputBoundary):
    cli_view_obj: ICliView

    def __init__(self, cli_view_obj: ICliView) -> None:
        self.cli_view_obj = cli_view_obj

    def present(self, output_dto: OutputDto) -> dict:
        # Не знаю, как убрать зависимость от типа 'output' тут.
        # Видимо что-то не так где-то сделал изначально.
        # Cоздавать use_case и прокидывать разные
        # презентеры, вью и т.д. для каждого роута отдельно мне кажется
        # слишком медленно. Даже с таким маленьким приложением уже видна
        # задержка в доли секунды при его запуске из-за создания всех объектов.
        match output_dto.output:
            case int(value):
                return {
                    'response': self.cli_view_obj.render(
                        templates['single_value_res'], {'output': value}
                    )
                }
            case list(res_list):
                return {
                    'response': self.cli_view_obj.render(
                        templates['list_res'], {
                            'output': str(res_list)
                        }
                    )
                }
            case _: raise ValueError
