from setuptools import setup, find_packages

setup(name='ipfshttpclient',
    version='0.0.1',
    url='https://github.com/AudiusProject/py-ipfs-api',
    packages=['ipfshttpclient'],
    install_requires=[
        'requests',
        'six'
    ]
)
