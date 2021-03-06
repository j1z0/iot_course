import os
from setuptools import setup

# variables used in buildout
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'pytest-runner',
    'boto3',
]

tests_require = [
    'pytest',
    'pytest-mock',
    'pytest-cov',
]

setup(
    name='sample',
    version=open("sample/_version.py").readlines()[-1].split()[-1].strip("\"'"),
    description='starter project',
    long_description=README,
    packages=['sample'],
    include_package_data=True,
    zip_safe=False,
    author='4dn Team at Harvard Medical School',
    author_email='jeremy_johnson@hms.harvard.edu',
    url='https://data.4dnucleome.org',
    license='MIT',
    install_requires=requires,
    setup_requires=requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
)
