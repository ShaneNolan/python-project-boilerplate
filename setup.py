from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description: str = file.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="",
    version="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="",
    author_email="",
    packages=find_packages(exclude=("tests",)),
    install_requires=requirements,
    zip_safe=False,
    test_suite="tests",
    # entry_points={"": ["",]},
)
