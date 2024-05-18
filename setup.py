import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_descrip = f.read()
    
Repo_name = "chicken-disease-classification"
User_name = "PdotRajkumar"

setuptools.setup(name = "cnnClassifier",
    version = "0.0.0",
    description="package for cnn app",
    long_description = long_descrip,
    long_description_content_type="text/markdown",
    author = "XYZ",
    author_email = "XYZ@mail.com",
    url=f"https://github.com/{User_name}/{Repo_name}",
    project_urls={"Bug Tracker": f"https://github.com/{User_name}/{Repo_name}/issues"}, 
    package_dir = {"":"src"},
    packages= setuptools.find_packages(where="src")
    
    
                )