from setuptools import setup, find_packages

setup(
    name="agniscan",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "colorama",
        "tqdm",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "agniscan=agniscan.main:main"
        ]
    },
    author="Rashi Karnewar",
    description="AgniScan - Automated Web Security Scanner",
    python_requires=">=3.8",
)
