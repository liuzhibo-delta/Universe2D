from star import star


class universe:
    def __init__( self ):
        self.stars = []
        self.stars.append( star( ( -100 , 0 ) , 1 , ( 0 , 10 ) ) )
        self.stars.append( star( ( 100 , 0  ) , 1 , ( 0 , -10 ) ) )
        self.stars.append( star( ( 0 , 100*pow( 3.0 , 1/2 ) ) , 1 , ( 20 , 0 ) ) )
    
    def next( self ):
        '''
        calculate the next state of the universe .
        '''
        for i in range( len( self.stars ) ) :
            self.stars[ i ].broadcast( self.stars[ : i ] + self.stars[ i+ 1 : ] )
            self.stars[ i ].next()
    
    def show( self ):
        '''
        return a list of position
        '''
        return self.stars