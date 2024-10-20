from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="style_table",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas"],
    include_package_data=True,
    description="A library for styling pandas DataFrames in Jupyter Notebooks",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/style_table.py",
    author="Jose Luis Garcia Tucci",
    author_email="jlgarciatucci@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
