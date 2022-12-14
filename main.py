from math import *
# 1 mm = 3.793627 px
alpha = 1/3.793627  # coefficient for translation mm ---> px
R = 6372795 #meters
# (0,0) ---> (1920/2, 1080/2) new center (960, 540)

class Camera:
    def __init__(self, lat, lon, orientation, alt, roll, pitch, yaw, px, py, f, m_a, m_b):
        self.lat = radians(lat)  # latitude(deg)
        self.lon = radians(lon)  # longitude(deg)
        self.orientation = radians(orientation) #Orientation relative to the North in degrees
        self.alt = alt  # altitude(meters)
        self.roll = roll  # roll(degrees)
        self.pitch = pitch  # pitch(degrees)
        self.yaw = yaw  # yaw(°degrees)
        self.f = f/1000  # focal length(mm) ---> convert to metres
        self.matrix_x = m_a  # matrix side, px
        self.matrix_y = m_b  # matrix side, px
        self.px = px - matrix_x/2  # pixel X coordinate in the image, px
        self.py = (py - matrix_y/2) * (-1)  # pixel Y coordinate in the image, px
        self.bearing = 0
        self.x = self.get_x_position()  # coordinates of the object relative to the projection of the camera on the ground
        self.y = self.get_y_position()  # coordinates of the object relative to the projection of the camera on the ground

    # Camera position x
    def get_x_position(self):
        if self.f != 0:
            return (self.px * alpha * self.alt)/(1000 * self.f)
        else:
            return 0

    # Camera position y
    def get_y_position(self):
        if self.f != 0:
            return (self.py * alpha * self.alt)/(1000 * self.f)
        else:
            return 0

    #Do the turn of coordinates, to face to //////////////////////// NORTH NOT ALREADY DONE
    def set_the_turn(self):
        x1 = self.x  # point coordinates in old basis
        y1 = self.y
        phi = self.orientation
        self.x = x1 * cos(phi) - y1 * sin(phi)  # point coordinates in old basis
        self.y = x1 * sin(phi) + y1 * cos(phi)


    # Start bearing to the point
    def set_bearing(self):
        if self.y != 0:
            self.bearing = atan(self.x / self.y)

    # Distance to object
    def get_distance(self):
        ix = self.lat + self.x
        iy = self.lon + self.y
        return sqrt(pow(ix, 2)+pow(iy, 2))

    # Coordinates of object in real life(latitude and longitude)
    def get_coordinates(self):
        lat1 = self.lat # Latitude of the first point
        lon1 = self.lon # Longitude of the first point
        self.set_the_turn()
        self.set_bearing()
        bearing = self.bearing # Start bearing
        delta = self.get_distance()/R
        lat2 = asin(sin(lat1)*cos(delta) + cos(lat1)*sin(delta)*cos(bearing)) # Latitude of the second point
        lon2 = lon1 + atan2(sin(bearing)*sin(delta)*cos(lat1), cos(delta) - sin(lat1) * sin(lat2)) # Longitude of the second point
        return degrees(lat2), degrees(lon2)


if __name__ == "__main__":
    f = 530  # 50mm
    matrix_x, matrix_y = 1920, 1080  # in px
    px = 80
    py = 320
    lat = 59.973017 # degrees
    orientation = 30 # degrees
    lon = 30.220557 # degrees
    alt = 50
    roll = 0
    pitch = 0
    yaw = 0
    # Find coordinates in real life in ideal conditions
    camera = Camera(lat, lon, orientation, alt, roll, pitch, yaw, px, py, f, matrix_x, matrix_y)
    # дрон смотрит строго на север, или в

    print('\nDrone latitude: ', degrees(camera.lat),
          '\nDrone longitude', degrees(camera.lon))

    print('\nIdeal conditions\nDistance from camera projection to obj by X axis', camera.x,
          '\nDistance from camera projection to obj by Y axis', camera.y,
          '\nDistance from camera projection to obj', camera.get_distance())

    obj_lat, obj_lon = camera.get_coordinates()
    print('\nObject latitude', obj_lat,
          '\nObject longitude', obj_lon)



    #print(*camera.get_coordinates())
    #print(camera.azimut)

    # ДАННЫЕ ЗНАЧЕНИЯ НАХОДЯТ КООРДИНАТЫ ТОЧКИ НА ПОЛЕ ЗЕНИТА
    # 59.973017000000006 30.220557
    # -21.88377189547847 5.470942973869618
    # 59.973064281098495 30.220179054598162