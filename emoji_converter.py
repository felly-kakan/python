#emojis in windows(windowskey + .)
message=input("> ")
words=message.split()
emoji_converter={
    ":)": "😊",
    ":(": "😒"
}
#output=""
x=""
for  word in words:
   x += emoji_converter.get(word,word) + " " 
print(x)
