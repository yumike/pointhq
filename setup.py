from setuptools import setup, find_packages


setup(
    name = 'pointhq',
    version = '0.1.dev',
    license = 'ISC',
    description = 'pointhq.com API client',
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
