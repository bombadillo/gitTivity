import json
import commitToJson
import fileWriter
import fileRemover
from modules.common.config import Config

def save(branches):
    branchesToOutput = {}
    for branchItem in branches:
        commits = commitToJson.convertAll(branchItem.commits)
        branchesToOutput[str(branchItem.name)] = [{"commits": commits}]

    data = json.dumps(branchesToOutput)
    fileRemover.remove(Config.outputJsonFile)
    fileWriter.writeString(data, Config.outputJsonFile)
