date = input("Enter date: ")
day = int(date.split('.')[0])
mon = date.split('.')[1]

if (mon == '01'):
    if (day < 20):
        sign = "Capricornus"  
    else: sign = "Aquarius"

elif (mon == '02'):
    if (day < 19):
        sign = "Aquarius"  
    else: sign = "Pisces"

elif (mon == '03'):
    if (day < 21):
        sign = "Pisces"
    else: sign = "Aries"

elif (mon == '04'):
    if (day < 20):
        sign = "Aries"
    else: sign = "Taurus"

elif (mon == '05'):
    if (day < 21):
        sign = "Taurus"
    else: sign = "Gemini"

elif (mon == '06'):
    if (day < 22):
        sign = "Gemini"
    else: sign = "Cancer"

elif (mon == '07'):
    if (day < 23):
        sign = "Cancer"
    else: sign = "Leo"

elif (mon == '08'):
    if (day < 23):
        sign = "Leo"
    else: sign = "Virgo"

elif (mon == '09'):
    if (day < 23):
        sign = "Virgo"
    else: sign = "Libra"

elif (mon == '10'):
    if (day < 24):
        sign = "Libra"
    else: sign = "Scorpius"

elif (mon == '11'):
    if (day < 22):
        sign = "Scorpius"
    else: sign = "Sagittarius"

elif (mon == '12'):
    if (day < 22):
        sign = "Sagittarius"
    else: sign = "Capricornus"

print("Your sign is", sign)
