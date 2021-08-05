import PIL.Image, PIL.ImageDraw

class CirculoDDA:

    def __init__(self, radius):
        self.radius = radius
        
        

    def circle(self, radius):
        # init vars
        switch = 3 - (2 * radius)
        points = set()
        x = 0
        y = radius
        # first quarter/octant starts clockwise at 12 o'clock
        while x <= y:
            # first quarter first octant
            points.add((x,-y))
            # first quarter 2nd octant
            points.add((y,-x))
            # second quarter 3rd octant
            points.add((y,x))
            # second quarter 4.octant
            points.add((x,y))
            # third quarter 5.octant
            points.add((-x,y))        
            # third quarter 6.octant
            points.add((-y,x))
            # fourth quarter 7.octant
            points.add((-y,-x))
            # fourth quarter 8.octant
            points.add((-x,-y))
            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1
        return points

    def circle_main(self):
        size = 200
        radius = self.radius
        circle_graph = PIL.Image.new("RGB", (size, size), (30,25,20))
        draw = PIL.ImageDraw.Draw(circle_graph)
        p = self.circle(radius)
        # print the point coords
        print (p)
        for point in p:
            draw.point((size/2+point[0],size/2+point[1]),(255,255,255))
        circle_graph.show()

