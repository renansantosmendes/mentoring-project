__author__ = 'Renan Santos'
__version__ = '0.1.0'

import typing as tp
import functools as ft
import logging as lg

import pytest_mock as pm

from renans.logger.email import EmailHandler


class MockEmailHandler(object):

    def __init__(self, mocker: pm.MockerFixture) -> None:
        super().__init__()
        self.mocker = mocker

    @ft.cached_property
    def mailhost(self) -> str:
        return self.mocker.Mock(spec=str)

    @ft.cached_property
    def fromaddr(self) -> str:
        return self.mocker.Mock(spec=str)

    @ft.cached_property
    def toaddrs(self) -> tp.List[str]:
        return self.mocker.Mock(spec=tp.List[str])

    @ft.cached_property
    def subject(self) -> str:
        return self.mocker.Mock(spec=str)

    @ft.cached_property
    def credentials(self) -> tp.Tuple[str, str]:
        return self.mocker.Mock(spec=tp.Tuple[str, str])

    @ft.cached_property
    def secure(self) -> tp.Tuple[str, str]:
        return self.mocker.Mock(spec=tp.Tuple[str, str])

    @ft.cached_property
    def timeout(self) -> float:
        return self.mocker.Mock(spec=float)

    @ft.cached_property
    def email_handler(self) -> EmailHandler:
        mailhost = self.mailhost
        fromaddr = self.fromaddr
        toaddrs = self.toaddrs
        subject = self.subject
        credentials = self.credentials
        secure = self.secure
        timeout = self.timeout

        return EmailHandler(
            mailhost,
            fromaddr,
            toaddrs,
            subject,
            credentials,
            secure,
            timeout,
        )

    @ft.cached_property
    def log_record(self) -> lg.LogRecord:
        return self.mocker.Mock(spec=lg.LogRecord)