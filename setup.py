from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in law_management/__init__.py
from law_management import __version__ as version

setup(
	name="law_management",
	version=version,
	description="Law Management, Legal Management, This module allows to manage lawyers,clients, matters(cases), trials and its invoicing.",
	author="Solufy",
	author_email="dawnstar0825@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
