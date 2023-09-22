sana=input ("Sanani kiriting (dd.mm.yyyy hh:mm): ").split(" ")
# print(sana)
day, month, year = sana[0].split(".")
# print(day, month, year)
oy = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June','07': 'July', '08': 'August','09': 'September', '10': 'October', '11':'November', '12':'December'}
hour, min=sana[1].split(":")
# print(hour, min)
print(day, oy.get(month), year,"year", hour,"hour", min, "minutes")
