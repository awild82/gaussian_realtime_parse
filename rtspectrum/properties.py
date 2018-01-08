from builtins import object

class DipoleVector(object):
    """A DipoleVector object contains the x, y, and z dipole 
    components

    Attributes:
        x: x component of the dipole
        y: y component of the dipole
        z: z component of the dipole
    """
    def __init__(self):
        self._x = None
        self._y = None
        self._z = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,value):
        self._y = value
 
    @property
    def z(self):
        return self._z

    @z.setter
    def z(self,value):
        self._z = value

'''
The following classes are defined for compatibility reasons
'''

class ElectricDipole(DipoleVector):
    pass

class MagneticDipole(DipoleVector):
    pass

class ElectricField(DipoleVector):
    pass

class MagneticField(DipoleVector):
    pass


