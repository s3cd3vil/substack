import importlib


class PluginFactory:
    """
    Thi class factory a plugin by their name, type, requester and kb
    """

    def __init__(self, plugin_name, plugin_type, requester, kb):
        self.plugin_name = plugin_name
        self.plugin_type = plugin_type
        self.requester = requester
        self.kb = kb

    def _get_plugin_file_name(self):
        """
        Find the plugin file name from plugin class name
        """
        return self.plugin_name[:-6].lower() + "_plugin"

    def create(self):
        """
        Create an instance of a plugin
        """
        try:
            module = "substack.plugins.%s.%s" % (self.plugin_type, self._get_plugin_file_name())
            plugin_class = getattr(importlib.import_module(module), self.plugin_name)
            instance = plugin_class()
            instance.set_requester(self.requester)
            instance.set_kb(self.kb)
            return instance
        except:
            return None
