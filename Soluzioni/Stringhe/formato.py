def is_date(s: str) -> bool:
    parts = s.split('/')
    
    if len(parts) != 3:
        return False
    
    day, month, year = parts
    # day, month, year = parts[0], parts[1], parts[2]

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    return True 

print(is_date("10/07/2015"))
print(is_date("10-07-2015")) 
print(is_date("1/07/2015")) 
print(is_date("10/7/2015")) 
print(is_date("10.07.2015")) 
print(is_date("10.aa.2015"))
print(is_date("10/aa/2015")) 