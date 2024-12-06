from setuptools import setup, find_packages
setup(
    name="ModelPK",
    version="0.1",
    packages=find_packages(),
    install_requires=["tellurium","numpy","pandas","python-dateutil","scikit-learn","scipy",
                      "six","threadpoolctl","tzdata","joblib","pytz"
    ],
    author="Jia Liang",
    author_email="jyliang@uw.edu",
    description="A brief description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jyliang27/ModelPK",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)