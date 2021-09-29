

class Button():
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = image

    # This function will draw images in x,y positions in window.
    def draw(self, gameDisplay):        
        gameDisplay.blit(self.image, (self.x, self.y))

    # Whether clicked or not.
    def clicked(self, pos):
        x, y = pos
        if self.x <= x and self.x + self.width >= x:
            if self.y <= y and self.y + self.height >= y:
                return True

        return False