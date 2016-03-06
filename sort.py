import json

#creating the dictionary
candidate_dict = {}
#Creating a list
jsonData=[]

#testbatch3.json will be replaced by whatever file we are using
with open('nevada_tweets.json', 'r') as data_file:
	for line in data_file:
		# converts each line into a json object
		jsonData.append(json.loads(line))
        data_file.close()

for item in jsonData:
	#print item.has_key("content")

	content = item['text']
	address = item['address']
	#retrieving the index of the first comma in the address (ex: 11111 Euclid Ave, Cleveland, OH)
	index = address.index(',')
	#taking the substring of the address to isolate the town
	town = address[(index+2):]
	index2 = town.index(',')
	state = town[index2+2:]
	town = town[:index2]
	state_town = ','.join([town, state])
	#now, the town should be completely isolated
		
	if 'Pharmacy' in content or 'bernie' in content or 'bern' in content:
		key = '_'.join([state_town, 'sanders'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
	if 'clinton' in content or 'hillary' in content:
		key = '_'.join([state_town, 'clinton'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
	if 'trump' in content or 'donald' in content or 'apprentice' in content:
		key = '_'.join([state_town, 'trump'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
	if 'cruz' in content or 'ted' in content:
		key = '_'.join([state_town, 'cruz'])
		if candidate_dict.has_key(key):
			candidate_dict[key] += 1
		else:
			candidate_dict[key] = 1
# put dictionary in a json file
with open('dictionary.json', 'w') as dictionary:
	for key, value in candidate_dict.iteritems():
		dictionary.write(key + ": " + str(value))
	dictionary.close()