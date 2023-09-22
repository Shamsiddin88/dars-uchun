morse = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k",
         ".-..": "l", "--":"m", "-.": "n","---":"o",".--.":"p", "--.-": "q", ".-.": "r", "...": "s","-": "t","..-": "u","...-": "v", ".--": "w", "-..-": "x", "-.--": "y","--..": "z"}
matn=list(input("So'z kiriting: ").split(" "))

value=list(morse.values())
key=list(morse.keys())

# print(value)
# print(key)

for i in matn:
    if i in key:
        print (value[key.index(i)], end="")