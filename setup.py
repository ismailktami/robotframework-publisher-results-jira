from setuptools import setup, find_packages
from PublisherJiraTestsResults.version import VERSION

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3'
]

setup(
  name='robotframework-publisher-results-jira',
  version=VERSION,
  description='Library to publish robot framework automation results on jira',
  author='Ismail Ktami',
  author_email='ktamiismail@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='robotframework jira xray testplans results outcomes', 
  packages=find_packages(),
  install_requires=[
    'robotframework>=3.2.2',
    'requests',
    'utils'
  ] 
)