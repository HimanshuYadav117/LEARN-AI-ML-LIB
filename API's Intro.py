# from cProfile import label
# import pandas as pd
# import numpy as np
# import plotly.graph_objects as go
# from plotly.offline import plot
# import plotly.express as px
# import matplotlib.pyplot as plt
# import datetime
# from pycoingecko import CoinGeckoAPI
# from mplfinance.original_flavor import candlestick2_ohlc
# cg = CoinGeckoAPI()

# bitcoin_data = cg.get_coin_market_chart_by_id(id='ethereum', vs_currency='inr', days=30)
# bitcoin_price_data = bitcoin_data['prices']
# data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
# data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
# candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
# fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
#                 open=candlestick_data['Price']['first'], 
#                 high=candlestick_data['Price']['max'],
#                 low=candlestick_data['Price']['min'], 
#                 close=candlestick_data['Price']['last'])
#                 ])

# fig.update_layout(xaxis_rangeslider_visible=False)
# # fig = px.scatter(candlestick_data, x="date", y="Price")

# fig.show()

#####################################################################################################################################################

#http get and post API methods 

# import requests as rq
# url="https://www.ibm.com/"
# r=rq.get(url)
# print(r.request.headers) #http request headers
# header=r.headers  #http response headers
# print(header['date'])

######################################################################################################################################################
#url='https://www.ibm.com/'
# r=requests.get(url)
#r.status_code,r.headers(for response headers),r.request.headers(for request headers),r.request.body,header['date'],content-type, r.encoding,r.text[0:100]

#suppose in response content there is a image now to handle it we can do the following steps
# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name

# # path=os.path.join(os.getcwd(),'image.png') #specifying path and name
# with open(path,'wb') as f: opening the path file and writing the content in it
# #     f.write(r.content) 
# now to view the image 
# Image.open(path)  


#url_get='http://httpbin.org/get'
#creating a query string like for name and password  
# create a dictionary of values to pass to get function ideally in url the queries are seperated by ? and assigned values using = and contains & for params for ex
# urlxyz/get?name=joseph&pass=123
# #payload={"name":"Joseph","ID":"123"}
#r=requests.get(url_get,params=payload)
#if content type of response is JSON #r.json()
#r.json()['args']
  

  #POST REQUESTS
  #url_post='http://httpbin.org/post'
  #r_post=requests.post(url_post,data=payload)
  #print("POST request URL:",r_post.url )
  #print("GET request URL:",r.url)
  #to view form in post request
  #r_post.json()['form']
  #print("POST request body:",r_post.request.body)
  #print("GET request body:",r.request.body) only post request has and body and get response has h body

# import os 
# from PIL import Image
# from IPython.display import IFrame
# import requests
# url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
# r=requests.get(url)
# path=os.path.join(os.getcwd(),'image.png')
# with open(path,'wb') as f:
#     f.write(r.content)
# Image.open(path)

################################################################################################################################################################
#RANDOMUSER API to generate random people details to work as testing data
# Get Methods
# get_cell()
# get_city()
# get_dob()
# get_email()
# get_first_name()
# get_full_name()
# get_gender()
# get_id()
# get_id_number()
# get_id_type()
# get_info()
# get_last_name()
# get_login_md5()
# get_login_salt()
# get_login_sha1()
# get_login_sha256()
# get_nat()
# get_password()
# get_phone()
# get_picture()
# get_postcode()
# get_registered()
# get_state()
# get_street()
# get_username()
# get_zipcode()


# from randomuser import RandomUser as ru
# lis1=ru.generate_users(10)
# print([x.get_first_name() for x in lis1])
# print([x.get_picture() for x in lis1])


# def get_users():
#     users =[]
     
#     for user in RandomUser.generate_users(10):
#         users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
#     return pd.DataFrame(users)    
# 
# Getting a dataframe of users so that tester can use it for testing easily
#  
# df1 = pd.DataFrame(get_users())  

#####################################################################################################################################################################
# #FruitVice API
# import requests
# import json
# import pandas as pd

# data = requests.get("https://www.fruityvice.com/api/fruit/all") #calling the API 
# results = json.loads(data.text) #retriving the results using loads
# pd.DataFrame(results) #converting them into dataframe
# #The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
# df2 = pd.json_normalize(results)
# #Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
# cherry = df2.loc[df2["name"] == 'Cherry']
# print("{} , {}".format((cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])))

# #other free PUBLIC APIS https://github.com/public-apis/public-apis

####################################################################################################################################################################
# import requests
# import json
# import pandas as pd
# url ='https://www.fishwatch.gov/api/species'
# res = requests.get(url)
# results=json.loads(res)
# r2=pd.DataFrame(results)
# print(r2)