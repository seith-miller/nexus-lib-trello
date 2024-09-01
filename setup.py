from setuptools import setup, find_packages

setup(
    name="nexus-lib-trello",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "py-trello",
        "langchain",
    ],
    author="Seith Miller",
    description="A LangChain tool for talking to Trello",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seith-miller/nexus-lib-trello",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
