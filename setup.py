from setuptools import setup, find_packages

setup(
    name='py-grabber',
    version='0.1.3',
    url='https://github.com/kirillsulim/py-grabber',
    description='Extract main content from web-page',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'chardet',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'pygrab = py_grabber.app:run',
            ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
