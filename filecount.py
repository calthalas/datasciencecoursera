# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
results = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    line = line.replace("X-DSPAM-Confidence: ","")
    line = float(line)
    count = count + 1
    results.append(line)

avg = sum(results)/count

#print results
#print count
print "Average spam confidence:",avg
