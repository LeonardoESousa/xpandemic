
import numpy as np
import random
from xpandemic.particles import *

epsilon_vaccum = 8.854187e-12    #Permitivity in C/Vm
e              = -1.60217662e-19 #Electron charge    
kb             = 8.617e-5        #Boltzmann constant
hbar           = 6.582e-16       #Reduced Planck's constant



###RATES#################################################################################    

##FUNCTION FOR SETTING RADII#############################################################

def raios(num,Rf, mat, lifetime, mats):
  # Initialize the Raios array with the value of Rf[(mat,mat)]
  Raios = np.empty(num)
  Raios.fill(Rf[(mat,mat)])

  # Use NumPy's where function to set the values of Raios for the other materials
  for m in lifetime.keys():
    if m != mat:
      Raios = np.where(mats == m, Rf[(mat,m)], Raios)

  return Raios


#########################################################################################

##STANDARD FORSTER TRANSFER RATE#########################################################
class Walk:
    def __init__(self,**kwargs):
        self.kind = 'jump'
        self.Rf = kwargs['Rf']

    def rate(self,**kwargs):
        r      = kwargs['r']
        system = kwargs['system']
        ex     = kwargs['particle']
        mats   = system.mats    
        local  = ex.position    
        mat = mats[local]
        
        taxa = self.Rf[ex.age]/r
        taxa[r == 0] = 0
        return taxa


    def action(self,particle,system,local):
        particle.move(local,system)
#########################################################################################

class Incubation:
    def __init__(self,**kwargs):
        self.kind = 'incubation'
        self.time = kwargs['time']
        
    def rate(self,**kwargs):
        return 1/self.time
     
    def action(self,particle,system,local):
        system.set_particles([Infectious(particle.position)])
        particle.kill(self.kind,system,system.s1,'converted')
        
class Death:
    def __init__(self,**kwargs):
        self.kind = 'death'
        self.lifetime = kwargs['time']
        self.IFR      = kwargs['ifr']

    def rate(self,**kwargs):
        return self.IFR/self.lifetime
     
    def action(self,particle,system,local):
        particle.kill(self.kind,system,system.s1,'dead') 

class Cure:
    def __init__(self,**kwargs):
        self.kind = 'death'
        self.lifetime = kwargs['time']
        self.IFR      = kwargs['ifr']

    def rate(self,**kwargs):
        return (1-self.IFR)/self.lifetime
     
    def action(self,particle,system,local):
        particle.kill(self.kind,system,system.s1,'recovered') 
