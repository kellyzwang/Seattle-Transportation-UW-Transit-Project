import pandas as pd

#original file
df = pd.read_csv(r'C:\Users\user\Desktop\AU\DATA 511\Final_Proj\Transit_Stops_for_King_County_Metro___transitstop_point.csv')

#Check the col name
print (list(df.columns.values))

#left with 4 cols we want
df_c = df[['X','Y', 'STOP_ID', 'ROUTE_LIST']]
print (df_c.shape) #check shape

#drop duplicates as stop_id has duplicates 
df_c = df_c.drop_duplicates()
print (df_c.shape) #check shape

#Drop bus stops without any bus that stops
df_c = df_c.dropna()
print (df_c.shape) #check shape

#Output to split the bus num col into multiple ones and re input
df_c.to_csv(r'C:\Users\user\Desktop\AU\DATA 511\Final_Proj\Bus_Route_1.csv', index=False) #max buses in one stop => 26 (!...)
df_2 = pd.read_csv(r'C:\Users\user\Desktop\AU\DATA 511\Final_Proj\Bus_Route_1.csv')

print(df_2.shape) #check shape
      
#Melt down the bus num into the col
df_pivot = pd.melt(df_2,id_vars=['X', 'Y', 'STOP_ID'], value_vars=['ROUTE_LIST', 'ROUTE_LIST 1', 'ROUTE_LIST 2', 'ROUTE_LIST 3', 'ROUTE_LIST 4', 'ROUTE_LIST 5', 'ROUTE_LIST 6', 
                              'ROUTE_LIST 7', 'ROUTE_LIST 8', 'ROUTE_LIST 9', 'ROUTE_LIST 10', 'ROUTE_LIST 11', 'ROUTE_LIST 12', 'ROUTE_LIST 13', 
                              'ROUTE_LIST 14', 'ROUTE_LIST 15', 'ROUTE_LIST 16', 'ROUTE_LIST 17', 'ROUTE_LIST 18', 'ROUTE_LIST 19', 'ROUTE_LIST 20', 
                              'ROUTE_LIST 21', 'ROUTE_LIST 22', 'ROUTE_LIST 23', 'ROUTE_LIST 24', 'ROUTE_LIST 25'], value_name='BUS_NUM')

print(df_pivot.shape) #check shape

df_pivot = df_pivot[['X','Y', 'STOP_ID', 'BUS_NUM']] #drop extra col created from value_vars
df_pivot = df_pivot.dropna() #drop na - as additional na created from multiple Route_list (Every stop has 26 cells - so we cleaned out)
print(df_pivot.shape) #check shape

#Output 
#df_pivot.to_csv(r'C:\Users\user\Desktop\AU\DATA 511\Final_Proj\Bus_Route.csv', index=False)

