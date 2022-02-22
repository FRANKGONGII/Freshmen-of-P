print("Mary has a little lab")

# interesting
print("Its fleece was white as %s." %'snow')

print("And everywhere that Mary went.")

# A simple circulation
print("." * 10)

# put two or more strings together
end1 = 'C'  
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

print("*" * 20)
formater = "%r %r %r %r"
print(formater %(1, 2, 3, 4))
print(formater %("one", "two", "three", "four"))
print(formater %(True, False, False, True))
print(formater %(formater, formater, formater, formater))

# if there is ' in " ", change '' into " "
# Q : how to achieve this ??????????
print(formater %("hello", "world", "I'm", "King"))
# output: 'hello' 'world' "I'm" 'King'
print(formater %("hello", "world", "I am", "King"))
# output: 'hello' 'world' 'I am' 'King'

print("*" * 20)
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are days:", days)
print("Here are months:", months)

# We can type as much as we want with three double-quotes, even 3 or 4 lines
print("""
    Aaddsciyukjtfg
    AddressFamilyjtyhnf
    dsfdbtryntum
    ewfetrgfnh """)


