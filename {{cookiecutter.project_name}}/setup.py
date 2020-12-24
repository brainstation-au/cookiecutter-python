from setuptools import setup, find_packages


requirements = [
]

setup(
    author="brainstation-au",
    author_email="brainstation@outlook.com.au",
    description="{{cookiecutter.project_description}}",
    entry_points={},
    install_requires=requirements,
    name="{{cookiecutter.project_name}}",
    package_data={},
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/brainstation-au/{{cookiecutter.project_name}}",
    version="0.1.0",
    zip_safe=False
)
