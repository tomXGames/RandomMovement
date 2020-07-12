
def setup():
    size(600, 600)
    global mv
    mv = mover()
    noiseSeed(int(random(100)))
    
def draw():
    background(255)
    #if frameCount %5 == 0:
    mv.update(frameCount)
    mv.show()    

class mover:
    x = 600/2
    y = 600/2
    
    def update(self, timeStep):
        self.angle = map(noise(timeStep//10), 0, 1, 0, 360)
        circle(self.x , self.y, 10)
        self.speed = 1
        self.xoff = self.speed * cos(self.angle)
        self.yoff = self.speed * sin(self.angle)
        self.x += self.xoff
        self.y += self.yoff
    def show(self):
        circle(self.x , self.y, 10)
        
