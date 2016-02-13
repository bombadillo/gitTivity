
import json
def convertAll(commits):
    commitList = []
    for commit in commits:
        commitObj = {}
        commitObj['authorName'] = commit.author.name
        commitObj['authorEmail'] = commit.author.email
        commitObj['committed_date'] = commit.committed_date
        commitObj['committer'] = commit.message
        commitObj['summary'] = commit.summary
        commitObj['parents'] = convertParents(commit)
        commitList.append(commitObj)
    return commitList

def convertParents(commit):
    parents_list = []
    for parent in commit.parents:
        parents_list.append(str(parent))
    return json.dumps(parents_list)
