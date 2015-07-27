
from sys import stdin, stdout, stderr

from . import fromfd

def inetd_sockets(max_socks):
    """
    """
    sock = fromfd(stdin.fileno())
    stdin.close()
    stdout.close()
    stderr.close()
    return sock
