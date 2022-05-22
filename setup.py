import setuptools

install_requires = [
            'pandas',
            'xlrd',
            'matplotlib',
            'numpy',
            'scipy',
            'seaborn',
            'sklearn',
            'xgboost',
            'tqdm',
        ]


setuptools.setup(
    name="ghlearn",
    version="1.0.0",
    author="Soumen Ganguly",
    description="Time Series Prediction Model for GreenHouse Air Temperature",
    packages=setuptools.find_packages(include=('ghlearn', 'ghlearn.*')),
    python_requires=">=3.6",
    install_requires=install_requires,
    package_data={'':['model_storage/*']},
)