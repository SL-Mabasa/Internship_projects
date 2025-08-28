import requests
import io
import csv
import xml.etree.cElementTree as xml

# TEST TYPE OF API
def type(name):
    url='https://'+name

    try:
        res = requests.get(url)
        res.raise_for_status()

        data_type = res.headers.get("Content-Type", "").lower()

        if "application/json" in data_type:
            data = 'JSON'
            print(f'\n{data} file\n')
            return data
        
        elif "csv" in data_type or url.endswith(".csv"):
            data = 'CSV'
            print(f'\n{data} file\n')
            return data
        
        elif "xml" in data_type:
            data = 'XML'
            print(f'\n{data} file\n')
            return data
        
        else:
            print('\nNo API data found\n')
            data = False
            return data
    
    except requests.exceptions.RequestException:
        statement = 'Request fail to obtain API data type'
        return statement

# GETS INFORMATION FROM API
def api(name, api_type):
    url='https://'+name

    if api_type == 'JSON':
        #JSON TYPE
        try:
            res = requests.get(url)
            res.raise_for_status()

            info = res.json()

            for data in info:
                print('\n')
                print(data)
        
        except requests.exceptions.RequestException:
            print('\nRequest fail as JSON\n')

    elif api_type == 'CSV':
        #CSV TYPE
        try:
            res = requests.get(url)
            res.raise_for_status()

            info = csv.reader(io.StringIO(res.text))

            for data in info:
                print('\n')
                print(data)
        
        except requests.exceptions.RequestException:
            print('\nRequest fail as CSV\n')

    elif api_type == 'XML':   
        #XML TYPE
        try:
            res = requests.get(url)
            res.raise_for_status()

            info = xml.fromstring(res.text)

            for data in info:
                print('\n')
                print(data)
        
        except requests.exceptions.RequestException:
            print('\nRequest fail as XML\n')
    
    else:
        print('\nNo API data information detected\n')


# Application
website = input('\nEnter website you want information from\nE.g (youtube.com) or (example.co.za)\n-> ')
check = type(website)

if check == 'JSON' or check == 'XML' or check == 'CSV':
    api(website, check)

elif check == False:
    pass

else:
    print(check)