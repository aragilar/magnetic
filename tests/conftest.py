from itertools import product
import socket

import pytest

TEST_FAMILIES = [
    socket.AF_INET,
    socket.AF_INET6,
    socket.AF_UNIX,
]

TEST_TYPES = [
    socket.SOCK_STREAM,
]

TEST_PROTOS = [
    0,
]

sock_args = list(zip(*product(TEST_FAMILIES, TEST_TYPES, TEST_PROTOS)))

@pytest.fixture(params=sock_args[0])
def family(request):
    return request.param

@pytest.fixture(params=sock_args[1])
def type(request):
    return request.param

@pytest.fixture(params=sock_args[2])
def proto(request):
    return request.param


@pytest.fixture()
def families(request):
    return sock_args[0]

@pytest.fixture()
def types(request):
    return sock_args[1]

@pytest.fixture()
def protos(request):
    return sock_args[2]


