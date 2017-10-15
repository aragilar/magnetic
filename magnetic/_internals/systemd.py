
from os import environ, getpid

from ..utils import (
    MagneticError, TOO_MANY_SOCKETS_MSG,
)
from . import fromfd

SD_LISTEN_FDS_START = 3
NO_SYSTEMD_SOCKETS_MSG = "No systemd sockets found"

def _systemd_sockets_pure_fix(max_socks):
    """
    Pure python acquisition of systemd sockets without use of systemd libraries.
    """
    sock_list = []
    if int(environ.get('LISTEN_PID', -1)) == getpid():
        sd_available_socks = int(environ.get('LISTEN_FDS', 0))
        if sd_available_socks > max_socks:
            raise MagneticError(
                TOO_MANY_SOCKETS_MSG.format(max_socks))
        for i in range(sd_available_socks):
            sock_list.append(fromfd(i + SD_LISTEN_FDS_START))
        if not sock_list:
            raise MagneticError(NO_SYSTEMD_SOCKETS_MSG)
        return sock_list
    raise MagneticError(NO_SYSTEMD_SOCKETS_MSG)

systemd_sockets = _systemd_sockets_pure_fix
