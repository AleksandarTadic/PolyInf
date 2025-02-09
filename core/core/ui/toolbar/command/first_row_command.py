from .interface_command import ICommand

class FirstRowCommand(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.first_row()