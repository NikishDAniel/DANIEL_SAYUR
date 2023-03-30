movieSales = { 
     'avatar' :{ 
        "cost":15,
        "sto" : 35,
        "stock":35,
        "profit":4,
        "price":0,
        "profitNew":0
     },
     'bahubali' :{ 
        "cost":12,
        "sto" : 45,
        "stock":45,
        "profit":3,
        "price":0,
        "profitNew":0
    }, 
     'johnWick' : {
        "cost":6,
        "sto" : 60,
        "stock":60,
        "profit":8,
        "price":0,
        "profitNew":0}
   
} 
print(movieSales.items())
'''  
#print(movieSales.keys())
print(movieSales.values())
print(type(movieSales.items()))
print(sorted(movieSales.items()))
''' 
a = sorted(movieSales.items(),key =lambda x:x[1]['profit'],reverse=True)[:3] 
print(a,type(a))

'''
list:
    '''

string = "apple"
for i in ['a','b','c']:
    print(i)