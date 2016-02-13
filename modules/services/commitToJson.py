def convertAll(commits):
    commitList = []
    for commit in commits:
        commitObj = {}
        commitObj['authorName'] = commit.author.name
        commitObj['authorEmail'] = commit.author.email
        commitObj['committed_date'] = commit.committed_date
        commitObj['committer'] = commit.message
        commitObj['summary'] = commit.summary
        commitObj['parents'] = commit.parents
        commitList.append(commitObj)
    return commitList
