from universe import universe
from tkinter import * 
import tkinter.ttk
import time
from PIL import Image , ImageTk
import numpy as np 

if __name__ == '__main__':
    u = universe() 
    root = Tk()
    can = Canvas( root , height = 500 , width = 500 )
    can.pack()
    trance = {  }
    graph = np.zeros( (500 , 500) )

    for i in range( 100000000 ):
        u.next()
        stars = u.show()
        for star in stars :
            weight = star.getMass()
            point = ( int( star.getPosition()[ 0 ] ) + 250 , int( star.getPosition()[ 1 ] ) + 250 )
            for i in range( point[ 0 ] - weight , point[ 0 ] + weight ):
                for j in range( point[ 1 ] - weight , point[ 1 ] + weight ) :
                    graph[ i , j ] = 255 
                    
        
        pilImage = Image.fromarray( graph )
        image_show = ImageTk.PhotoImage( pilImage )
        image_sprite = can.create_image( 250 , 250 , image = image_show )
        root.update()

    root.mainloop()