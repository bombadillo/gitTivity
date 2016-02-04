import repoRetriever as repoRetriever
from ..models.commit import Commit

def getLogsForBranches(branches):
    repo = repoRetriever.retrieve()
    for branch in branches:
        commitList = []
        commits = list(repo.iter_commits(branch.name))
        for commitItem in commits:
            commit = Commit()
            commit.author = commitItem.author
            commit.committed_date = commitItem.committed_date
            commit.committer = commitItem.committer
            commit.message = commitItem.message
            commit.summary = commitItem.summary
            commitList.append(commit)
        branch.commits = commitList
    return branches
