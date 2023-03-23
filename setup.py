from setuptools import setup, find_packages

version = '0.2.0'

setup(
    name='django-yarn',
    version=version,
    description="Integrate django with yarn",
    long_description=open('README.rst').read(),
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    author='Pavel Alekin',
    author_email='',
    url='https://github.com/minidron/django-yarn',
    license='BSD',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'django',
    ],
    entry_points="",
)
