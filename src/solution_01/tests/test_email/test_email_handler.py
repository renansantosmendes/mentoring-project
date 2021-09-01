__author__ = 'Renan Santos'

from logging.handlers import SMTPHandler
from unittest import mock as mk

import pytest
import pytest_mock as pm

from renans.logger.email import EmailHandler
from renans.logger.testing.mock_email_handler import MockEmailHandler


class TestEmailHandler(object):

    @pytest.fixture
    def smtp_handler_emit(self, mocker: pm.MockerFixture) -> mk.Mock:
        emit = mocker.Mock()
        mocker.patch('logging.handlers.SMTPHandler.emit', emit)
        return emit

    def test__init__success(
            self,
            mock_email_handler: MockEmailHandler,
    ) -> None:
        mailhost = mock_email_handler.mailhost
        fromaddr = mock_email_handler.fromaddr
        toaddrs = mock_email_handler.toaddrs
        subject = mock_email_handler.subject
        credentials = mock_email_handler.credentials
        secure = mock_email_handler.secure
        timeout = mock_email_handler.timeout

        email_handler = EmailHandler(
            mailhost,
            fromaddr,
            toaddrs,
            subject,
            credentials,
            secure,
            timeout,
        )

        assert email_handler.mailhost is mailhost
        assert email_handler.fromaddr is fromaddr
        assert email_handler.toaddrs is toaddrs
        assert email_handler.subject is subject
        assert email_handler.credentials is credentials
        assert email_handler.secure is secure
        assert email_handler.timeout is timeout
        assert isinstance(email_handler._smtp_handler, SMTPHandler)

    def test__emit__success(
            self,
            mock_email_handler: MockEmailHandler,
            smtp_handler_emit: mk.Mock,
    ) -> None:
        email_handler = mock_email_handler.email_handler
        log_record = mock_email_handler.log_record

        email_handler.emit(log_record)

        smtp_handler_emit.assert_called_once_with(log_record)
