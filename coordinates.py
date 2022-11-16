#Программа находит координаты второй точки зная координаты первой и расстояние между ними (TEST)
from math import *
R = 6372795 #meters

class Camera:
    def __init__(self, lat, lon, alt, roll, pitch, yaw):
        self.lat = radians(lat)  # latitude(deg)
        self.lon = radians(lon)  # longitude(deg)
        self.alt = alt  # altitude(meters)
        self.roll = roll  # roll(degrees)
        self.pitch = pitch  # pitch(degrees)
        self.yaw = yaw  # yaw(°degrees)
        self.azimut = 0
    def set_azimut(self):
        self.azimut = radians(180)
    def get_distance(self):
        return 600
    def get_coordinates(self):
        lat2 = asin(sin(self.lat)*cos(self.get_distance()/R) + cos(self.lat)*sin(self.get_distance()/R)*cos(self.azimut))
        lon2 = self.lon + atan2(sin(self.azimut)*sin(self.get_distance()/R)*cos(self.lat), cos(self.get_distance()/R) - sin(self.lat) * sin(lat2))
        return degrees(lat2),degrees(lon2)



if __name__ == "__main__":
    lat = 64.587222
    lon = 30.596944
    alt = 50000
    roll = 0
    pitch = 0
    yaw = 0
    # find coordinates in real life in ideal conditions
    camera = Camera(lat, lon, alt, roll, pitch, yaw)
    # дрон смотрит на строго север !!!!!!!!!!
    camera.set_azimut()
    print(degrees(camera.lat), degrees(camera.lon))
    print(*camera.get_coordinates())
    #print(camera.azimut)