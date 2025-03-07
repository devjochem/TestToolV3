from setuptools import find_packages, setup
with open("README.md", "r") as fh:
	description = fh.read()

setup(
	name="TestTool V3",
	version="3.0.1",
	author="DevJochem",
	author_email="jochembenning@gmail.com",
	packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
	description="A Simple testtool",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://github.com/gituser/test-tackage",
	license='MIT',
	python_requires='>=3.8',
	install_requires=[
        'pySMART',
        'numpy',
        'opencv-python',
        'PySide6',
        'PyQt6'
    ]
)
