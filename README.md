#### Description
Test Resources is basically a simple project that provides in memory files (including images and csv)   
for testing purposes   


#### Installation
installation is very simple.    
`pip install git+https://github.com/gradia-exchange/test-resources.git`   


#### Usage
```python
# E.g. Generating a photo for django unit test
from test_resources.files import generate_photo  
from django.core.files.uploaded import SimpleUploadedFile  
  
# Generating photos   
photo = generate_photo("avatar.png")   
photo_file = SimpleUploadedFile(photo.name, photo.read())   
   
# Generating csv files   
headers = ("name", "age", "color", "profession")   
columns = (("John Doe", 34, "dark", "Programmer"), ("Jane Smith", 23, "chocolate", "Sales Personnel"))   
csv = generate_csv("basic_upload.csv")   
csv_file = SimpleUploadedFile(csv.name, csv.read())   
```


#### Notice   
For image generation, it currently on supports PNGs which may be enough for most test cases   