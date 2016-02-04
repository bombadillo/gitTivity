import json
import commitToJson
import fileWriter
from ..common.config import Config

def save(branches):
    branchesToOutput = {}
    for branchItem in branches:
        commits = commitToJson.convertAll(branchItem.commits)
        branchesToOutput[str(branchItem.name)] = [{"commits": commits}]

    data = json.dumps(branchesToOutput)
    fileWriter.writeString(data, Config.outputJsonFile)
