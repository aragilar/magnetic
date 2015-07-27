
PYTHON_HAS_SANE_FROMFD = False

if PYTHON_HAS_SANE_FROMFD:
    from socket import fromfd
else:
    from .sane_fromfd import fromfd
