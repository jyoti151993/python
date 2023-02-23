"""
----------------------------------------------
Pandas Exercise
----------------------------------------------

Load the lms_members.xlsx file to Python using pandas and perform the following operation:

/* Display name of all the members */
/* Display name of all the members whose membership_status is Permanent*/
/* Display Name of the member , City in which he resides and date of membership expiry*/
/* name of the member whose date_expire is greater than 01-01-2020 */
/* name of the member who resides in PUNE */
/* name of the member who resides in Pune and his membership_status is Permanent*/
/* list all unique cities in the members dataframe*/

"""
import pandas as pd
import datetime as dt

lms_details=pd.ExcelFile("C:/Users/dbda-lab/Desktop/DBDA22/Python/LMS.xlsx")
df=pd.read_excel(lms_details,'lms_members')
print(df)

#/* Display name of all the members */
#print(df['MEMBER_NAME'])

#/* Display name of all the members whose membership_status is Permanent*/
#print(df[df['MEMBERSHIP_STATUS']=='Permanent']['MEMBER_NAME'])


#/* Display Name of the member , City in which he resides and date of membership expiry*/
#print(df[['MEMBER_NAME','CITY','DATE_EXPIRE']])


#/* name of the member whose date_expire is greater than 01-01-2020 */
#print(df[df['DATE_EXPIRE']>dt.datetime(2020,1,1)]['MEMBER_NAMER'])


#/* name of the member who resides in PUNE */
#print(df[df['CITY'].str.upper()=='PUNE'] ['MEMBER_NAME'])


#/* name of the member who resides in Pune and his membership_status is Permanent*/
#print(df[(df['CITY'].str.upper()=='PUNE') & (df['MEMBERSHIP_STATUS']=='Permanent') ]['MEMBER_NAME'])


#/* list all unique cities in the members dataframe*/
#print(df['CITY'].str.upper().unique())
#print(df['CITY'].str.lower().unique())