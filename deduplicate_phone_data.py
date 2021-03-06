import json, os

def clean_file (infile_1, infile_2, outfile_name):
	data = []

	with open(infile_1, 'r') as data_file_1:
		print ("reading in " + infile_1)
		for line in data_file_1:
			try:
				data.append(json.loads(line))
			except:
				continue

	with open(infile_2, 'r') as data_file_2:
		print ("reading and checking for duplicates in " + infile_2)
		for line in data_file_2:
			try:
				x = json.loads(line)
				if x not in data:
					data.append(json.loads(line))
			except:
				continue

	with open(outfile_name, 'w') as outfile:
		print ("writing to " + outfile_name)
		for d in data:
			outfile.write(json.dumps(d))
			outfile.write("\n")

original_data_path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(original_data_path)

for n in files:
	if 'phoneTweets22' in n:
		date_string = n[11:-5]
		if (date_string[0:2] == "22"):
			adjusted_date_string = date_string[1::]
			string_1 = "phoneTweets" + adjusted_date_string + ".json"
			string_2 = "phoneTweets2" + adjusted_date_string + ".json"
			outfile_name = "merged_phone_data_" + adjusted_date_string + ".json"
			if not outfile_name in files:
				clean_file(string_1, string_2, outfile_name)