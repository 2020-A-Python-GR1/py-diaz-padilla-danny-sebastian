import pickle


def storeData(data, filename):
    # Modo binario
    dbfile = open(filename, 'wb')
    # fuente y destination
    pickle.dump(data, dbfile)
    dbfile.close()


def loadData(filename):
    """Solo carga datos diccionario por eso se devuelve un diccionario vacío en caso de no encontrar nada"""
    try:
        # Modo binario
        dbfile = open(filename, 'rb')
        data = pickle.load(dbfile)
        dbfile.close()
        return data
    except FileNotFoundError as error:
        print("Error al leer archivo en rb", error)
        return dict()
