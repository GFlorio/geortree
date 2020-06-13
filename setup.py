from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='geortree',
    version='0.7.0',
    packages=['geortree'],
    url='https://github.com/GFlorio/geortree',
    license='MIT',
    author='Gabriel Florio',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='gabriel@gabrielflorio.com',
    description='Reasonably efficient R-Tree implementation, adapted to work '
                'with geographic coordinates.',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
