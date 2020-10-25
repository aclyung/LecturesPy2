import numpy

radius = int(input("반지름: "))
area = (radius ** 2) * numpy.pi
cer = numpy.pi * 2 * radius
print("넓이: {}, 둘레: {}".format(area, cer))
print("%.20f" % numpy.pi)
