from setuptools import setup, find_packages

setup(
    name='py-grabber',
    version='0.1',
    description='Extract main content from web-page',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'chardet',
    ],
    test_suite='tests',
)
