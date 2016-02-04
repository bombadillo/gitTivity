from git import Repo
from config import Config

def retrieve():
    repoDir = Config.repoUrl
    repo = Repo(repoDir)
    return repo
