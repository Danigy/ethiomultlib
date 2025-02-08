# setup.py
from setuptools import setup, find_packages

setup(
    name='ethiomultlib',                                                # a unique package name
    version='0.1.0',                                                    # version 0.1.0  
    packages=find_packages(),
    author='Daniel Gessese Amdework',                                   # My name, Fathers' name, and Grand Father's name
    author_email='dnlmdwrk@gmail.com',                                  # email
    description='A Python library for Ethiopian Multiplication.',
    long_description=open('README.md').read(),                          # Optional: If you have a README.md
    long_description_content_type='text/markdown',                      # README.md with markdown
    url="https://github.com/Danigy/ethiomultlib",                       # <-- ACTUAL URL HERE
    project_urls={
        "Source": "https://github.com/Danigy/ethiomultlib", 
            },
    license='MIT',                                                      # MIT license (GPL, Apache 2.0)
    release_date='February 7, 2025',                                    # First version of the library released date.
    classifiers=[
        'Development Status :: 3 - Alpha',                              # Choose development status
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',                                            # Minimum Python version supported
)