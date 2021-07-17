from datetime import datetime

def datetimeFromDate(date):
    return datetime.strptime(date + " 2020", "%d %b %Y")

aquarius = datetimeFromDate("21 Jan")
pisces = datetimeFromDate("20 Feb")
aries = datetimeFromDate("21 Mar")
taurus = datetimeFromDate("21 Apr")
gemini = datetimeFromDate("21 May")
cancer = datetimeFromDate("22 Jun")
leo = datetimeFromDate("23 Jul")
virgo = datetimeFromDate("23 Aug")
libra = datetimeFromDate("22 Sep")
scorpio = datetimeFromDate("23 Oct")
sagittarius = datetimeFromDate("23 Nov")
capricorn = datetimeFromDate("22 Dec")

numberOfDates = int(input())
for _ in range(numberOfDates):
    date = datetimeFromDate(input())
    if aquarius <= date < pisces:
        print("Aquarius")
    elif pisces <= date < aries:
        print("Pisces")
    elif aries <= date < taurus:
        print("Aries")
    elif taurus <= date < gemini:
        print("Taurus")
    elif gemini <= date < cancer:
        print("Gemini")
    elif cancer <= date < leo:
        print("Cancer")
    elif leo <= date < virgo:
        print("Leo")
    elif virgo <= date < libra:
        print("Virgo")
    elif libra <= date < scorpio:
        print("Libra")
    elif scorpio <= date < sagittarius:
        print("Scorpio")
    elif sagittarius <= date < capricorn:
        print("Sagittarius")
    else:
        print("Capricorn")
