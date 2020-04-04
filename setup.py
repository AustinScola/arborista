import setuptools

with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name='arborista',
    version='0.0.1',
    author='Austin Scola',
    author_email='austinscola@gmail.com',
    description='An abstract syntax tree transformation tool for bettering Python code.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AustinScola/arborista',
    packages=['arborista'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
