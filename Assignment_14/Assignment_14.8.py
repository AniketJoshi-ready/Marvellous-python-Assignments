class vehicle :
    def start(self) :
        print("I am any vehicle ")
class car(vehicle):
    def start(self):
        print("i am perticularly a CAR ")    
def main():
    vobj=vehicle()
    vobj.start()

    cobj=car()
    cobj.start()
if __name__=="__main__":
    main() 