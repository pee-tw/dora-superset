from github import Github

github_token = "<replace_me>"
g = Github(github_token)

repo = g.get_repo("pee-tw/dora-superset")

commits = repo.get_commits()

for commit in commits:
    print(commit.commit.message)
    print(commit.commit.author.date)
