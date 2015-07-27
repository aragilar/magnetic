
from os import strerror
import socket

from ._sane_fromfd import lib, ffi
from .sock_enums import AddressFamily, SocketKind, IPProtocol

_FAMILY_IS_PROTOCOL_STRS = [
    "AF_UNIX",
    "AF_INET",
    "AF_INET6",
]

# Common address families which either have a single protocol (i.e. protocol==0
# is always correct), or are commonly assumed to have only one protocol (e.g.
# INET, which has both SOCK_RAW which allows different protocols, as well as
# IPPROTO_UDPLITE as a potential protocol with SOCK_DGRAM
FAMILY_IS_PROTOCOL = [
    getattr(AddressFamily, fam)
    for fam in _FAMILY_IS_PROTOCOL_STRS
    if hasattr(AddressFamily, fam)
]

def errno_to_exception(errno, arg):
    return socket.error(errno, strerror(errno), arg)

def sock_fd_errno_exception(errno, fd):
    return errno_to_exception(errno, "fd {:d}".format(fd))

def fromfd(fd):
    family = get_family(fd)
    type = get_type(fd)
    proto = get_proto(fd)
    return socket.socket(family, type, proto, fd)

def get_family(fd):
    fam = ffi.new("int *")
    flag = lib.magnetic_get_sock_family(fd, fam)
    if flag == -1:
        raise sock_fd_errno_exception(ffi.errno, fd)
    return AddressFamily(fam[0])

def get_type(fd):
    ty = ffi.new("int *")
    flag = lib.magnetic_get_sock_type(fd, ty)
    if flag == -1:
        raise sock_fd_errno_exception(ffi.errno, fd)
    return SocketKind(ty[0])

def get_proto(fd):
    proto = ffi.new("int *")
    flag = lib.magnetic_get_sock_proto(fd, proto)
    if flag == -1:
        raise sock_fd_errno_exception(ffi.errno, fd)
    return IPProtocol(proto[0])
