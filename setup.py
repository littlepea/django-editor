from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = [
        'django',
    ]

setup(name='django-editor',
    version=version,
    description="Allows pluggable WYSIWYG editors in django admin without hard dependencies",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Evgeny Demchenko',
    author_email='little_pea@list.ru',
    url='https://github.com/littlepea/django-editor',
    license='BSD',
    packages=find_packages(),
    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
        'argparse',  # apparently needed by django-setuptest on python 2.6
        'django-imperavi',
        'django-tinymce',
    ),
    zip_safe=False,
    install_requires=REQUIREMENTS,
)
