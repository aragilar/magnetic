import socket
import pytest

import magnetic._utils as utils


class TestCreateAndBind(object):
    def test_create_default(self, families, types, protos):
        sockets = utils.create_and_bind(families, types, protos)
        for sock, family, type, proto in zip(sockets, families, types, protos):
            assert sock.family == family
            assert sock.type == type
            assert sock.proto == proto

    def test_max_socks_greater_than(self, families, types, protos):
        # no exception should be raised
        max_socks = max(len(families), len(types), len(protos)) + 1
        utils.create_and_bind(families, types, protos, max_socks=max_socks)

    def test_max_socks_equal(self, families, types, protos):
        # no exception should be raised
        max_socks = max(len(families), len(types), len(protos))
        utils.create_and_bind(families, types, protos, max_socks=max_socks)

    def test_max_socks_less_than(self, families, types, protos):
        max_socks = max(len(families), len(types), len(protos)) - 1
        with pytest.raises(utils.MagneticError):
            utils.create_and_bind(families, types, protos, max_socks=max_socks)

    def test_no_args(self):
        normal_sock = socket.socket()
        mag_sock = utils.create_and_bind()[0]
        assert mag_sock.family == normal_sock.family
        assert mag_sock.type == normal_sock.type
        assert mag_sock.proto == normal_sock.proto
