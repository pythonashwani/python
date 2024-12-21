from github import Github
gitCred = open("./git_credential", "r");
token = gitCred.readline();
g = Github(token)
# Get the authenticated user
user = g.get_user("pythonashwani")
# List repositories
for repo in user.get_repos():
    print(f"Repository Name: {repo.name}")