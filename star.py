from setting import G , dt 

class star:
    def __init__( self , position = None , mass = None , v = None ):
        '''
        position = ( x , y )
        mass = int kg 
        v = ( x , y )
        '''
        self.position = position
        self.mass = mass
        self.v = v
        self.a = ( 0.0 , 0.0 )
        self.outside = []

    def broadcast( self , list_of_stars ):
        self.outside = list_of_stars 
        self.calculate_acclerate() 

        
    def calculate_acclerate( self ):
        '''
        return GMm/R^２
        '''
        self.a = ( 0.0 , 0.0 )
        for s in self.outside :
            Mass = s.getMass()
            position = s.getPosition()
            delta_r = ( position[ 0 ] - self.position[ 0 ] , position[ 1 ] - self.position[ 1 ] )
            self.a = ( self.a[ 0 ] + G*Mass*delta_r[ 0 ]/( pow( delta_r[ 0 ]*delta_r[ 0 ] + delta_r[ 1 ] *delta_r[ 1 ] , 3/2 ) ) , self.a[ 1 ] + G*Mass*delta_r[ 1 ]/( pow( delta_r[ 0 ]*delta_r[ 0 ] + delta_r[ 1 ] *delta_r[ 1 ] , 3/2 ) ) )



    def getMass( self ):
        return self.mass
    
    def getPosition( self ):
        return self.position 

    def next( self ):
        '''
        return the next state of stars .
        '''
        self.position = ( self.position[ 0 ] + self.v[ 0 ] * dt, self.position[ 1 ] + self.v[ 1 ] * dt )
        self.v = ( self.v[ 0 ] + self.a[ 0 ] * dt , self.v[ 1 ] + self.a[ 1 ] * dt )