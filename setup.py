import setuptools

with open('Readme.md') as readme_reader:
	long_description = readme_reader.read()

setuptools.setup(
	name='pyhtrie',
	version='1.0.0',
	author='Aron Sajan Philip',
	author_email='arondeveloper@yahoo.com',
	long_description=long_description,
	packages=setuptools.find_packages()
	)