
import requests
import datetime

# Function to download file
def download_file(url, file_name):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return file_name


# Calculate the process execution time
Start_Time = datetime.datetime.now()

os.chdir ('D:\Script_Learning\Python_3\Soccer_Study')