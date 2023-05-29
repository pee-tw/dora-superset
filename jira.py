from jira import JIRA

PAT = "<replace_me>"
options = {'server': 'https://good-dora.atlassian.net'}
jira = JIRA(options, basic_auth=('ptankulrat@gmail.com', PAT))


issues = jira.search_issues('project = BE')
for issue in issues:
    print(issue.fields.summary)
    
    
issues = jira.search_issues('project = GP')
for issue in issues:
    print(issue.fields.summary)