import glob, os
import pysrt
os.chdir("./")
print("data")
count = 0
for file in glob.glob("*.srt"):
	# print(file)
	subs = pysrt.open(file, encoding='iso-8859-1')
	# print(len(subs))

	for i in range(0,len(subs)):
		if (subs[i].text.find("an1")) > -1:
			count += 1
		if (subs[i].text.find("an2")) > -1:
			count += 1
		if (subs[i].text.find("an3")) > -1:
			count += 1
		if (subs[i].text.find("an4")) > -1:
			count += 1
		if (subs[i].text.find("an5")) > -1:
			count += 1
		if (subs[i].text.find("an6")) > -1:
			count += 1
		if (subs[i].text.find("an7")) > -1:
			count += 1
		if (subs[i].text.find("an8")) > -1:
			count += 1
		if (subs[i].text.find("an9")) > -1:
			count += 1
	print(count)
print(count)

