import datetime

def what_day(day, month, year):
    """ฟังก์ชั่นนี้จะบอกว่า day, month, year(ค.ศ.) คือวันอะไรของสัปดาห์"""
    date = datetime.date(year, month, day)
    day_of_week = date.weekday()
    return day_of_week

def is_leap_year(year):
    """เช็คว่า year เป็นปีอธิกสุรทิน ที่เดือนกุมภาพันธ์จะมี 29 วัน"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return 
    
def what_month(day,month,year):
    return datetime.date(year, month, day).strftime("%B")

def calendar(month, year):
    """ฟังก์ชั่นนี้จะพิมพ์ปฏิทินประจำเดือน month ของปี ค.ศ. year"""

    # จำนวนวันในแต่ละเดือน
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # ถ้าเป็น leap year เดือนกุมภาพันธ์จะมี 29 วัน
    if is_leap_year(year):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    month_name = what_month(1, month, year)

    # วันแรกของเดือนคือวันอะไร (0 = Mo, 1 = Tu,..., 6 = Su)
    first_day_of_week = what_day(1, month, year)

    # ปฏิทินของเดือนถูกตั้งค่าเริ่มต้นให้ว่างเปล่า
    monthly_cal = ''

    
    
    # สร้างส่วนหัวของปฏิทิน
    monthly_cal += f'{month_name} {year}\n'
    monthly_cal += '--------------------\n'
    monthly_cal += 'Mo Tu We Th Fr Sa Su\n'

    # คำนวณจำนวนช่องว่างก่อนวันแรกของเดือน
    for i in range(first_day_of_week):
        monthly_cal += '   '

    # วาดปฏิทิน
    day = 1
    while day <= days_in_month[month - 1]:
        monthly_cal += f'{day:2d} '

        # เมื่อถึงวันอาทิตย์ เริ่มบรรทัดใหม่
        if (day + first_day_of_week) % 7 == 0:
            monthly_cal += '\n'

        day += 1

    # ส่วนท้ายของปฏิทิน (เช่น กรณีที่ปฏิทินไม่เต็มสัปดาห์)
    if (day + first_day_of_week) % 7 != 0:
        monthly_cal += '\n'

    return monthly_cal

print(calendar(4, 2010))
