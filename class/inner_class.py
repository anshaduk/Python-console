class Employee:
    class Company:
        def __init__(self,name,loc,dir,c_manager):
            self.name=name
            self.loc=loc
            self.dir=dir
            self.c_manager=c_manager
    
    def __init__(self,name,emp_id,c_name,c_loc,c_dir,c_c_manager):
        self.name=name
        self.emp_id=emp_id
        self.company=Employee.Company(c_name,c_loc,c_dir,c_c_manager)
    
    def show_details(self):
        print(f"name:{self.name}\nid:{self.emp_id}\ncomp_name:{self.company.name}\nlocation:{self.company.loc}")

e1=Employee("Anshad",1002,'ABCD','calicut','XYZ','mno')   
e1.show_details()     
        