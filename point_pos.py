import math

def camera_object_distance(lat1, long1, lat2, long2):

    # pi - число pi, rad - радиус сферы (Земли)
    rad = 6372795

    # в радианах
    latit_1 = lat1 * math.pi / 180.
    latit_2 = lat2 * math.pi / 180.
    longit_1 = long1 * math.pi / 180.
    longit_2 = long2 * math.pi / 180.

    # косинусы и синусы широт и разницы долгот
    cl1 = math.cos(latit_1)
    cl2 = math.cos(latit_2)
    sl1 = math.sin(latit_1)
    sl2 = math.sin(latit_2)
    delta = longit_2 - longit_1
    c_delta = math.cos(delta)
    s_delta = math.sin(delta)

    # вычисления длины большого круга
    y = math.sqrt(math.pow(cl2 * s_delta, 2) + math.pow(cl1 * sl2 - sl1 * cl2 * c_delta, 2))
    x = sl1 * sl2 + cl1 * cl2 * c_delta
    ad = math.atan2(y, x)
    dist = ad * rad

    # вычисление начального азимута
    x = (cl1 * sl2) - (sl1 * cl2 * c_delta)
    y = s_delta * cl2
    z = math.degrees(math.atan(-y / x))

    if (x < 0):
        z = z + 180.

    z2 = (z + 180.) % 360. - 180.
    z2 = - math.radians(z2)
    anglerad2 = z2 - ((2 * math.pi) * math.floor((z2 / (2 * math.pi))))
    angledeg = (anglerad2 * 180.) / math.pi

    print('Distance >> %.0f' % dist, ' [meters]')
    print('Initial bearing >> ', angledeg, '[degrees]')

def object_coordinates(lat_drone, long_drone, dist):

    rad = 6372795

    angle = 0
    latit_1 = lat_drone * math.pi / 180.
    longit_1 = long_drone * math.pi / 180.

    #latit_2 =
    #longit_2 =


    #print('Object on >> ' lat_obj, long_obj)
    #print('Distance >> %.0f' % dist, ' [meters]')
    #print('Initial bearing >> ', angledeg, '[degrees]')


x1 = 60.067734
y1 = 30.334748
x2 = 60.068460
y2 = 30.331156
camera_object_distance(x1, y1, x2, y2)