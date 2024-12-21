from github import Github
# Replace 'your_access_token' with your actual GitHub token
gitCred = open("./git_credential", "r");
token = gitCred.readline();
g = Github(token)
# Get the authenticated user
user = g.get_user()

# Get a specific repository
repo = g.get_repo(user.login+"/test-repo1")

# Create an issue
issue = repo.create_issue(title="Test Issue", body="This is a test issue.")
print(f"Issue created: {issue.title}")