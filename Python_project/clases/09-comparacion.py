class Coordenadas:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon
    #igual
    def __eq__(self, value):
        return self.lat == value.lat and self.lon == value.lon   
    
    #no igual
    #def __ne__(self, value):
    #    return self.lat != value.lat or self.lon != value.lon
    
    #mayor menor que
    def __lt__(self, value):
        return self.lat + self.lon < value.lat + value.lon
    
    #menor/mayor o igual que
    def __le__(self, value):
        return self.lat + self.lon <= value.lat + value.lon      
    
coords = Coordenadas(45,98)
coords2 = Coordenadas(45,98)
coords3 = Coordenadas(46,98)
coords4 = Coordenadas(45,98)
coords5 = Coordenadas(48,98)


print(coords == coords2)
print(coords != coords2)
print(coords < coords3)
print(coords > coords3)
print(coords <= coords4)
print(coords4 >= coords5)