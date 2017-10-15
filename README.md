[![Documentation Status](https://readthedocs.org/projects/magnetic/badge/?version=latest)](http://magnetic.readthedocs.org/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/aragilar/magnetic.svg?branch=master)](https://travis-ci.org/aragilar/magnetic)
[![Coverage Status](https://codecov.io/github/aragilar/magnetic/coverage.svg?branch=master)](https://codecov.io/github/aragilar/magnetic?branch=master)
[![Version](https://img.shields.io/pypi/v/magnetic.svg)](https://pypi.python.org/pypi/magnetic/)
[![License](https://img.shields.io/pypi/l/magnetic.svg)](https://pypi.python.org/pypi/magnetic/)
[![Wheel](https://img.shields.io/pypi/wheel/magnetic.svg)](https://pypi.python.org/pypi/magnetic/)
[![Format](https://img.shields.io/pypi/format/magnetic.svg)](https://pypi.python.org/pypi/magnetic/)
[![Supported versions](https://img.shields.io/pypi/pyversions/magnetic.svg)](https://pypi.python.org/pypi/magnetic/)
[![Supported implemntations](https://img.shields.io/pypi/implementation/magnetic.svg)](https://pypi.python.org/pypi/magnetic/)
[![PyPI](https://img.shields.io/pypi/status/magnetic.svg)](https://pypi.python.org/pypi/magnetic/)


magnetic provides
[socket activation](http://0pointer.de/blog/projects/socket-activation.html)
for python.
Socket activation allows for services to be started when necessary. While
[systemd](https://en.wikipedia.org/wiki/Systemd) has popularised socket
activation recently, other systems support socket activation, such as
[launchd](https://en.wikipedia.org/wiki/Launchd) and
[inetd](https://en.wikipedia.org/wiki/Inetd). magnetic aims to provide a unified
interface to the different socket activation protocols, as well as providing
some helpers on top the builtin socket module.

Currently targeted protocols/methods are:
 * inetd
 * systemd
 * launchd (in development)

Support for other protocols/methods is welcome, please file issues or PRs with
new methods. There was plans to support upstart, but as upstart is effectively
dead, we are not going to support upstart.

magnetic can be installed via pip, but note that magnetic requires a C compiler to
build.

Bug reports and suggestions should be filed at
[https://github.com/aragilar/magnetic/issues](https://github.com/aragilar/magnetic/issues).
