import json

class AppContext:
    def __init__(self, activated_plugins=[], workspace_contexts=[]):
        self.activated_plugins = activated_plugins
        self.workspace_contexts = workspace_contexts

    @staticmethod
    def from_dict(context_dict):
        activated_plugins = context_dict.get("activated_plugins", [])
        workspace_contexts = context_dict.get("workspace_contexts", {})
        return AppContext(activated_plugins, workspace_contexts)
    
    @staticmethod
    def load_context(path):
        with open(path, "r", encoding="UTF-8") as file:
            context_data = json.load(file)
            try:
                context = AppContext.from_dict(context_data)
            except Exception as e:
                print(e)
            return context

    def save_context(self, main_window):
        config_path = "resources/data/context.json"
        self.activated_plugins = main_window.plugin_registry.activated_plugins
        self.workspace_contexts["TAB_WIDGETS"] = main_window.central_widget.get_tab_contexts()
        json_object = json.dumps(self.to_dict(), indent=4)
        with open(config_path, "w", encoding="UTF-8") as file:
            file.write(json_object)

    def to_dict(self):
        return {
            "activated_plugins": self.activated_plugins,
            "workspace_contexts": self.workspace_contexts
        }
