from setuptools import setup, find_packages

setup(
    name="agniscan",
    version="1.0",
    description="AgniScan - Automated SAST and DAST Security Scanner",
    author="Rashi Karnewar",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "agniscan=agniscan.main:main",
        ],
    },
)
