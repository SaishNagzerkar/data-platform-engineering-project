import requests
import logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
import pandas as pd 
url="https://jsonplaceholder.typicode.com/users"
response= requests.get(url,timeout=10) 
response.raise_for_status()
data=response.json()
df=pd.DataFrame(data)
clean_df=df[["id", "name", "email", "phone", "website"]]
print("\n Missing values:")
print(clean_df.isnull().sum())
clean_df["name"]=clean_df["name"].str.upper()
clean_df["email"]=clean_df["email"].str.lower()
clean_df.to_csv("clean_users.csv",index=False)
logging.info("Data cleaning and CSV export completed successfully!")