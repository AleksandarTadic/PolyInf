from .interface_command import ICommand

class LastRowCommand(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.last_row()