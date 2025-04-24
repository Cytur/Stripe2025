import pygame




class Deer():
    def __init__(self, xcor:int, ycor:int):
        self.speed = 10
        self.xcor = xcor
        self.ycor = ycor
        self.Rect = pygame.Rect((self.xcor, self.ycor), (288, 288))
        
        self.frames = []

        for img in range(5):
            image=pygame.image.load(f'DeerAsset/deer{img+1}.png')
            image = pygame.transform.scale(image, (160, 128))
            self.frames.append(image)
        

        self.frame_count = 0
        self.current_frame = self.frames[self.frame_count]

    def animation_update(self):
        self.frame_count += 1
        if self.frame_count == len(self.frames):
            self.frame_count = 0
        self.current_frame = self.frames[self.frame_count]


    def jump(self, direction):
        pass
        #Abdullah u mind doing this part, idk what to do


        self.Rect = pygame.Rect((self.xcor, self.ycor), (256, 256))