from setuptools import setup, find_packages
base_packages = [
    "scikit-learn>=0.22.2",
    "numpy>=1.18.5",
    "rich>=10.4.0",
    "requests"
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="keybert",
    packages=find_packages(exclude=["notebooks", "docs"]),
    version="0.7.0",
    author="Maarten Grootendorst",
    author_email="maartengrootendorst@gmail.com",
    description="KeyBERT performs keyword extraction with state-of-the-art transformer models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaartenGr/keyBERT",
    keywords="nlp bert keyword extraction embeddings",
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=base_packages,
    python_requires=">=3.6",
)
