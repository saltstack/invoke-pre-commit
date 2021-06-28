from setuptools import setup


setup(
    name='pre_commit_dummy_package',
    version='0.0.0',
    scripts=["invoke-wrapper"],
    install_requires=['invoke==1.5.0'],
)
