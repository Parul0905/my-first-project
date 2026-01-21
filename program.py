#Smart Home Device Tracker(Application of OOPs concepts like attriibute shadowing,use of constructors etc).
#Create a class named SmartDevice
class SmartDevice:
  brand = "HomeTech"
  #Create a Constructor accepting device_name , power_status and also to Shadow the class atttribute.
  def __init__(self,device_name,power_status):
    self.device_name=device_name
    self.power_status=power_status
    self.brand="Custombrand"       #Attribute Shadowing

#Create a method to show status of the device
  def get_status():
    status="ON" if self.power_status else"OFF"
    return f"{self.device_name} is{self.power_status}-{self.brand}



