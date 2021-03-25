from setuptools import setup, find_packages
from pip._internal.req import parse_requirements
from pip._internal.download import PipSession


requires_file = parse_requirements("requirements.txt", session=PipSession())
requires = [str(ir.req) for ir in requires_file]

""" Full manual: https://setuptools.readthedocs.io/en/latest/setuptools.html
"""
setup(
    name="TutorialPackage",
    version="0.1",
    packages=find_packages(),
    # scripts=['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine

    install_requires=[
        'PyYAML==5.4',
        'scikit_learn@https://files.pythonhosted.org/packages/4d/73/7b6c17c3738de4c8fc42b626eb26e7756ef8624b0b8729d0820216932721/scikit_learn-0.21.3-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl'
    ],
    # install_requires=requires,

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata to display on PyPI
    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://bugs.example.com/HelloWorld/",
        "Documentation": "https://docs.example.com/HelloWorld/",
        "Source Code": "https://code.example.com/HelloWorld/",
    },
    # Lista di possibili valori per i classifiers:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]

    # could also include long_description, download_url, etc.
)