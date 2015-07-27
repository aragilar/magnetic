from functools import wraps
from logging import getLogger
import socket

log = getLogger(__name__)

UNKNOWN_METHOD_MSG = "Socket activation method {} not known"
NO_OS_SUPPORT_MSG = "OS does not support socket activation"
TOO_MANY_SOCKETS_MSG = "More than {} sockets given"
ACTIVATION_FAILED_MSG = "Socket activation failed"
UNKNOWN_SOCK_TYPE_MSG = "Unknown socket family based on sockname {}"
SOCKET_UNFIXED_MSG = "Socket identification broke"

HAS_SOCKET_ACTIVATION = hasattr(socket, "AF_UNIX")

class MagneticError(Exception):
    pass



def _fix_sock_props(sock_fd):
    """
    Discover family, type, protocol of socket, and return socket correctly
    opened.
    """
    # from gunicorn, should work based on check of socket.c in cpython
    try:
        sock = socket.fromfd(sock_fd, socket.AF_UNIX, socket.SOCK_STREAM)
        sockname = sock.getsockname()
        if isinstance(sockname, str) and sockname.startswith('/'):
            # doesn't check type afaik
            family, type, proto = socket.AF_UNIX, socket.SOCK_STREAM, 0
        elif len(sockname) == 2 and '.' in sockname[0]:
            # doesn't check type afaik
            family, type, proto = socket.AF_INET, socket.SOCK_STREAM, 0
        elif len(sockname) == 4 and ':' in sockname[0]:
            # doesn't check type afaik
            family, type, proto = socket.AF_INET6, socket.SOCK_STREAM, 0
        else:
            raise MagneticError(UNKNOWN_SOCK_TYPE_MSG.format(sockname))
    except socket.error as e:
        log.warn(str(e))
    try:
        return socket.fromfd(sock_fd, family, type, proto)
    except NameError:
        raise MagneticError(SOCKET_UNFIXED_MSG)


def create_and_bind(families, types, protos, addrs, max_socks=None):
    """
    Create needed sockets and bind them.
    """
    log.debug("Socket creation forced")
    sock_list = []
    if (max_socks is not None) and (
        max_socks < max(len(families), len(types), len(protos))):
        raise MagneticError(TOO_MANY_SOCKETS_MSG.format(max_socks))
    for fam, ty, pro, ad in zip(families, types, protos, addrs):
        sock = sock(fam, ty, pro)
        sock.bind(ad)
        sock_list.append(sock)
    return sock_list
