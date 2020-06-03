from setuptools import find_packages, setup

setup(
    name="ezyvet-etl-santhosh",
    version="1.0.0",
    description="Provides API to build contact, address and phone from contacts by doing various ETL transformations",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
