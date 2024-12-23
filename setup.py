from setuptools import setup, find_packages

setup(
    name="pygame-core",
    version="0.1.0",
    description="A modular core for Pygame-based 2D games.",
    author="Nicklas Beyer Lydersen",
    author_email="nicklasbeyerlydersen@gmail.com",
    url="https://github.com/Nicklas185105/Pygame-Core",
    packages=find_packages(include=["core*"]),
    install_requires=[
        "pygame>=2.6.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
