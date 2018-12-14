import csv

path = "budget_data.csv"

count=0
total=0
previous=867884
changelist=[]
maxchange=0
minchange=0

with open(path, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	for row in csvreader:

		current=int(row[1])

		count=count+1
		total=total+current

		

		change=current-previous
		changelist.append(change)

		if change>maxchange:
			maxchange=change
		if change<minchange:
			minchange=change
		previous=current

average_change=sum(changelist)/len(changelist)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {count}")
print(f"Total : {total}")
print(f"average change: {average_change}")
print(f"maxchange: {maxchange}")
print(f"minchange) {minchange}")

