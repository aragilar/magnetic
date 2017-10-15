magnetic_ provides `socket activation`_ for python.  Socket activation allows
for services to be started when necessary. While systemd_ has popularised socket
activation recently, other systems support socket activation, such as `launchd`_
and `inetd`_. magnetic_ aims to provide a unified interface to the different
socket activation protocols, as well as providing some helpers on top the
builtin socket module.


|Documentation Status| |Build Status| |Coverage Status|


.. |Documentation Status| image:: https://readthedocs.org/projects/magnetic/badge/?version=latest
   :target: http://magnetic.readthedocs.org/en/latest/?badge=latest
.. |Build Status| image:: https://travis-ci.org/aragilar/magnetic.svg?branch=master
   :target: https://travis-ci.org/aragilar/magnetic
.. |Coverage Status| image:: https://codecov.io/github/aragilar/magnetic/coverage.svg?branch=master
   :target: https://codecov.io/github/aragilar/magnetic?branch=master

.. _`socket activation`: http://0pointer.de/blog/projects/socket-activation.html
.. _systemd: https://en.wikipedia.org/wiki/Systemd
.. _launchd: https://en.wikipedia.org/wiki/Launchd
.. _inetd: https://en.wikipedia.org/wiki/Inetd
.. _magnetic: https://magnetic.readthedocs.io/
