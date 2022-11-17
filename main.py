from math import *
# 1 mm = 3.793627 px
alpha = 1/3.793627  # coefficient for translation mm ---> px
R = 6372795 #meters
# (0,0) ---> (1920/2, 1080/2) new center (960, 540)

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

    # Camera position x
    def get_x_position_ideal(self):
        if self.f != 0:
            return (self.px * alpha * self.alt)/(1000 * self.f)
        else:
            return 0

    # Camera position y
    def get_y_position_ideal(self):
        if self.f != 0:
            return (self.py * alpha * self.alt)/(1000 * self.f)
        else:
            return 0

    def set_azimut(self):
        if self.get_y_position_ideal() != 0:
            self.azimut = atan(self.get_x_position_ideal()/self.get_y_position_ideal())

    # Distance to object
    def get_distance(self):
        ix = self.lat + self.get_x_position_ideal()
        iy = self.lon + self.get_y_position_ideal()
        return sqrt(pow(ix,2)+pow(iy,2))

    # Coordinates of object
    def get_coordinates(self):
        lat1 = self.lat # Latitude of the first point
        lon1 = self.lon # Longitude of the first point
        azimut = self.azimut # Start bearing
        delta = self.get_distance()/R
        lat2 = asin(sin(lat1)*cos(delta) + cos(lat1)*sin(delta)*cos(azimut)) # Latitude of the second point
        lon2 = lon1 + atan2(sin(azimut)*sin(delta)*cos(lat1), cos(delta) - sin(lat1) * sin(lat2)) # Longitude of the second point
        return degrees(lat2),degrees(lon2)


if __name__ == "__main__":
    f = 530  # 50mm
    matrix_x, matrix_y = 1920, 1080  # in px
    px = 80
    py = 320
    lat = 59.973017
    lon = 30.220557
    alt = 50
    roll = 0
    pitch = 0
    yaw = 0
    # Find coordinates in real life in ideal conditions
    camera = Camera(lat, lon, alt, roll, pitch, yaw, px, py, f, matrix_x, matrix_y)
    # дрон смотрит строго на север
    camera.set_azimut()

    print('\nDrone latitude: ', degrees(camera.lat),
          '\nDrone longitude', degrees(camera.lon))

    print('\nDistance to obj x', camera.get_x_position_ideal(),
          '\nDistance to obj y', camera.get_y_position_ideal(),
          '\nDistance to obj', camera.get_distance())

    obj_lat, obj_lon = camera.get_coordinates()
    print('\nObject latitude', obj_lat,
          '\nObject longitude', obj_lon)

    #print(*camera.get_coordinates())
    #print(camera.azimut)

    # ДАННЫЕ ЗНАЧЕНИЯ НАХОДЯТ КООРДИНАТЫ ТОЧКИ НА ПОЛЕ ЗЕНИТА
    #59.973017000000006 30.220557
    #-21.88377189547847 5.470942973869618
    #59.973064281098495 30.220179054598162