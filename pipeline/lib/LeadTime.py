import os
import re
import pytz

from datetime import datetime

from github import Github

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
PROJECT_PREFIX = "GP-"

date_format = '%Y-%m-%dT%H:%M:%S.%f%z'


def calculate_lead_time(issue):
    release_with_issues = []
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo("pee-tw/dora-superset")
    releases = repo.get_releases()    
    for release in releases:
        issues = re.findall(f"{PROJECT_PREFIX}(\d+)", release.body)
        issues_with_prefix = list(map(lambda issue: f"{PROJECT_PREFIX}{issue}", issues))

        release_with_issues.append(
            {"issues": issues_with_prefix, "date": release.created_at}
        )
        
    released_on = None
    for release in release_with_issues:
        if issue.key in release["issues"]:
            released_on = release['date']
            tz = pytz.timezone('Asia/Bangkok')
            released_on = tz.localize(released_on)
            break
        
    if released_on == None:
        return 0
    
    return (released_on - datetime.strptime(issue.fields.created, date_format)).days