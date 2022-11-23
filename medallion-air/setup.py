from setuptools import find_packages, setup

setup(
    name="medallion_air",
    version="0+dev",
    author="George T. C. Lai",
    author_email="tsungchih.hd@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["test"]),
    # package_data={"project_fully_featured": ["hacker_news_dbt/*"]},
    install_requires=[
        "aiobotocore==1.3.3",
        "dagster",
        "dagster-pandas",
        "dagster-postgres",
        # "duckdb!=0.3.3",  # missing wheels
        "mock",
        # DataFrames were not written to Snowflake, causing errors
        "pandas<1.4.0",
        "pyarrow>=4.0.0",
        # "pyspark",
        "requests",
        "gcsfs",
        "fsspec",
        # "s3fs",
        "scipy",
        # "sklearn",
        # "snowflake-sqlalchemy",
    ],
    extras_require={"dev": ["dagit", "pytest"], "tests": ["mypy", "pylint", "pytest"]},
)
