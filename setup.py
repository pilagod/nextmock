import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nextmock",
    version="0.0.0",
    author="pilagod",
    author_email="pilagooood@gmail.com",
    keywords="testing unit mock",
    description="NextMock is an enhanced mock for unittest.mock.Mock",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pilagod/nextmock",
    project_urls={
        'Documentation': 'https://github.com/pilagod/nextmock',
        'Source': 'https://github.com/pilagod/nextmock',
        'Tracker': 'https://github.com/pilagod/nextmock/issues',
    },
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Mocking",
        "Topic :: Software Development :: Testing :: Unit",
    ],
    python_requires='>=3.6',
)
