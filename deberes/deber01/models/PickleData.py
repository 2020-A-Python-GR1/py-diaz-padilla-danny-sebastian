import pickle


def storeData(data, filename):
    # Modo binario
    dbfile = open(filename, 'ab')
    # fuente y destination
    pickle.dump(data, dbfile)
    dbfile.close()


def loadData(filename):
    # Modo binario
    dbfile = open(filename, 'rb')
    data = pickle.load(dbfile)
    dbfile.close()
    return data
