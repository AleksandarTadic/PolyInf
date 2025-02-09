from .toolbar_builder import ToolbarBuilder

class StandardTextToolbarDirector:
    @staticmethod
    def construct(parent, invoker):
        return ToolbarBuilder(parent, invoker)\
            .set_spacer()\
            .set_combobox()\
            .set_spacer()\
            .get_result()