from random import randint
class Dragon:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def kill(self,target): 
        if self.health <= 0 :
            print '%s is dead' %self.name
        elif C[target.name].health <=0:
                print '%s has died' %target.name
        else:
            while self.health > 0 or C[target.name].health > 0:
                if C[target.name].health <= 50:
                    hit = randint(1,20)
                    target.health -= hit
                    print '%s hits %s for %s' %(self.name,target.name,hit)
                elif C[target.name].health > 50:
                    hit = randint(1,50)
                    if hit >= 40:
                        C[target.name].health -= hit
                        print "%s critically hits %s for %s" %(self.name,target.name,hit)
                    else:
                        C[target.name].health -= hit
                        print "%s hits %s for %s" %(self.name,target.name, hit)
                    C[target.name].kill(C[self.name])
                elif self.health <= 0 :
                    print '%s is dead' %self.name
                    break
                elif C[target.name].health <=0:
                    print '%s has died' %target.name
                    break
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
        if self.health <= 0 :
            print '%s is dead' %self.name
        elif C[target.name].health <=0:
                print '%s has died' %target.name
        else:
            while self.health > 0 or C[target.name].health > 0:
                if C[target.name].health <= 50:
                    hit = randint(1,20)
                    target.health -= hit
                    print '%s hits %s for %s' %(self.name,target.name,hit)
                elif C[target.name].health > 50:
                    hit = randint(1,50)
                    if hit >= 40:
                        C[target.name].health -= hit
                        print "%s critically hits %s for %s" %(self.name,target.name,hit)
                    else:
                        C[target.name].health -= hit
                        print "%s hits %s for %s" %(self.name,target.name, hit)
                    C[target.name].kill(C[self.name])
                elif self.health <= 0 :
                    print '%s is dead' %self.name
                    break
                elif C[target.name].health <=0:
                    print '%s has died' %target.name
                    break
    def IsDead(self):
        if self.health <= 0:
            return True
        else:
            return False
Alice = Dragon('Alice',100)
Fahad = Hero('Fahad', 100)
C = {'Alice':Alice,'Fahad':Fahad}
if __name__ == '__main__':
    Alice.kill(Fahad)

