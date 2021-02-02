import csv

def reset_in_log():
	with open("../gui/data/log/data_in_filtered.csv", "w+") as csvfile:
	    fieldnames = ['Name', 'Date','Time Stamp','System', 'Probability']
	    writercsv = csv.DictWriter(csvfile, fieldnames=fieldnames)

	    writercsv.writeheader()

	with open("../gui/data/log/data_in.csv", "w+") as csvfile:
	    fieldnames1 = ['Name', 'Date', 'Time Stamp', 'System', 'Probability']
	    writercsv1 = csv.DictWriter(csvfile, fieldnames=fieldnames1)

	    writercsv1.writeheader()

def reset_out_log():
		#clearing data_log filtered csv file.
	with open("../gui/data/log/data_in_filtered.csv", "w+") as csvfile:
	    fieldnames = ['Name', 'Date','Time Stamp','System', 'Probability']
	    writercsv = csv.DictWriter(csvfile, fieldnames=fieldnames)

	    writercsv.writeheader()

	#clearing data_log raw csv file.
	with open("../gui/data/log/data_out.csv", "w+") as csvfile:
	    fieldnames1 = ['Name', 'Date', 'Time Stamp', 'System', 'Probability']
	    writercsv1 = csv.DictWriter(csvfile, fieldnames=fieldnames1)

	    writercsv1.writeheader()

reset_in_log()
reset_out_log()

