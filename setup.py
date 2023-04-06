from setuptools import setup, find_packages

setup(
    name='mighty_subscribe',
    version='0.1',
    description='for testing installation of a package',
    author='Jacob',
    author_email='jwang@mightyoaks.com',
    packages=['mighty_subscribe',],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.11',
    ],
)
