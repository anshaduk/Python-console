class Company:
    def __init__(self,name,loc,dir,c_manager):
        self.c_name=name
        self.loc=loc
        self.dir=dir
        self.c_manager=c_manager


class Employee:
    def __init__(self,name,emp_id,age,comp:Company):
        self.name=name
        self.emp_id=emp_id
        self.age=age
        self.company=comp
    def show_details(self):
        print(f"name:{self.name}\nemp_id:{self.emp_id}\ncompany_name:{self.company.c_name}\n"
              f"location:{self.company.loc}")

c_obj=Company("ABCD",'calicut',"XYZ","mno")
e1=Employee("shyam","1100",29,c_obj)
e1.show_details();