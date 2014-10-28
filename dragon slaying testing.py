from random import randint
class Dragon:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def kill(self,target): 
        if C[self.name].IsDead == True:
            print '%s is dead' %self.name
        elif self.IsDead == False:
            while C[target.name].IsDead() == False:
                if C[target.name].health <= 50:
                    hit = randint(1,20)
                    target.health -= hit
                    print '%s hits %s for %s' %(self.name,target.name,hit)
                else:
                    hit = randint(1,50)
                    if hit >= 40:
                        C[target.name].health -= hit
                        print "%s critically hits %s for %s" %(self.name,target.name,hit)
                    else:
                        C[target.name].health -= hit
                        print "%s hits %s for %s" %(self.name,target.name, hit)
                if C[target.name].IsDead():
                    print '%s has died' %target.name
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
        if C[self.name].IsDead == True:
            print '%s is dead' %self.name
        elif self.IsDead == False:
            while C[target.name].IsDead() == False:
                if C[target.name].health <= 50:
                    hit = randint(1,20)
                    target.health -= hit
                    print '%s hits %s for %s' %(self.name,target.name,hit)
                else:
                    hit = randint(1,50)
                    if hit >= 40:
                        C[target.name].health -= hit
                        print "%s critically hits %s for %s" %(self.name,target.name,hit)
                    else:
                        C[target.name].health -= hit
                        print "%s hits %s for %s" %(self.name,target.name, hit)
                if C[target.name].IsDead():
                    print '%s has died' %target.name
            C[target.name].kill(C[self.name])
    def IsDead(self):
        if self.health <= 0:
            return True
        else:
            return False
Alice = Dragon('Alice',200)
Fahad = Hero('Fahad', 100)
C = {'Alice':Alice,'Fahad':Fahad}
if __name__ == '__main__':
    Fahad.kill(Alice)
