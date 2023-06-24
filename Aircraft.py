class Aircraft():

    def __init__(self, fuel, engines, lights, collisionLights, rudders, hydraulicsSystem):
        self.fuel = fuel
        self.engines = engines
        self.lights = lights
        self.collisionLights = collisionLights
        self.rudders = rudders
        self.hydraulicsSystem = hydraulicsSystem

    def CheckStatusAircraft(self):
        if self.fuel and self.engines and self.lights and self.collisionLights and self.rudders\
                and self.hydraulicsSystem:
            print('Components of the aircraft are in good technical condition')
        else:
            print('Error in the security process!!!!')