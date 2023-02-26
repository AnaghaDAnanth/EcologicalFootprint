import requests
import json
import csv

# year = list(range(1992, 2019))
# country_list = list(range(1, 1022))

# year = list(range(1992, 2017))
year = [2015]
country_list = [1,2,3,4,7,8,9,10,11,12,13,14,16,18,19,20,21,23,25,26,27,28,29,32,33,35,37,38,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,66,67,68,69,70,72,73,74,75,79,80,81,84,86,87,89,90,91,93,95,97,98,100,101,102,103,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,121,122,123,124,126,129,130,131,133,134,135,136,137,138,141,143,144,146,147,149,150,154,155,156,157,158,159,162,165,166,167,168,169,170,171,173,174,175,176,178,179,181,182,183,184,185,186,189,191,193,194,195,197,198,199,200,201,202,203,206,207,208,209,210,211,212,213,215,216,217,219,220,221,222,223,225,226,228,229,230,231,233,234,235,236,237,238,244,248,249,250,251,255,256,272,273,276,277,299,351,2000,2001,2002,2003,2004,2005,1000,1001,1002,1003,1004,1005,1006,1007,1009,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,5001]

payload={}
headers = {
  'Authorization': 'Basic YW5hZ2hhOjE0MG9kcFR0b29TbzdNN2hzZDJpOTNjbWdQcXI2NzJzNjAyNTltbWs2MDdjVnNUaW1uNGQ='
}

for i in range(len(year)):
  print("I = ", i)
  for j in range(len(country_list)):
    print("beginning")
    url = f'https://api.footprintnetwork.org/v1/data/{country_list[j]}/{year[i]}/all'
    response = requests.request("GET", url, headers=headers, data=payload)

    json_object = json.loads(response.text)
    if (i == 0 and j==0):
      if (len(json_object) == 0):
        pass
      else:
        print("NOWW:", j)
        keys = json_object[0].keys()
        # print("DONE")
        with open('2015.csv', 'w', newline='') as output_file:
          dict_writer = csv.DictWriter(output_file, keys)
          dict_writer.writeheader()
          dict_writer.writerows(json_object)
          
    else:
      print("LATER:", j)
      print("LATERRR:", json_object)
      if (len(json_object) == 0):
        pass
      else:
        keys = json_object[0].keys()
        with open('2015.csv', 'a', newline='') as output_file:
          dict_writer = csv.DictWriter(output_file, keys)
          dict_writer.writerows(json_object)

print("Fetched Data Successfully")
  # with open("test.json", "a") as myfile:
  #     myfile.write(res)



