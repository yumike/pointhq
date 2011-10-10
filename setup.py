import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name = 'pointhq',
    version = '0.1',
    license = 'ISC',
    description = 'pointhq.com API client',
    long_description = read('README.rst'),
    url = 'https://github.com/yumike/pointhq',
    author = 'Mike Yumatov',
    author_email = 'mike@yumatov.org',
    packages = find_packages(),
    install_requires = [
        'httplib2',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
