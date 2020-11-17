from pathlib import Path
import json
import re
import os

class bcolors:
    HEADER = '\033[95m'
    RESET = '\033[0m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKRED = '\033[31m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class Device: 
    def __init__(self):
        self._deviceConfig = ""
        self._deviceType = ""
        self._deviceName = ""
        self._deviceVersion = ""

    def __init__(self, filePath, benchmarkPath):
        self._deviceConfig = ""
        self._deviceType = ""
        self._deviceName = ""
        self._deviceVersion = ""
        self._benchmarkPath = Path(benchmarkPath)
        deviceConfigurationFile = Path(filePath)
        if os.path.exists(deviceConfigurationFile):
            with open(deviceConfigurationFile, 'r') as f:
                for line in f.readlines():
                    self._deviceConfig += line
            
            if self._deviceConfig:
                self.extractConfigurationDetails()
            else:
                print("[**] ParseError -- Unable to parse configuration file")

        else:
            #TODO: Replace this with some sort of PYthon logging/actual error handling
            print("[**] ConfigError -- File \"%s\" not found" % deviceConfigurationFile)

    def output(self):
        print("Device Hostname: %s\nDevice Type: switch\nDevice Version: %s" % (self._deviceName, self._deviceVersion))


    def extractConfigurationDetails(self):
        searchString = "hostname"
        #TODO: not this..
        self._deviceName = self._deviceConfig[self._deviceConfig.find(searchString) + len(searchString):].split('\n')[0]
        searchString = "version"
        self._deviceVersion = self._deviceConfig[self._deviceConfig.find(searchString) + len(searchString):].split('\n')[0]

    def performAudit(self):
        with open(self._benchmarkPath, 'r') as f:
            data = json.load(f)
        

        print(bcolors.HEADER + "Performing CIS Level 1 Benchmark Audit for%s" % self._deviceName + bcolors.RESET)
        for benchmark in data['benchmarks']:
            print("#" * 20)
            print(bcolors.BOLD + bcolors.UNDERLINE + benchmark['name'] + bcolors.RESET)
            print(bcolors.BOLD + bcolors.OKCYAN + "Description: " + bcolors.RESET + benchmark['description'])
            if benchmark['searchstring'][0] in self._deviceConfig:
                print(bcolors.BOLD + self._deviceName + bcolors.OKGREEN + " Passes!" + bcolors.RESET)
            else:
                print(bcolors.BOLD + self._deviceName + bcolors.OKRED + " Fails!" + bcolors.RESET)
                print(bcolors.BOLD + bcolors.OKCYAN + "Remediation: " + bcolors.RESET + benchmark['remediation'])
                print(bcolors.BOLD + bcolors.OKCYAN + "Potential Impact: " + bcolors.RESET + benchmark['impact'])
                    
            print("#" * 20 + "\n")














											
