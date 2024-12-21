from github import Github
gitCred = open("./git_credential", "r");
token = gitCred.readline();
g = Github(token)
# Get the authenticated user
user = g.get_user()
print(f"Username: {user.login}")
# Create a new repository
repo_name = "test-repo1"
repo = user.create_repo(repo_name)
print(f"Repository {repo_name} created successfully.")