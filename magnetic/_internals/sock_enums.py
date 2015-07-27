
from enum import IntEnum
from socket import *

# from python 3.4 cpython
if not hasattr(locals(), 'AddressFamily'):
    IntEnum._convert(
        'AddressFamily',
        __name__,
        lambda C: C.isupper() and C.startswith('AF_')
    )
if not hasattr(locals(), 'SocketKind'):
    IntEnum._convert(
        'SocketKind',
        __name__,
        lambda C: C.isupper() and C.startswith('SOCK_')
    )

# Custom Enums

IntEnum._convert(
        'IPProtocol',
        __name__,
        lambda C: C.isupper() and C.startswith('IPPROTO_'))

__all__ = ['AddressFamily', 'SocketKind', 'IPProtocol']
