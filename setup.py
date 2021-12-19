from distutils.core import setup

setup(
    name="foo",
    version="1.0.0",
    description="foos the bar",
    author="company",
    author_email="name@company.com",
    url="https://bitbucket.org/companyname/lib-foo",
    install_requires=[
        "structlog",
    ],
    packages=[
        "foo",
    ],
)
