from math import *
# 1 mm = 3.793627 px
alpha = 1/3.793627  # coefficient for translation mm ---> px
R = 6372795 #meters
# (0,0) ---> (1920/2, 1080/2) new center (960, 540)

for_round = 6 # for round float format .6

class Camera:
    def __init__(self, lat, lon, alt, roll, pitch, yaw, px, py, f, m_a, m_b):
        self.lat = radians(lat)  # latitude(deg)
        self.lon = radians(lon)  # longitude(deg)
        self.alt = alt  # altitude(meters)
        self.roll = roll  # roll(degrees)
        self.pitch = pitch  # pitch(degrees)
        self.yaw = yaw  # yaw(°degrees)
        self.f = f/1000  # focal length(mm) ---> convert to metres
        self.matrix_x = m_a  # matrix side, px
        self.matrix_y = m_b  # matrix side, px
        self.px = px - matrix_x/2  # pixel X coordinate in the image, px
        self.py = (py - matrix_y/2) * (-1)  # pixel Y coordinate in the image, px
        self.azimut = 0
    def get_x_position_ideal(self):
        if self.f != 0:
            return (self.px * alpha * self.alt)/(1000 * self.f)
        else:
            return 0
    def get_y_position_ideal(self):
        if self.f != 0:
            return (self.py * alpha * self.alt)/(1000 * self.f)
        else:
            return 0
    def set_azimut(self):
        self.azimut = atan(self.get_x_position_ideal()/self.get_y_position_ideal())
    def get_distance(self):
        ix = round(self.lat + self.get_x_position_ideal(), for_round)
        iy = round(self.lon + self.get_y_position_ideal(), for_round)
        return sqrt(pow(ix,2)+pow(iy,2))
    def get_coordinates(self):
        lat2 = asin(sin(self.lat)*cos(self.get_distance()/R) + cos(self.lat)*sin(self.get_distance()/R)*cos(self.azimut))
        lon2 = self.lon + atan2(sin(self.azimut)*sin(self.get_distance()/R)*cos(self.lat), cos(self.get_distance()/R) - sin(self.lat) * sin(lat2))
        return degrees(lat2),degrees(lon2)



if __name__ == "__main__":
    f = 50  # 50mm
    matrix_x, matrix_y = 1920, 1080  # in px
    px = 720
    py = 240
    lat = 64.587222
    lon = 30.596944
    alt = 50000
    roll = 0
    pitch = 0
    yaw = 0
    # find coordinates in real life in ideal conditions
    camera = Camera(lat, lon, alt, roll, pitch, yaw, px, py, f, matrix_x, matrix_y)
    # дрон смотрит на строго север
    camera.set_azimut()
    print(degrees(camera.lat), degrees(camera.lon))
    print(camera.get_x_position_ideal(),camera.get_y_position_ideal())
    print(*camera.get_coordinates())
    #print(camera.azimut)