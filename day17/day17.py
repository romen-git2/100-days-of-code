# complex subsystems
# these are the detailed classes that do the actual work
class LightSystem:
    def turn_on(self):
        print("Lights ON")
    def turn_off(self):
        print("Lights OFF")

class SecuritySystem:
    def arm(self):
        print("Security ARMED")
    def disarm(self):
        print("Security DISARMED")

class ClimateControl:
    def set_temperature(self, temp):
        print(f"Climate set to {temp}°C")

# the facade
# this hides the complexity of the subsystems
class SmartHomeFacade:
    def __init__(self):
        self.lights = LightSystem()
        self.security = SecuritySystem()
        self.climate = ClimateControl()

    def leave_house(self):
        """
        The agent calls this one method but it triggers 3 separate actions
        """
        print("Executing Leave House Sequence")
        self.lights.turn_off()
        self.climate.set_temperature(18) # save energy
        self.security.arm()
        print("Sequence Complete")

    def arrive_home(self):
        print("Executing Arrive Home Sequence")
        self.security.disarm()
        self.lights.turn_on()
        self.climate.set_temperature(22) # comfortable
        print("Sequence Complete")

# the agent
if __name__ == "__main__":
    # the agent doesn't need to know about LightSystem or SecuritySystem
    # it just deals with the facade
    home_bot = SmartHomeFacade()

    print("Owner is leaving for work.")
    home_bot.leave_house()

    print("Owner has returned.")
    home_bot.arrive_home()