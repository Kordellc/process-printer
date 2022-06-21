import psutil


def get_proccesses():
    procList = []
    ids = psutil.pids()
    for proc in ids:
        procList.append(psutil.Process(proc).name())
    return procList


def printList(procList):
    with open('processes.txt', 'w') as f:
        f.write('\n'.join(procList))
    pass


if __name__ == '__main__':
    proc_list = get_proccesses()
    printList(proc_list)