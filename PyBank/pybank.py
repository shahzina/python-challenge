#PyBank
import csv
import os

file = os.path.join("..", "PyBank","Resources", "budget_data.csv")

sum = 0
total_rev_change = 0
count = 0
#rev_change_count = 0
avg_rev_change = 0
rev_change = 0
max_rev_inc = 0
max_rev_dec = 0
cur_rev = 0
prev_rev = 0

outfile = "budget_output.txt"

with open(file, newline = '') as budgetcsv:
	csvreader = csv.reader(budgetcsv, delimiter = ',')
	header = next(csvreader)

	for row in csvreader:
		count = count + 1
		cur_rev = row[1]
		date = row[0]
		print(cur_rev)
		sum = sum + int(cur_rev)

		#rev change for each month
		rev_change = int(cur_rev) - int(prev_rev)
		total_rev_change = total_rev_change + rev_change
		#rev_change_count = len(total_rev_change)

		if rev_change >= 0:
			if rev_change > max_rev_inc:
				max_rev_inc = rev_change
				inc_date = date 

		elif rev_change < 0:
			if rev_change < max_rev_dec:
				max_rev_dec = rev_change
				dec_date = date 

		prev_rev = cur_rev

	avg_rev_change = total_rev_change/ count

	# print("")
	# print("Financial Analysis")
	# print("-"*50)
	# print("Total months : "+ str(count))
	# print("Total Revenue : "+ str(sum))
	# print("Average Revenue Change is $"+str(avg_rev_change))
	# print("Greatest Increase in Revenue: "+ inc_date + " ($" + str(max_rev_inc) +")")
	# print("Greatest Decrease in Revenue: "+ dec_date + " ($" + str(max_rev_dec) +")")
	# print("")

	with open(outfile, "w") as output:
		# output.write("financial analysis \n")
		# output.write("-"*10)
		output.write("Financial Analysis \n")
		output.write("-"*50 + "\n")
		output.write("Total months : "+ str(count)+ "\n")
		output.write("Total Revenue : "+ str(sum)+ "\n")
		output.write("Average Revenue Change is $"+str(avg_rev_change)+ "\n")
		output.write("Greatest Increase in Revenue: "+ inc_date + " ($" + str(max_rev_inc) +") \n")
		output.write("Greatest Decrease in Revenue: "+ dec_date + " ($" + str(max_rev_dec) +") \n")



