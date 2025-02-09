from .interface_command import ICommand

class PromoteSubtableCommand(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.promote_subtable()