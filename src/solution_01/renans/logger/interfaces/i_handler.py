__author__ = 'Renan Santos'
__version__ = '0.1.0'

import abc
import typing as tp
import logging as lg


class IHandler(abc.ABC):

    def __init__(
            self,
            mailhost: tp.Union[str, tp.Tuple[str, int]],
            fromaddr: str,
            toaddrs: tp.List[str],
            subject: str,
            credentials: tp.Optional[tp.Tuple[str, str]] = None,
            secure: tp.Union[tp.Tuple[str], tp.Tuple[str, str], None] = None,
            timeout: float = 5.0) -> None:
        super(IHandler, self).__init__()
        self.mailhost = mailhost
        self.fromaddr = fromaddr
        self.toaddrs = toaddrs
        self.subject = subject
        self.credentials = credentials
        self.secure = secure
        self.timeout = timeout

    @abc.abstractmethod
    def emit(self, record: lg.LogRecord) -> None:
        raise NotImplementedError()
