from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='<%= projectID %>',
    version='0.0.1',
    description='<%= desc %>',
    long_description=readme(),
    url='https://github.com/<%= githubuser %>/<%= projectID %>',
    download_url='https://github.com/<%= githubuser %>/<%= projectID %>/tarball/0.0.1',
    author='<%= user %>',
    author_email='<%= email %>',
    license='GPLv3',
    keywords=['?'],
    packages=['<%= projectID %>'],
    install_requires=[
         'pytest>=2.9.2',
         'sphinx>=1.4.5',
         'gcsfs>=0.3.1', 
         'tqdm>=4.36.1',
         'pytest-cov>=2.8.1',
         'coverage>=4.5.4',

    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
