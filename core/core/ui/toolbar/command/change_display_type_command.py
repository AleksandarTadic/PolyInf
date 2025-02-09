from .interface_command import ICommand

class ChangeDisplayTypeCommand(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.change_central_widget()