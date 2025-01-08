"""Based on: https://github.com/pypa/sampleproject."""
# pylint: disable=invalid-name,missing-module-docstring,missing-function-docstring
from os import getenv, path
from setuptools import find_packages, setup

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get the version from the environment variable, default to '0.0.1' if not set
version = getenv('RELEASE_VERSION', '0.0.1')

# Define requirements
INSTALL_REQUIRE = ['pygame>=2.5.2']
EXTRAS_REQUIRE = {
    'test': ['pylint', 'pytest', 'pytest-pylint'],
}

setup(
    name='pygame-pygame_core',

    # Versions should comply with PEP440
    version=version,

    description='A modular pygame_core library for Pygame-based 2D games.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url="https://github.com/PolyStack-Games/Pygame-Core",

    author="PolyStack Games",
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

    packages=find_packages(include=["pygame_core", "pygame_core.*"]),

    install_requires=INSTALL_REQUIRE,

    extras_require=EXTRAS_REQUIRE,

    setup_requires=['pytest-runner'],

    package_data={
        # Include any package-specific data files here
    },

    data_files=[],

    project_urls={
        'Source': 'https://github.com/PolyStack-Games/Pygame-Core',
    },
)
# pylint: enable=invalid-name,missing-module-docstring,missing-function-docstring
