li = ['.com','.tech','.edu','.org']
user_name = input("Enter your user_name: ")
length= len(user_name)
for i in range(0,4):
    k=user_name.find(li[i])
    print(k)