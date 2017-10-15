import setuptools

import versioneer

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

run_requires = ["cffi>=1.0.0", "six"]

if PY34_BACKPORT:
    run_requires.append("enum34")

setuptools.setup(
    name="magnetic",
    version = versioneer.get_version(),
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    cmdclass=versioneer.get_cmdclass(),
)
