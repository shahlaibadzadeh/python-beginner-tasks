from datetime import datetime
user_birth = input("Enter birthday: (17.02.2000) ")
birth_dateform = datetime.strptime(user_birth, "%d.%m.%Y")
mon = birth_dateform.month
day = birth_dateform.day

if (mon == 1):
    if (day < 20):
        sign = "Capricornus"  
    else: sign = "Aquarius"

elif (mon == 2):
    if (day < 19):
        sign = "Aquarius"  
    else: sign = "Pisces"

elif (mon == 3):
    if (day < 21):
        sign = "Pisces"
    else: sign = "Aries"

elif (mon == 4):
    if (day < 20):
        sign = "Aries"
    else: sign = "Taurus"

elif (mon == 5):
    if (day < 21):
        sign = "Taurus"
    else: sign = "Gemini"

elif (mon == 6):
    if (day < 22):
        sign = "Gemini"
    else: sign = "Cancer"

elif (mon == 7):
    if (day < 23):
        sign = "Cancer"
    else: sign = "Leo"

elif (mon == 8):
    if (day < 23):
        sign = "Leo"
    else: sign = "Virgo"

elif (mon == 9):
    if (day < 23):
        sign = "Virgo"
    else: sign = "Libra"

elif (mon == 10):
    if (day < 24):
        sign = "Libra"
    else: sign = "Scorpius"

elif (mon == 11):
    if (day < 22):
        sign = "Scorpius"
    else: sign = "Sagittarius"

elif (mon == 12):
    if (day < 22):
        sign = "Sagittarius"
    else: sign = "Capricornus"

print("Your sign is", sign)
