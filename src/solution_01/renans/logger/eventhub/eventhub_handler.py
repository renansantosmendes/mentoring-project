__author__ = 'Renan Santos'
__version__ = '0.1.0'

import typing as tp
import logging as lg
from renans.logger.interfaces.i_handler import IHandler


class EventhubHandler(IHandler):

    def __init__(
            self,
            eventhub_connection_string: str,
            eventhub_name: str,
            application_name: str) -> None:
        super(EventhubHandler, self).__init__()
        self.eventhub_connection_string = eventhub_connection_string
        self.eventhub_name = eventhub_name
        self.application_name = application_name

    def emit(self, record: lg.LogRecord) -> None:
        raise NotImplementedError()
