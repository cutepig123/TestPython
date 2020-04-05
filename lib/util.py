import os

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))


def MySystem(cmd):
    print(cmd)
    os.system(cmd)


def info(object, spacing=10, collapse=1):
    "Print methods and doc strings.\n\t\tTakes module, class, list, dictionary, or string."
    methodList = [method for method in dir(
        object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s: %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList]))


def walkDirX(top, callback):
    for root, dirs, files in os.walk(top, topdown=False):
        callback(root, dirs, files)


def listDir(top, callback):
    for file in os.listdir(top):
        fullPath = os.path.join(top, file)
		callback(fullPath)
        if os.path.isdir(fullPath):
            listDir(fullPath)
