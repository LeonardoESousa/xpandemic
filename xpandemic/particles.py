import numpy as np
import random
import sys

class Particles:
    def __init__(self,species,initial,ages):
        self.species  = species
        self.initial  = initial
        self.position = initial
        self.status   = 'alive'
        self.identity = random.uniform(0,5)
        self.report   = ''
        self.process  = None
        self.destination  = None
        self.Dx = 0
        self.Dy = 0
        self.Dz = 0
        self.age  = random.choices(list(ages.keys()), list(ages.values()))[0]

    def move(self,local,system):
        Dx, Dy, Dz = system.distance(system,self.position)
        self.Dx += Dx[local]
        self.Dy += Dy[local]
        self.Dz += Dz[local]
        self.position = local
        

    def make_text(self,system,energy,causamortis):
        time = system.time   
        X,Y,Z = system.X, system.Y, system.Z  
        Mats  = system.mats 
        x, y, z  = X[self.position],Y[self.position],Z[self.position]
        mat = Mats[self.position]
        #energy = energies[self.position]
        texto = f'{time:.0f},{self.Dx:.0f},{self.Dy:.0f},{self.Dz:.0f},{self.species},{energy:.0f},{mat:.0f},{x:.0f},{y:.0f},{z:.0f},{causamortis},{self.status}'
        self.report += texto+'\n'
    
    def kill(self,causamortis,system,energies,result):
        self.status = result
        self.make_text(system,energies,causamortis)
        system.remove(self)
    
    def write(self):
        return self.report


        
 
class Susceptible(Particles):
    def __init__(self,initial,ages):
        Particles.__init__(self,'Susceptible',initial,ages) 
        self.color  = "red"
        self.marker = "$S$"

class Exposed(Particles):
    def __init__(self,initial,ages):
        Particles.__init__(self,'Exposed',initial,ages) 
        self.color  = "orange"
        self.marker = "$E$"
        
class Infectious(Particles):
    def __init__(self,initial,ages):
        Particles.__init__(self,'Infectious',initial,ages) 
        self.color  = "green"
        self.marker = "$I$"
