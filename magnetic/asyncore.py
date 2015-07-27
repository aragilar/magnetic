import asyncore
import socket

from . import get_socket

class dispatcher(asyncore.dispatcher):
    """
    Subclass of `asyncore.dispatcher` with socket activation support.

    This class provides a version of `asyncore.dispatcher` with socket
    activation support via the `sock_activate_method` attribute. Defining this
    attribute (see `get_socket`'s `method`) will cause the dispatcher to acquire a socket
    from that system, instead of creating its own. By default, not defining
    `sock_activate_method` causes the dispatcher to create its own socket.
    """
    sock_activate_method = None

    def create_socket(self, family=socket.AF_INET, type=socket.SOCK_STREAM):
        sock = get_socket(
            self.sock_activate_method, family=family, type=type,
            force_create=True
        )
        self.family_and_type = sock.family, sock.type
        sock.setblocking(0)
        self.set_socket(sock)


class dispatcher_with_send(dispatcher, asyncore.dispatcher_with_send):
    """
    Subclass of `asyncore.dispatcher_with_send` with socket activation support.

    This class provides a version of `asyncore.dispatcher_with_send` with socket
    activation support via the `sock_activate_method` attribute. Defining this
    attribute (see `get_socket`'s `method`) will cause the dispatcher_with_send
    to acquire a socket from that system, instead of creating its own. By
    default, not defining `sock_activate_method` causes the dispatcher_with_send
    to create its own socket.
    """
    pass
