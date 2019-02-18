import setuptools

with open('Readme.md') as readme_reader:
	long_description = readme_reader.read()

setuptools.setup(
	name='pyhtrie',
	version='1.0.0',
	author='Aron Sajan Philip',
	author_email='arondeveloper@yahoo.com',
	long_description=long_description,
	license='MIT',
	summary='Hashed Trie Data Structure for faster memory efficient and fast keyword indexing and lookup',
	url='https://github.com/aronsajan/pyhtrie/tree/master',
	packages=setuptools.find_packages()
	)