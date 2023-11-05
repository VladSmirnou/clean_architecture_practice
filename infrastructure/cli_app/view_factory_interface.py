from abc import ABC, abstractmethod
from infrastructure.cli_app.view_interface import ICliView


class IViewFactory(ABC):
    @abstractmethod
    def make_view(self) -> ICliView: ...
