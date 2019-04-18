
import requests
import json
import csv

CACHE_FNAME = "itunes_cache.json" # can be anything, name of a json file
try:
    file_obj = open(CACHE_FNAME,'r')
    file_contents = file_obj.read()
    CACHE_DICTION = json.loads(file_contents)
    file_obj.close()
except:
    CACHE_DICTION = {}

# Have to do some work to fill these in
# baseurl = "https://itunes.apple.com/search" # This would be different depending on the API, and the only way to find it is to be told or to look it up
# diction_of_parameters = {}
# diction_of_parameters["term"] = "Pop"
# diction_of_parameters["media"] = "music"

# Then make a request and save the result in a variable
#resp_obj = requests.get(baseurl, params=diction_of_parameters) # Always the same, just fill in the info
#print(resp_obj.text) # what type is this?
#print(type(resp_obj.text))
#itunes_data = json.loads(resp_obj.text)
# print(type(itunes_data))

def params_unique_combination(baseurl, params_d, private_keys=["api_key"]):
    alphabetized_keys = sorted(params_d.keys())
    res = []
    for k in alphabetized_keys:
        if k not in private_keys:
            res.append("{}-{}".format(k, params_d[k]))
    return baseurl + "_".join(res)


baseurl = "https://itunes.apple.com/search" # This would be different depending on the API, and the only way to find it is to be told or to look it up
diction_of_parameters = {}
diction_of_parameters["term"] = "Pop"
diction_of_parameters["media"] = "music"
unique_identifier = params_unique_combination(baseurl, params_diction) # creating a unique ident for this request

if unique_identifier in CACHE_DICTION:
	return CACHE_DICTION[unique_identifier]
else:
	resp = requests.get(baseurl, params=params_diction) # response obj -- I only want to do this once for EACH unique request
	python_object = json.loads(resp.text)
	# Do something else first -- save it for the next time
	cache_file_object = open(CACHE_FNAME, 'w')
	# take the cache dictionary and add a new key-val pair
	CACHE_DICTION[unique_identifier] = python_object
	# I need to make sure that EVERYTHING NOW in the cache dictionary will be saved in my file for next time
	cache_file_object.write(json.dumps(CACHE_DICTION))
	return python_object # return CACHE_DICTION[unique_identifier]
	print(resp.text)

## Now I can do some investigation!

## Just like before!

## I'm interested in the song titles inside this data. I want a list of song titles. Saved in variable song_titles.

# write the data to a file for easy copying

# OR, just do investigation with code
#print(itunes_data.keys())
# print(itunes_data["results"])
#print(type(itunes_data["results"]))
#print(type(itunes_data["results"][0]))
# itunes_data["results"] accesses a list of dictionaries
#print(itunes_data["results"][0].keys()) # maybe this'lll give me an idea of what the keys of EVERY diction in the list are

#trackName?
#print(itunes_data["results"][0]["trackName"])
#print(itunes_data["results"][0]["releaseDate"])

#for result in itunes_data["results"]:
	#print(result["trackName"])
