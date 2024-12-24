from setuptools import setup, find_packages

def parse_requirements(filename):
    """Parse dependencies from a requirements file."""
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="api_client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=
    parse_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "api-client=client:main",
        ],
    },
)
