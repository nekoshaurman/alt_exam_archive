from math import *
# 1 mm = 3.793627 px
alpha = 1/3.793627  # coefficient for translation mm ---> px
# (0,0) ---> (1920/2, 1080/2) new center (960, 540)

for_round = 6


class Camera:
    def __init__(self, lat, lon, alt, roll, pitch, yaw, px, py, f, m_a, m_b):
        self.lat = lat  # latitude(deg)
        self.lon = lon  # longitude(deg)
        self.alt = alt  # altitude(meters)
        self.roll = roll  # roll(degrees)
        self.pitch = pitch  # pitch(degrees)
        self.yaw = yaw  # yaw(°degrees)
        self.f = f/1000  # focal length(mm) ---> convert to metres
        self.matrix_x = m_a  # matrix side, px
        self.matrix_y = m_b  # matrix side, px
        self.px = px - matrix_x/2  # pixel X coordinate in the image, px
        self.py = (py - matrix_y/2) * (-1)  # pixel Y coordinate in the image, px


    def get_x_position_ideal(self):
        if self.alt != 0 and self.px != 0:
            return (self.px * alpha * self.alt)/(1000 * self.f)
        else:
            return 0

    def get_y_position_ideal(self):
        if self.alt != 0 and self.py != 0:
            return (self.py * alpha * self.alt)/(1000 * self.f)
        else:
            return 0

    def get_coordinates_ideal(self):
        return round(self.lat + self.get_x_position_ideal(), for_round), \
               round(self.lon + self.get_y_position_ideal(), for_round), \
               self.alt


if __name__ == "__main__":
    f = 50  # 50mm
    matrix_x, matrix_y = 1920, 1080  # in px
    px = 720
    py = 240
    lat = 59.966782
    lon = 30.309607
    alt = 200
    roll = 0
    pitch = 0
    yaw = 0
    # find coordinates in real life in ideal conditions
    camera = Camera(lat, lon, alt, roll, pitch, yaw, px, py, f, matrix_x, matrix_y)
 ##
    print(camera.get_coordinates_ideal())