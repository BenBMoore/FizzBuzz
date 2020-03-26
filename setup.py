import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FizzBuzz",
    version="0.0.1",
    author="Ben Moorer",
    author_email="ben@ben.gs",
    description="A small FizzBuzz Program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenBMoore/FizzBuzzt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
