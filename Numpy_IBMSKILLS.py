# from os import system
# from turtle import clear
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

# # df = pd.read_excel(xlsx_path)

# # new_index=['a','b','c','d','e','f','g','h']

# # df_new=df
# # df_new.index=new_index
# # df_new.loc['a', 'Artist']
# # print(df_new.loc['a':'d', 'Artist'])

#####################################################################################################################################################

# def Plotvec1(u, z, v):
    
#     ax = plt.axes() # to generate the full window axes
#     ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
#     ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
#     ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
#     plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
#     plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
#     plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
#     plt.show()

# x = np.linspace(0, 2*np.pi, num=100) #linspace
# y=np.sin(x)                         #sin cos functions
# plt.plot(x,y)                  
# plt.show()                         #to print plotted graph
# u = np.array([1, 0])              #numpy 1 D arrays
# v = np.array([0, 1])            
# z = np.add(u,v)                  #add,multiply,subtract,divide,dot (for dot product) of vectors [for linear algebra]
# Plotvec1(u,z,v)

# #####################################################################################################################################################

# x=np.linspace(2,3,num=10)           #for equally dividing a start and stop window into nums slices for ex start =2 end =3 and num=3 then 2 , 2.5 , 3
# for i in x:
#     print(i)

#####################################################################################################################################################
#with open('filepath','mode'):
    #perform operations like read,readline,readlines,write,

#loc[index] and iloc[integer indexes]  -- #set_index, index, we can also use slicing for selecting in loc and iloc 
# dataframes df[[select these columns]] , df[[name,age]] or df=old_df[age]>=10

#2d arrays in numpy
#A[0:2, 2] slicing in 2 d array A[0:2][2]==prints 0th and 1st element for row =0 and row=1 similarly A[0][0:2] prints first 2 elements of 0th row

#we can also perform dot product########MATRIX MULTIPLICATION ############ res_array = np.dot(A,B) {condition of dot product a's no of column = b's no of rows}
#sin of 2D array = np.sin(Z)
#Transpose of 2D array - C.T     the (  .T  ) is used to find the transpose


# df=pd.DataFrame({'name':['a','b','c'],'age':[10,20,30]})
# df.index=np.array(['h','i','j'])
# print(df)