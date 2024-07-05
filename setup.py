from setuptools import setup, find_packages

# Read the contents of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="E-Peen",
    version="1.1.0",
    author="crosschainer",
    author_email="cross@xian.org",
    description="A benchmarking tool (CPU, GPU, RAM, Storage) to measure your e-peen.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crosschainer/e-peen",
    packages=["e_peen"],
    include_package_data=True,
    install_requires=[
        "pyopencl",
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'e-peen = e_peen.app:run',
        ],
    },
)