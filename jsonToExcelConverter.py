import json
import csv

with open("purple.json") as file:
	data = json.load(file)
	responses = []
	print(len(data))
	i=0
	for item in data:
		# responses.append(item['responses'])
		value = json.dumps(item['responses'])
		pre_output= json.loads(value)
		print(pre_output)
		output = json.loads(pre_output)

		if "ID" in output:
			responses.append(output["ID"])
		elif "comment" in output:
			responses.append(output["useful_question"])
			responses.append(output["enjoy_question"])
			responses.append(output["easy_to_follow_question"])
			responses.append(output["comment"])
		i+=1
		print(str(i))
	print(responses)

outfile = "purpleoutput.csv"

with open(outfile, "w") as file:
	csv_file = csv.writer(file)
	csv_file.writerow(["ID","useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment",
					   "useful_question","enjoy_question","easy_to_follow_question","comment"])

	csv_file.writerow([responses[0],responses[1],responses[2],responses[3],responses[4],responses[5],responses[6],responses[7],responses[8],responses[9],
						   responses[10],responses[11],responses[12],responses[13],responses[14],responses[15],responses[16],responses[17],responses[18],responses[19],
						   responses[20],responses[21],responses[22],responses[23],responses[24],responses[25],responses[26],responses[27],responses[28],responses[29],
						   responses[30],responses[31],responses[32],responses[33],responses[34],responses[35],responses[36],responses[37],responses[38],responses[39],
					   	   responses[40],responses[41],responses[42],responses[43], responses[44], responses[45], responses[46], responses[47], responses[48]])