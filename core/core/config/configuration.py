import json

class Configuration:
    def __init__(self, title, core_version, icon, window_size, plugins_path="plugins", context_path="resources/data/context.json"):
        self.title = title
        self.core_version = core_version
        self.icon = icon
        self.window_size = window_size

        self.plugins_path = plugins_path
        self.context_path = context_path

    @property
    def width(self):
        return self.window_size["width"]
    
    @property
    def height(self):
        return self.window_size["height"]
    @property
    def maximized(self):
        return self.window_size["maximized"]
    
    @staticmethod
    def from_dict(configuration_dict):
        title = configuration_dict.get("title", "")
        core_version = configuration_dict.get("core_version", "")
        icon = configuration_dict.get("icon", "")
        window_size = configuration_dict.get("window_size", {" width": 600, "height": 500, "maximized": False})
        plugins_path = configuration_dict.get("plugins_path", "plugins")
        context_path = configuration_dict.get("context_path", "resources/data/context.json")

        return Configuration(title, core_version, icon, window_size, plugins_path, context_path)
    
    @staticmethod
    def load_configuration():
        config_path = "resources/data/configuration.json"
        with open(config_path, "r", encoding="UTF-8") as file:
            config_data = json.load(file)
            try:
                config = Configuration.from_dict(config_data)
            except Exception as e:
                print(e)
            return config

    def save_configuration(self, main_window):
        config_path = "resources/data/configuration.json"
        self.window_size["width"] = main_window.frameGeometry().width()
        self.window_size["height"] = main_window.frameGeometry().height()
        self.window_size["maximized"] = main_window.isMaximized()
        json_object = json.dumps(self.to_dict(), indent=4)
        with open(config_path, "w", encoding="UTF-8") as file:
            file.write(json_object)

    def to_dict(self):
        return {
            "title": self.title,
            "core_version": self.core_version,
            "icon": self.icon,
            "window_size": {
                "width": self.width,
                "height": self.height,
                "maximized": self.maximized
            },
            "plugins_path": self.plugins_path,
            "context_path": self.context_path
        }