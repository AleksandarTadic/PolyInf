from .toolbar_builder import ToolbarBuilder

class TableToolbarDirector:
    @staticmethod
    def construct(parent, invoker):
        return ToolbarBuilder(parent, invoker)\
            .set_spacer()\
            .set_previous_page()\
            .set_spacer()\
            .set_first()\
            .set_spacer()\
            .set_delete()\
            .set_insert()\
            .set_spacer()\
            .set_last()\
            .set_spacer()\
            .set_next_page()\
            .set_spacer()\
            .get_result()