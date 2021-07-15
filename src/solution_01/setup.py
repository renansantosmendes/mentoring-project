__author__ = 'Gabriel Salgado and Renan Santos'

from setuptools import setup, find_packages
import pathlib as pl

meta = dict()
exec(open(pl.Path('renans', 'logger', 'meta.py')).read(), meta)

author = meta['__author__']
author_email = meta['__email__']
version = meta['__version__']
name = meta['__name__']
license_ = meta['__license__']
credits_ = meta['__credits__']
doc = meta['__doc__']

maintainer = author
maintainer_email = author_email
keywords = [
    'classification',
    'solution',
    'predictions',
    'evaluation',
]
description = doc.split('\n', 1)[0]
long_description = doc
install_requires = [
    element
    for element in [
        line.split('#', 1)[0].strip()
        for line in open('requirements.txt', 'r', encoding='utf-8')
    ]
    if element and not element.startswith('--')
]
extras_require = {
    'tests': [
        'pytest',
        'pytest-mock',
        'pytest-cov',
    ]
}
classifiers = [
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
]

setup(
    name=name,
    author=author,
    author_email=author_email,
    version=version,
    license=license_,
    credits=credits_,
    maintainer=maintainer,
    maintainer_email=maintainer_email,
    keywords=keywords,
    description=description,
    long_description=long_description,
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=classifiers,
    packages=find_packages(exclude=['tests']),
)
