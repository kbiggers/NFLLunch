from setuptools import find_packages
from setuptools import setup


setup(
    name="NFLLunch",
    project_urls={
        "Code": "https://github.com/kbiggers/NFLLunch",
        "Issue tracker": "https://github.com/kbiggers/NFLLunch/issues",
    },
    license="BSD-3-Clause",
    maintainer="Lunch Buds",
    description="NFL Lunch.",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    setup_requires=[
        "wheel",
        "pip",
    ],
    install_requires=[
        "ipython",
        "pytest",
        "Flask ",
        "beautifulsoup4",
        "click",
        "flask-rebar",
        "flask-marshmallow",
        "sleeper-api-wrapper",
        "nflgame-redux==2.0.1b1",
        "ff-espn-api"
    ],
)
