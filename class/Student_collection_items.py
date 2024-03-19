class student:
    def __init__(self,roll,name,marks:list):
        self.roll=roll
        self.name=name
        self.marks=marks

    def display_details(self):
        print(f"roll_no:{self.roll}\nname:{self.name}\n")

    def percentage(self):
        total=0
        for i in self.marks:
            total+=i
        per=(total/400)*100
        print("Percentage of marks=",per)
    
s1=student('00abc1','shyam',[90,70,60,80])
s1.display_details()
s1.percentage()

    