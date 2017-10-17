import sys,json,array,collections,geoip2.database


data = []
jsonfield = "src_host"

# Load data to memory
f = open(sys.argv[1])
line = f.readline()
while line:
    line = f.readline()
    try:
	json_object = json.loads(line)
	data.append(json_object[jsonfield])
    except ValueError:
	continue
f.close()
print("loaded")
data.sort()
print("sorted")
# End memory load

reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
geo_data = []
set(data)
for i in data:
	try:
	   response = reader.country(i)
	   print(response.country.name) #+" i")
	   #print(i)
	except ValueError:
           continue
