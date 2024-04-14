import requests
import pandas as pd
import re

eval_links = {
    "W3V1": "https://www.onlinegdb.com/t/as/1465678/sub/evaluate",
    "W3V2": "",
    "W4V1": "",
    "W4V2": "",
    "W5V1": "",
    "W5V2": "",
    "W6V1": "",
    "W6V2": "",
    "W7V1": "",
    "W7V2": "",
    "W8V1": "",
    "W8V2": "",
    "W9V1": "",
    "W9V2": "",
    "W10V1": "",
    "W10V2": "",
    "W11V1": "",
    "W11V2": "",
    "W12V1": "",
    "W12V2": "",
}

#names as shown in ONLINEGDB NOT CANVAS!
names_list = [
    "First Last",
    "First Last2",
    "First Last3"
]

#Enter your OnlineGDB email and password here
email = ""
password = ""

login_url = "https://www.onlinegdb.com/login"
login_data = {
    "email": email,
    "password": password
}
session = requests.Session()
response = session.post(login_url, data=login_data)
def bits_calculator(name_to_check,start_week,end_week):
    total_bits = 0              #Start with 0 bits
    completed_previous = True   #Assume they finished the last one

    for week in range(start_week,end_week):
        # sleep(1)              #Prevent rate limits just incase
                                #week by week rewards
        if week>=1 and week<=4:
            reward=10
        elif week>=5 and week<=8:
            reward=20
        else:
            reward=30
        #extract week link from dictionary     
        v1 = f"W{week}V1"
        v2 = f"W{week}V2"
        eval_url1 = eval_links[v1]
        eval_url2 = eval_links[v2]
    
        pattern = r'\b(\d) passed of \1\b'  #filters the table so that only "x passed of x"
        response = session.get(eval_url1)

        df_v1 = pd.read_html(response.text)[0]
        df_v1 = df_v1[df_v1["Test Result"].str.extract(pattern, expand=False).notnull()]
        # print(df_v1)                      #uncomment to view a table of everyone who passed v1
        
        response = session.get(eval_url2)
        df_v2 = pd.read_html(response.text)[0]
        df_v2 = df_v2[df_v2["Test Result"].str.extract(pattern, expand=False).notnull()]
        # print(df_v2)                      #uncomment to view a table of everyone who passed v2
       
        #preproccess for top 10 (sort by submission date)
        df_v1["Submission Date"] = df_v1["Submission Date"].apply(lambda x: re.search(r"'([^']*)'", x).group(1))
        df_v1["Submission Date"] = pd.to_datetime(df_v1["Submission Date"], format="%a, %d %b %Y %H:%M:%S %Z")
        df_v1.sort_values(by="Submission Date", inplace=True)

        #extract top 10
        top_10_names = df_v1.head(10)["Submitted By"].tolist()

        #the three ways to earn bits
        is_in_top_10 = name_to_check in top_10_names
        is_in_both = name_to_check in df_v1["Submitted By"].values and name_to_check in df_v2["Submitted By"].values
        is_in_either = name_to_check in df_v1["Submitted By"].values or name_to_check in df_v2["Submitted By"].values

        #adding all ways to earn bits 
        if is_in_either and completed_previous:
            total_bits+=reward
        if is_in_top_10:
            total_bits+=reward
        if is_in_both:
            total_bits+=reward

        completed_previous = is_in_either   #used to update streak
    print(name_to_check,":",total_bits)


if __name__ == "__main__":
    """Main function"""
    start_week = 0
    end_week = 0
    for name in names_list:
        bits_calculator(name,start_week,end_week)
