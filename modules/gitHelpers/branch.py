from ..models.branch import Branch

def getBranches(repo):
    branchList = []
    branches = repo.heads
    for branchName in branches:
        branch = Branch()
        branch.name = branchName
        branchList.append(branch)
    return branchList
