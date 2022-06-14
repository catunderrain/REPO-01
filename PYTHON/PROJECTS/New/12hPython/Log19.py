
text = input()
with open('C:\\Users\\lovem\\Desktop\\VAkhung.txt', 'a') as file: # 'w' for overwritting
    file.write(text)
    
with open('C:\\Users\\lovem\\Desktop\\VAkhung.txt') as file:
    print(file.read())

print(file.closed)
