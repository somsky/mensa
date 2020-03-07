import AbstractMenuSource
import pickle
import json

class PickleSource(AbstractMenuSource.AbstractMenuSource):
    def getMenu(self, address):
        raw = pickle.load(open(address, "rb"))
        try:
            menu = json.loads(raw.content)
        except:
            print('Error reading pickle file {}'.format(address))
            menu = []
        return menu
            

