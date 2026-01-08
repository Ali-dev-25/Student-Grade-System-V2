from dataclasses import dataclass

#بناء قاعدة بيانات بطريقة افضل 
@dataclass
class Student:
    std_id : str
    name : str
    email : str
    phone : str
    
    web_design: int
    info_sec: int
    comm_tech: int
    data_struct: int
    wireless_net: int
    comm_skill: int

    def calculate_average(self) -> float: #type Hint
        total = (self.web_design + self.info_sec + self.comm_tech +
                    self.data_struct + self.wireless_net + self.comm_skill)
        total = total /6
        return float(f"{total:.2f}")
        
    def validate(self):
        """Validate student data."""
        if not self.std_id or not self.name:
            raise ValueError("Student ID or name cannot be empty.")
        
        if not self.std_id.isdigit():
            raise ValueError("Error: ID must be NUmbers")
        
        if len(self.std_id) !=7:
            raise ValueError(f"Wrong! ID must be 7 digits(You entered {len(self.std_id)} digits).")
        
        if not self.phone.isdigit():
            raise ValueError("Phone must be Numbers")
        
        if len(self.phone) !=9:
            raise ValueError(f"Wron! Phone must be 9 digits (You entered {len(self.phone)} digits)")
        
        
        marks = [self.web_design, self.info_sec, self.comm_tech,
            self.data_struct, self.wireless_net, self.comm_skill]
        
        for mark in marks:
            if not isinstance(mark,(int,float)):
                raise ValueError("Marks must be numbers")
            if not(0 <= mark <= 100):
                raise ValueError(f"Mark {mark} is out of valid range (0-100).")

