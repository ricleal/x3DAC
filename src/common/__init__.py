import os

def findFileInTheProject(fileName):
    """
    Attempts to locate a filename inside the project
    
    @return: the complete path of the file found
    """
    fileNameAttempt = os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.getcwd(),fileName)
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.getcwd(),os.path.join(os.pardir,fileName))
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    fileNameAttempt = os.path.join(os.getcwd(),"../",os.path.join(os.pardir,fileName))
    if os.path.exists(fileNameAttempt):
        return fileNameAttempt
    
    raise IOError("File not found in the Project: "+fileName)

def singleton(cls):
    """
    PEP318 :  Implementing the singleton pattern with a decorator.
    """
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance    