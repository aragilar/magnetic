# -*- coding: utf-8 -*-
"""
magnetic
~~~~~~~~~~

A bunch of tools for using venvs (and virtualenvs) from python.

:copyright: (c) 2015 by James Tocknell.
:license: MIT, see LICENSE for more details.
"""

from .utils import (
    MagneticError, NO_OS_SUPPORT_MSG, UNKNOWN_METHOD_MSG, create_and_bind
)
from ._internals import fromfd
from ._internals.systemd import systemd_sockets
from ._internals.inetd import inetd_sockets
from ._internals.launchd import launchd_sockets
from ._internals.upstart import upstart_sockets

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def get_socket(
    method, family=None, type=None, proto=None, addr=None, force_create=False,
):
    """
    Utility function to get a single socket-activation socket.

    `get_socket` returns a single socket (`socket.socket`), with `bind`
    having been called by the parent process (or equivalent depending on
    system). In the case that acquiring the socket fails,
    `magnetic.MagneticError` is raised. If `force_create` is `True`, try to
    create a socket with `family`, `type` and `proto`. This new socket is not
    bound.

    .. note::
        This function enforces that a single socket be returned, multiple
        sockets being provided cause this function to raise
        `magnetic.MagneticError`.

    .. warning::
        There should only be a single call to `get_socket` or `get_sockets`.
        Multiple calls may break in strange ways.

    :param method: The system used to perform socket activation. `None`
        specifies that a new socket be created. Supported values are 'systemd',
        'inetd', 'launchd', 'upstart' and `None`.
    :type method: str or None

    :param family: The family used if a new socket is created. See
        `socket.socket` for further information.
    :type family: socket.AF_* or similar

    :param type: The type used if a new socket is created. See
        `socket.socket` for further information.
    :type type: socket.SOCK_* or similar

    :param protocol: The protocol used if a new socket is created. See
        `socket.socket` for further information.
    :type protocol: int

    :param force_create bool: Create a new socket if activation fails.

    :return: The acquired socket.
    :rtype: `socket.socket` or equivalent

    :raises magnetic.MagneticError: if socket acquisition fails.

    """
    return get_sockets(
        [method], [family], [type], [proto], [addr], force_create, max_socks=1
    )[0]


def get_bound_sockets(
    method, families=None, types=None, protos=None, addrs=None, force_create=False,
    max_socks=None
):
    """
    Utility function to get socket-activation sockets.

    `get_sockets` returns a list of sockets (`socket.socket`), with `bind`
    having been called by the parent process (or equivalent depending on
    system). In the case that acquiring the sockets fail,
    `magnetic.MagneticError` is raised. If `force_create` is `True`, try to
    create sockets with `families`, `types` and `protos`. These new sockets are
    not bound.

    .. warning::
        There should only be a single call to `get_socket` or `get_sockets`.
        Multiple calls may break in strange ways.

    :param method: The system used to perform socket activation. `None`
        specifies that a new socket be created. Supported values are 'systemd',
        'inetd', 'launchd', 'upstart' and `None`.
    :type method: str or None

    :param families: List of families to use if new sockets are created. Each
        item represents a new socket. See `socket.socket` for further
        information.
    :type families: list of socket.AF_* or similar

    :param types: List of types to use if new sockets are created. Each
        item represents a new socket. See `socket.socket` for further
        information.
    :type types: list of socket.SOCK_* or similar

    :param protocol: List of families to use if new sockets are created. Each
        item represents a new socket. See `socket.socket` for further
        information.
    :type protocol: list of int

    :param force_create bool: Create a new socket if activation fails.

    :param max_socks: Maximum number of sockets that should be acquired. If the
        number of sockets that can be acquired exceeds this, raise
        `magnetic.MagneticError`. `None` disables this check.
    :type max_socks: int or None

    :return: The acquired sockets.
    :rtype: list of `socket.socket` or equivalent

    :raises magnetic.MagneticError: if socket acquisition fails.

    """
    if method is None:
        return create_and_bind(families, types, protos, addrs, max_socks)
    try:
        if not HAS_SOCKET_ACTIVATION:
            raise MagneticError(NO_OS_SUPPORT_MSG)
        return max_socks(method, max_socks)
    except MagneticError:
        if force_create:
            return create_and_bind(families, types, protos, addrs, max_socks)
        raise



def mag_sockets(method, max_socks=None):
    if method == "systemd":
        return systemd_sockets(max_socks)
    elif method == "inetd":
        return inetd_sockets(max_socks)
    elif method == "launchd":
        return launchd_sockets(max_socks)
    elif method == "upstart":
        return upstart_sockets(max_socks)
    raise MagneticError(UNKNOWN_METHOD_MSG.format(method))
