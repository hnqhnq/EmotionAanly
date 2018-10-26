import codecs
import copy

class Context:
    def __init__(self):
        self.__props = {}

    def init(self, filePath):
        with codecs.open(filePath, "r", "utf-8") as file:
            for line in file:
                line = line.strip()
                if line and line[0] != "#":
                    pos = line.find("==")
                    if pos > -1:
                        key = line[0:pos].strip()
                        value = line[pos + 2:].strip()
                        self.__props[key] = value
                    elif len(line.strip()) > 0:
                        try:
                            self.__props[key] += (" "+line.strip())
                        except:
                            print("please check your sentence!!")

    def getProperty(self, key, defaultValue=None):
        value = self.__props.get(key)
        if value is None:
            return defaultValue
        return value

    def setProperty(self, key, value):
        self.__props[key] = value

    def getProperties(self):
        return copy.deepcopy(self.__props)

    def getInt(self, key, defaultValue=None):
        v = self.getProperty(key, defaultValue)        
        return int(v)

    def getFloat(self, key, defaultValue=None):
        v = self.getProperty(key, defaultValue)
        return float(v)

    def getString(self, key, defaultValue=None):
        return self.getProperty(key, defaultValue)

    def getBoolean(self, key, defaultValue=None):
        v = self.getProperty(key, defaultValue)
        if v == "True":
            return True
        elif v == "False":
            return False
        return bool(v)

    def getKeys(self):
        vs = set()
        for k in self.__props:
            vs.add(k)
        return vs

    def getValues(self):
        vs = list()
        for k in self.__props:
            vs.append(self.__props[k])
        return vs

    def __str__(self):
        return str(self.__props)

    def __repr__(self):
        return repr(self.__props)
