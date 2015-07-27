import setuptools

import os
## Utility funcs from https://github.com/pypa/sampleproject/blob/master/setup.py
here = os.path.abspath(os.path.dirname(__file__))
# Read the version number from a source file.
# Code taken from pip's setup.py
def find_version(*file_paths):
    import codecs
    import re
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")
#import codecs
#with codecs.open('DESCRIPTION.rst', 'r', 'utf-8') as f:
#    long_description = f.read()

def need_backport(major, minor):
    import sys
    if sys.version_info[0] < major or (
        sys.version_info[0] == major and sys.version_info[1] < minor
    ):
        return True
    return False

PY34_BACKPORT = need_backport(3,4)

run_requires = ["cffi>=1.0.0"]

if PY34_BACKPORT:
    run_requires.append("enum34")

setuptools.setup(
    name="magnetic",
    version=find_version("magnetic", "__init__.py"),
    packages=["magnetic", "magnetic._internals"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["magnetic/_internals/sane_fromfd_build.py:ffi"],
    install_requires=run_requires,
    author = "James Tocknell",
    author_email = "aragilar@gmail.com",
    description = "Socket activation for python",
#    long_description = long_description,
    url = "http://magnetic.rtfd.org",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
