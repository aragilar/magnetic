import pytest

import magnetic.utils as utils


class TestCreateSocks(object):
    def test_create_default(self, family, type, proto):
        sockets = utils._create_socks(families, types, protos)
        for sock, family, type, proto in zip(sockets, families, types, protos):
            assert sock.family == family
            assert sock.type == type
            assert sock.proto == proto

    def test_max_socks_greater_than(self, families, types, protos):
        # no exception should be raised
        max_socks = max(len(families), len(types), len(protos)) + 1
        utils._create_socks(families, types, protos, max_socks)

    def test_max_socks_equal(self, families, types, protos):
        # no exception should be raised
        max_socks = max(len(families), len(types), len(protos))
        utils._create_socks(families, types, protos, max_socks)

    def test_max_socks_less_than(self, families, types, protos):
        max_socks = max(len(families), len(types), len(protos)) - 1
        with pytest.raises(utils.MagneticError):
            utils._create_socks(families, types, protos, max_socks)
