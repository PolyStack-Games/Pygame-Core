"""Based on: https://github.com/pypa/sampleproject."""
#pylint: disable=invalid-name,missing-module-docstring,missing-function-docstring
from os import path
from setuptools import find_packages, setup

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the version from the VERSION.py file
with open(path.join(path.abspath(path.dirname(__file__)), 'VERSION'), encoding='utf-8') as f:
    version = f.read()

# Define requirements
INSTALL_REQUIRE = ['pygame>=2.5.2']
TESTS_REQUIRE = ['pylint', 'pytest', 'pytest-pylint']

setup(
    name='pygame-core',

    # Versions should comply with PEP440
    version=version,

    description='A modular core library for Pygame-based 2D games.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url="https://github.com/Nicklas185105/Pygame-Core",

    author="Nicklas Beyer Lydersen",
    author_email="nicklasbeyerlydersen@gmail.com",

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],

    keywords='pygame game development engine',

    packages=find_packages(include=["core", "core.*"]),

    install_requires=INSTALL_REQUIRE,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': TESTS_REQUIRE,
    },

    setup_requires=['pytest-runner'],

    tests_require=TESTS_REQUIRE,

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # for example: 'sample': ['package_data.dat']
    package_data={
        # Include any package-specific data files here
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    project_urls={
        'Wiki': 'https://github.com/Nicklas185105/Pygame-Core/wiki',
        'Source': 'https://github.com/Nicklas185105/Pygame-Core',
    },
)
#pylint: enable=invalid-name,missing-module-docstring,missing-function-docstring
