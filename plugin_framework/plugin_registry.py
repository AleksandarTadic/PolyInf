import os
import inspect
import importlib
import json
from plugin_framework.plugin_specification import PluginSpecification

class PluginRegistry:
    def __init__(self, path, iface, activated_plugins=[], plugins=[]):
        self.path = path # folder
        self.iface = iface # interface (main_window)
        self.activated_plugins = activated_plugins
        self._plugins = plugins
        # FIXME: premesteno je da se instalira spram putanje
        # kasnije se putanje izvlace iz konfiguracije
        self.init_plugins()

    def install(self, plugin):
        exsists = self._check_existing_plugin(plugin.plugin_specification.id)
        if not exsists:
            # FIXME: nisu proverene zavisnosti
            self._plugins.append(plugin)

    def uninstall(self, plugin):
        # FIXME: sta se radi sa zavisnostima
        self.deactivate(plugin.plugin_specification.id)
        self._plugins.remove(plugin)
        # FIXME: obrisati folder koji se nalazi u plugin-s

    def activate(self, _id):
        for plugin in self._plugins: # plugin # naslednica od extension
            if _id == plugin.plugin_specification.id:
                plugin.activate()
                if _id not in self.activated_plugins:
                    self.activated_plugins.append(_id)


    def deactivate(self, _id):
        for plugin in self._plugins: # plugin # naslednica od extension
            if _id == plugin.plugin_specification.id:
                plugin.deactivate()
                if _id in self.activated_plugins:
                    self.activated_plugins.remove(_id)


    def install_from_path(self, path=""):
        if path == "":
            path = self.path
        if os.path.exists(path):
            # TODO: ako putanja nije u okviru plugin foldera, kopirati sadrzaj u njega
            # (zbog relativnih importa)
            package_name = os.path.basename(path)
            print("Package name:", package_name)
            package_path = os.path.join(self.path, package_name)
            print("Package path", package_path)
            plugin_path = os.path.join(package_path, "plugin.py") # Po dogovoru glavni deo plugin-a cuvamo u plugin.py
            spec_path = os.path.join(package_path, "specification.json") # specifikacija svakog plugina ce se nalaziti
            # u ovoj dateoteci
            with open(spec_path) as fp:
                data = json.load(fp)
            specification = PluginSpecification.from_dict(data)
            # dinamicko ucitavanje modula
            plugin = importlib.import_module(plugin_path.replace(os.path.sep, ".").rstrip(".py"))
            clsmembers = inspect.getmembers(plugin_path, inspect.isclass)
            print(clsmembers)
            if len(clsmembers) == 1:
                plugin = plugin.Plugin(specification, self.iface) # unutar modula ce postojati tacno jedna klasa koju cemo
                # zvati Plugin
                # instalacija plugin-a
                self.install(plugin)
            else:
                raise IndexError("The plugin.py module must contain just one class!")
        else:
            # putanja nije dobra
            raise FileNotFoundError("Plugin doesn't exist on specified path!")

    def init_plugins(self):
        """
        Loads all plugins from path.
        """
        plugins_packages = os.listdir(self.path)
        for package in plugins_packages:
            package_path = os.path.join(self.path, package)
            plugin_path = os.path.join(package_path, "plugin.py") # Po dogovoru glavni deo plugin-a cuvamo u plugin.py
            spec_path = os.path.join(package_path, "specification.json") # specifikacija svakog plugina ce se nalaziti
            # u ovoj dateoteci

            data = {}
            with open(spec_path) as fp:
                data = json.load(fp)
            specification = PluginSpecification.from_dict(data)
            # dinamicko ucitavanje modula
            plugin = importlib.import_module(plugin_path.replace(os.path.sep, ".").rstrip(".py"))
            clsmembers = inspect.getmembers(plugin_path, inspect.isclass)
            # print(clsmembers)
            if len(clsmembers) == 1:
                plugin = plugin.Plugin(specification, self.iface) # unutar modula ce postojati tacno jedna klasa koju cemo
                # zvati Plugin
                # instalacija plugin-a
                self.install(plugin)
            else:
                raise IndexError("The plugin.py module must contain just one class!")
        for plugin_id in self.activated_plugins:
            self.activate(plugin_id)


    def _check_existing_plugin(self, _id):
        """
        Checks if plugin with _id is already in plugin list.
        """
        for plugin in self._plugins:
            if plugin.plugin_specification.id == _id:
                return True
        return False
    