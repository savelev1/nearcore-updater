#!/usr/bin/python3

import sys
import os
import time
import datetime

logFileName = 'nearcore-updater.log';
enableLog = True

def getFullPath(filename):
    return os.path.dirname(os.path.realpath(__file__)) + '/' + filename

def getNowDateString():
    now = datetime.datetime.now()
    return f'{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}:{now.second}:{now.microsecond}'

def logInFile(text):
    if enableLog == False:
        return
    open(getFullPath(logFileName), 'a')
    with open(getFullPath(logFileName), 'a') as file:
        file.write(f'[{getNowDateString()}] {text}\r\n')

def printAndLog(text):
    print(text)
    logInFile(text)

def plexit():
    printAndLog('exit()\r\n\r\n')
    exit()

if len(sys.argv) < 2:
    print('Missing argument <NETWORK>')
    exit();

if len(sys.argv) < 3:
    print('Missing argument <NEARCORE_DIR>')
    exit();

if len(sys.argv) >= 4:
    enableLog = bool(sys.argv[3])

network = sys.argv[1]
nearcoreDir = sys.argv[2]

printAndLog("Checking for updates")

currentVersion = os.popen(f'curl -s https://rpc.{network}.near.org/status | jq .version.version').read()
myVersion = os.popen('curl -s http://127.0.0.1:3030/status | jq .version.version').read()

if len(currentVersion):
    currentVersion = currentVersion[:-1]

if len(myVersion):
    myVersion = myVersion[:-1]

if currentVersion == myVersion:
    printAndLog(f'Versions are equal (rpc {currentVersion}, local {myVersion})')
    plexit()

printAndLog(f'Start update to {currentVersion}')

os.system(f'rm -rf {nearcoreDir}.backup');
os.system(f'mv {nearcoreDir} {nearcoreDir}.backup');
os.system(f'git clone -b {currentVersion} https://github.com/nearprotocol/nearcore.git {nearcoreDir}');
makeReleaseExitCode = os.system(f'cd {nearcoreDir} && make release');
if makeReleaseExitCode != 0:
    printAndLog('Build failed')
    plexit()
    
os.system('nearup stop');
os.system(f'nearup run localnet --binary-path {nearcoreDir}/target/release');

printAndLog('Run tests')

for count in range(4):
    rpcVersion = os.popen(f'curl -s https://rpc.{network}.near.org/status | jq .version').read()
    localVersion = os.popen(f'curl -s http://127.0.0.1:303{count}/status | jq .version').read()
    if rpcVersion == localVersion:
        printAndLog(f"Node {count} works")
    else:
        printAndLog(f"Node {count} don't works. Test failed.")
        os.system(f'mv {nearcoreDir}.backup {nearcoreDir}')
        os.system('nearup stop')
        os.system(f'nearup run {network} --binary-path {nearcoreDir}/target/release/ --nodocker')
        plexit()

printAndLog("Tests completed")
os.system('nearup stop')
os.system(f'nearup run {network} --binary-path {nearcoreDir}/target/release/ --nodocker')
printAndLog(f"Node updated. Current version {currentVersion} ({network})\r\n\r\n")
