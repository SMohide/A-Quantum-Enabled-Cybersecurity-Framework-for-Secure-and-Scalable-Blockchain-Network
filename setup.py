"""
QECF Framework Setup

A Quantum-Enabled Cybersecurity Framework for
Secure and Scalable Blockchain Networks
"""

from setuptools import setup, find_packages

with open(
    "README.md",
    "r",
    encoding="utf-8"
) as fh:

    long_description = fh.read()

with open(
    "requirements.txt",
    "r",
    encoding="utf-8"
) as fh:

    requirements = [

        line.strip()

        for line in fh

        if line.strip()

        and not line.startswith("#")
    ]

setup(

    name="qecf-framework",

    version="1.0.0",

    author="Shravani Mohide",

    author_email="your-email@example.com",

    description=(
        "Quantum-Enabled Cybersecurity Framework "
        "for Secure and Scalable Blockchain Networks"
    ),

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/your-username/qecf-framework",

    packages=find_packages(),

    include_package_data=True,

    install_requires=requirements,

    python_requires=">=3.10",

    classifiers=[

        "Development Status :: 4 - Beta",

        "Intended Audience :: Science/Research",

        "Intended Audience :: Developers",

        "Topic :: Security :: Cryptography",

        "Topic :: Scientific/Engineering",

        "Topic :: Scientific/Engineering :: Artificial Intelligence",

        "Topic :: System :: Networking",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",

        "Programming Language :: Python :: 3.10",

        "Programming Language :: Python :: 3.11",
    ],

    keywords=[

        "blockchain",

        "cybersecurity",

        "quantum-computing",

        "post-quantum-cryptography",

        "qkd",

        "qrng",

        "distributed-systems",

        "consensus",

        "security-framework",

        "research"
    ],

    project_urls={

        "Paper":
            "https://doi.org/your-paper-doi",

        "Source":
            "https://github.com/your-username/qecf-framework",

        "Documentation":
            "https://github.com/your-username/qecf-framework/wiki"
    },
)
