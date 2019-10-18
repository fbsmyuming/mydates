import datetime
import time
def Important_Dates(date1,date2):
    Time_now=datetime.date.today()
    date3=Time_now.strftime("%Y/%m/%d")#把日期转为字符串

    date1=time.strptime(date1,"%Y/%m/%d")
    date2=time.strptime(date2,"%Y/%m/%d")
    date3=time.strptime(date3,"%Y/%m/%d")

    date1=datetime.datetime(date1[0],date1[1],date1[2])
    date2=datetime.datetime(date2[0],date2[1],date2[2])
    date3=datetime.datetime(date3[0],date3[1],date3[2])
    
    def get_days_passed_in_my_life():
        life=(date3-date1).days
        print("You have been living in this world for %d days!",%life)
    def get_days_passed_in_marriage():
        marri=(date3-date2).days
        print("You have been married for %d days!",%marri)
