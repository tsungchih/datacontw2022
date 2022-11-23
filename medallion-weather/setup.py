from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="medallion_weather",
        packages=find_packages(exclude=["medallion_weather_tests"]),
        install_requires=[
            "dagster",
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )
