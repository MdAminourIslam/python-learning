def day_of_week(day):
    match day:
        case 1:
            return "It's Saturaday"
        case 2:
            return "It's Sunday"
        case 3:
            return "It's Monday"
        case 4:
            return "It's Tuesday"
        case 5:
            return "It's Wednusday"
        case 6:
            return "It's Thusday"
        case 7:
            return "It's Friday"
        case _: #Default Case
            return "Not a Valid Day"
        

def is_weekend(day):
    match day:
        case 1 | 2 | 3 | 4 | 5: # Multiple Case 
            return False
        case 6 | 7:
            return True
        case _:
            return "Not a Valid Day"


print(day_of_week(1))
print(day_of_week(2))
print(day_of_week(8))



print(is_weekend(1))
print(is_weekend(6))
print(is_weekend(9))
