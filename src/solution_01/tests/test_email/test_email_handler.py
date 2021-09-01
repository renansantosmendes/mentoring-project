__author__ = 'Renan Santos'

from renans.logger.email import EmailHandler
from renans.logger.testing.mock_email_handler import MockEmailHandler


class TestEmailHandler(object):

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
