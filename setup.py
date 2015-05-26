from setuptools import setup

setup(
    name='blogdown',
    version='1.2.0',
    author='Brant Young',
    author_email='brant.young@gmail.com',
    include_package_data = True,
    packages=['blogdown', 'blogdown.modules'],
    description='a simple static blog generator',
    long_description=open('README.rst').read(),
    license='BSD License',
    url='https://github.com/brantyoung/blogdown/',
    entry_points = {
        'console_scripts': ['run-blogdown = blogdown.cli:main'],
    },
    install_requires=[
        'PyYAML',
        'Babel',
        'blinker',
        'Markdown',
        'Jinja2>=2.4',
        'Werkzeug',
        'docutils',
        'pygments',
    ]
)
