import gitHelpers.repoRetriever as repoRetriever
import gitHelpers.branch as branch
import gitHelpers.commitRetriever as commitRetriever
import services.saveRepoData as saveRepoData

def start():
    repo = repoRetriever.retrieve()
    branches = branch.getBranches(repo)
    branches = commitRetriever.getLogsForBranches(branches)
    saveRepoData.save(branches)
