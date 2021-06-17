__author__ = 'Renan Santos'
__version__ = '0.1.0'

import typing as tp
import logging as lg
from renans.logger.interfaces.i_handler import IHandler


class EmailHandler(IHandler):

    def __init__(
            self,
            mailhost: tp.Union[str, tp.Tuple[str, int]],
            fromaddr: str,
            toaddrs: tp.List[str],
            subject: str,
            credentials: tp.Optional[tp.Tuple[str, str]] = None,
            secure: tp.Union[tp.Tuple[str], tp.Tuple[str, str], None] = None,
            timeout: float = 5.0) -> None:
        super(EmailHandler, self).__init__()
        self.mailhost = mailhost
        self.fromaddr = fromaddr
        self.toaddrs = toaddrs
        self.subject = subject
        self.credentials = credentials
        self.secure = secure
        self.timeout = timeout

    def emit(self, record: lg.LogRecord) -> None:
        raise NotImplementedError()
