import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="001",
    version="0.0.1",
    author="Matias Barreto",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },

license="MIT",
packages=["001"]
install_requires=["requests"],

)