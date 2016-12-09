from substack.data.logger import logger
from substack.plugins.base.plugin import Plugin


class PortPlugin(Plugin):
    def __init__(self):
        Plugin.__init__(self)

    def get_type(self):
        return "port"

    def scan(self, domain):
        open_ports = self.real_scan(domain)
        return open_ports

    def real_scan(self, domain):
        msg = 'Plugin is not implementing required method real_scan'
        raise NotImplementedError(msg)
