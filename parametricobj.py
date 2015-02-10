import math
import rhinoscriptsyntax as rs

pi = math.pi
LayerRotation = 0.0

#height of column
#height = 25.0
height = rs.GetReal("Enter column height (between 5 and 30)", 15, 5, 30)
#radius of column
#radius = 5.0
radius = rs.GetReal("Enter column radius (between 2 and 10)", 2, 2, 10)
spheresize = radius / 10
#spacing of spheres in circle
spacing1 = pi/30
spacing2 = spacing1*2

#height of base
#base = 8.75
base = rs.GetReal("Enter height of stand (between 5 and 10)", 8.75, 5, 10)
list_of_points = [(radius + 5, 0, 0), (radius + 2.22, 0, 2.5), (radius + 7.08, 0, 4.5), (radius + 4.7, 0, 7.5), (radius, 0, base)]


rs.EnableRedraw(False)

baseCurve = rs.AddCurve(list_of_points)
rs.AddRevSrf(baseCurve,((0,0,0), (0,0,1)))


for z in rs.frange(base, height+base, spheresize):
    LayerRotation = LayerRotation + spacing1
    for theta in rs.frange(0.0, 2*pi, spacing2):
        x = radius *  math.cos(theta + LayerRotation)
        #print("The value of x is ", x)
        y =  radius * math.sin(theta + LayerRotation)
        #print("The value of y is ", y)
        mySphere = rs.AddSphere([x,y,z], spheresize)

nextheight = height+radius

candle_base = [(radius, 0, height+base), (radius, 0, height+base+2), (radius+3.63, 0, height+base+2), (radius+3.63, 0, height+base+4), (0,0,height+base+4)]
candleBaseCurve = rs.AddCurve(candle_base)
rs.AddRevSrf(candleBaseCurve,((0,0,0),(0,0,1)))

candleHeight = 15
topSleeve = rs.AddCylinder((0,0,height+base+4), candleHeight, radius)


flame = [(0,0,height+base+4+candleHeight), (1.78,0,height+base+4+candleHeight+2), (2,0,height+base+4+candleHeight+3),(0.71,0,height+base+4+candleHeight+4),(0,0,height+base+4+candleHeight+6)]
flameCurve = rs.AddCurve(flame)
rs.AddRevSrf(flameCurve,((0,0,0),(0,0,1)))


rs.EnableRedraw(True)