__author__ = 'Renan Santos'
__version__ = '0.1.0'

import abc
import logging as lg


class IHandler(abc.ABC):

    def __init__(self) -> None:
        super(IHandler, self).__init__()

    @abc.abstractmethod
    def emit(self, record: lg.LogRecord) -> None:
        raise NotImplementedError()
