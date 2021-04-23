"""Run "python setup.py install" to install pyhighlighterclient."""

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        long_description = f.read()

except Exception:
    long_description = """
    `pyhighlighterclient` is a demo python package for silverpond, ......

    More information at: https://github.com/silverpond/pyhighlighterclient/.
"""


setup(name="pyhighlighterclient",
      packages=find_packages(),
      version='0.0.3',
      description="highlighter client python package",
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 1 - Beta',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: '
          'Python Modules',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      author='Mykhailo',
      author_email='mihailkirilyuk@hotmail.com',
      license='MIT',
      url="https://github.com/silverpond/pyhighlighterclient/",
      keywords=['Python', 'plugin'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['setuptools>=38.6.0'],
      )
