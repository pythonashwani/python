import subprocess

# Define the URL of the GitHub Repository
repo_url = "https://github.com/pythonashwani/test-repo1.git"
# Define the directory where you want to clone the repository
clone_dir = "./repo"
# Run the git clone command
subprocess.run(["git", "clone", repo_url, clone_dir])