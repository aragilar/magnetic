from logging import getLogger
import socket
from warnings import warn

from six.moves import zip_longest

from ._internals.sock_enums import AddressFamily, SocketKind

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


def create_and_bind(
    families=None, types=None, protos=None, addrs=None, max_socks=None
):
    """
    Create needed sockets and bind them.
    """
    log.debug("Socket creation forced")
    sock_list = []
    if families is None:
        families = [None]
    if types is None:
        types = [None]
    if protos is None:
        protos = [None]
    if addrs is None:
        addrs = [None]

    if (max_socks is not None) and (
        max_socks < max(len(families), len(types), len(protos))
    ):
        raise MagneticError(TOO_MANY_SOCKETS_MSG.format(max_socks))
    for fam, ty, pro, ad in zip_longest(families, types, protos, addrs):
        if fam is None:
            fam = AddressFamily.AF_INET
        if ty is None:
            ty = SocketKind.SOCK_STREAM
        if pro is None:
            pro = 0
        sock = socket.socket(fam, ty, pro)

        if ad is not None:
            sock.bind(ad)
        else:
            warn("No address passed, not binding...")

        sock_list.append(sock)
    return sock_list
