from random import randint
class Dragon:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def kill(self,target): 
        while True:
            if self.health <= 0 :
                print '%s is dead' %self.name
                return False
                break
            elif C[target.name].health <=0:
                return False
                break
            else:
                if self.health > 0:
                        hit = randint(1,20)
                        target.health -= hit
                        print '%s hits %s for %s' %(self.name,target.name,hit)
                elif C[target.name].health > 0:
                        hit = randint(1,20)
                        target.health -= hit
                        print '%s hits %s for %s' %(self.name,target.name,hit)
                C[target.name].kill(C[self.name])
    def IsDead(self):
        if self.health <= 0:
            return True
        else:
            return False
class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def kill(self,target): 
        while True:
            if self.health <= 0 :
                print '%s is dead' %self.name
                return False
                break
            elif C[target.name].health <=0:
                return False
                break
            else:
                if self.health > 0:
                        hit = randint(1,20)
                        target.health -= hit
                        print '%s hits %s for %s' %(self.name,target.name,hit)
                elif C[target.name].health > 0:
                        hit = randint(1,20)
                        target.health -= hit
                        print '%s hits %s for %s' %(self.name,target.name,hit)
                C[target.name].kill(C[self.name])
    def IsDead(self):
        if self.health <= 0:
            return True
        else:
            return False
Alice = Dragon('Alice',10)
Fahad = Hero('Fahad', 30)
C = {'Alice':Alice,'Fahad':Fahad}
if __name__ == '__main__':
    Alice.kill(Fahad)

