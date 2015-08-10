###############################################################################
# pws-scraper                                                                 #
#                                                                             #
# This program scrapes Purdue University (West Lafayette)'s listing of        #
# work-study jobs and outputs a more readable version of the listings. This   #
# program can also detect if new jobs have been posted since the last time the#
# program was run.                                                            #
# Note: Purdue is unlikely to update their listing more than once a day, so   #
# running this program more than once a day is a waste of time and resources. #
###############################################################################

import requests # For easy scraping
import time     # To print the current date and time
import fnmatch  # For counting the runs already performed
import os       # For counting the runs already performed

class Job(object):
    def __init__(self, categories, title, number, duties, contact, email, address, remarks, openings, start_date, experience, skill, min_hours, max_hours, min_pay, max_pay, on_campus):
        self.categories = categories
        self.title = title
        self.number = number
        self.duties = duties
        self.contact = contact
        self.email = email
        self.address = address
        self.remarks = remarks
        self.openings = openings
        self.start_date = start_date
        self.experience = experience
        self.skill = skill
        self.min_hours = min_hours
        self.max_hours = max_hours
        self.min_pay = min_pay
        self.max_pay = max_pay
        self.on_campus = on_campus
    def return_jobs(self): # Returns a 'Job' in a pretty format
        return "Job Number: " + self.number + "Category: " + self.categories + "Title: " + self.title + "Duties: " + self.duties + "Contact: " + self.contact + "Email: " + self.email + "Address: " + self.address + "Remarks: " + self.remarks + "Openings: " + self.openings + "Start Date: " + self.start_date + "Experience: " + self.experience + "Skill: " + self.skill + "Min. Hours: " + self.min_hours + "Max. Hours: " + self.max_hours + "Min. Pay: " + self.min_pay + "Max. Pay: " + self.max_pay + "On campus: " + self.on_campus + "\n"

print "Accessing and downloading webpage... ",
page = requests.get('http://www.purdue.edu/webdb/jobposting/JobSearch.cfm?TableName=qryStudentJobs&CriteriaFields=JobTypeInfo&Criteria=Campus%20Jobs%2FWork%20Study&CriteriaOpFields=&CriteriaOps=&OpStatus=&CFID=2024892&CFTOKEN=6f16bd8b971e0b29-C5E4577A-A265-DCBE-B2EB9504DCB435E6') # Grabs webpage
original = open('original.html', 'w')
original.write(page.text) # Writes webpage to file
original.close()
print "Done."
original = open('original.html', 'r')
print "Done."

output_count = 1 # To be used later
for file in os.listdir('.'): # <- and next 2 lines count number of outputs
    if fnmatch.fnmatch(file, 'pws-scraper-output-*.txt'): # already generated
        output_count += 1

number_of_lines = (sum(1 for line in original) + 1) # Counts the number of lines in the file
original.close()
f=open('original.html', 'r') # This line and following line splits the original
lines = f.readlines()        # webpage into a giant list where each line is an
f.close()                    # index (i.e., lines[0] = first line).
#os.remove('original.html')
number_of_jobs = lines[number_of_lines - 130][1:3] # Finds and saves the # of jobs
count = int(number_of_jobs)

# Each job takes up 50 lines with a few blank lines in between. The format is
# consistent throughout. The jobs start at line 560 of the webpage. The 'a'
# variable defines which job the program is on. The for loop just defines the
# dictionary key and value. For example, the first iteration would define the
# key as "string1" and the value as Job(lines[a+5][26:], ...). [a+5][26:]
# corresponds to the fact that the 'Category' of the job starts on the 27th
# character of the 5th line. And so on and so forth for the reaminder of the
# Job() class.
print "Tabulating jobs..."
transition = {}
for x in range(1,count+1): 
    a = 560 + ((x-1) * 53) - 1
    transition["string{0}".format(x)] = Job(lines[a+5][26:], lines[a+7][29:].replace('&nbsp;',"",2), lines[a+9][23:].replace('&nbsp;',"",2), lines[a+11][26:].replace('&nbsp;',"",2), lines[a+13][27:].replace('&nbsp;',"",2), lines[a+15][1:].replace('&nbsp;',"",2), lines[a+17][27:].replace('&nbsp;',"",2), lines[a+25][27:].replace('&nbsp;',"",2), lines[a+27][28:].replace('&nbsp;',"",2), lines[a+29][23:].replace('&nbsp;',"",2), lines[a+31][34:].replace('&nbsp;',"",2), lines[a+33][18:].replace('&nbsp;',"",2), lines[a+35][29:].replace('&nbsp;',"",2), lines[a+37][22:].replace('&nbsp;',"",2), lines[a+39][20:].replace('&nbsp;',"",2), lines[a+41][20:].replace('&nbsp;',"",2), lines[a+45][22:].replace('&nbsp;',"",2))

# This loop just prints out the value of each key (which stands for each job)
# and writes it to the output file. 
print "Started generating/writing output file..."
output = open('pws-scraper-output-' + format(output_count, '03') + '.txt', 'w')
output.write("Run Number: " + format(output_count, '03') + "\n")
output.write("Generated on: " + time.strftime("%m/%d/%Y at %H:%M:%S") + "\n") # Prints date and time
output.write("Number of Jobs: " + number_of_jobs + "\n\n")
for x in range(1,count+1):
    d = "string" + str(x)
    b = transition[d].return_jobs()
    output.write(b)
output.close()
print "Done writing jobs to file!"

if output_count > 1:
# The remainder of this 'if' branch examines the newest and second newest
# output files to see if there's one or more jobs in the newest file that isn't
# in the second newest file. If so, a file will be generated indicating so. 
# The same principles as used in the 'tabulating jobs' loop are used below.
    print "Now analyzing files..."
    previous = open('pws-scraper-output-' + format(output_count-1, '03') + '.txt', 'r')
    previous_lines = previous.readlines()
    previous.close()
    previous_number_of_jobs = previous_lines[2][16:18]
    current = open('pws-scraper-output-' + format(output_count, '03') + '.txt', 'r')
    current_lines = current.readlines()
    current.close()
    current_number_of_jobs = current_lines[2][16:18]
    previous_jobs = []
    for i in range(1, ((int(previous_number_of_jobs))+1)):
        previous_multiplier = 4 + ((i-1) * 18)
        previous_jobs.append(previous_lines[previous_multiplier][12:17])
    current_jobs = []
    for i in range(1, ((int(current_number_of_jobs))+1)):
        current_multiplier = 4 + ((i-1) * 18)
        current_jobs.append(current_lines[current_multiplier][12:17])
    new_jobs = list(set(current_jobs) - set(previous_jobs))
    if len(new_jobs) > 0:
        print str(len(new_jobs)) + " new jobs available!"
        difference = open('pws-scraper-difference-between-' + format(output_count-1, '03') + '-and-' + format(output_count, '03') + '.txt', 'w+')
        difference.write('Jobs in ' + format(output_count, '03') + ' but not in ' + format(output_count-1, '03') + ".\n\n")
        for item in new_jobs:
            lookup = item
            with open('pws-scraper-output-' + format(output_count, '03') + '.txt', 'r') as myFile:
                for num, line in enumerate(myFile, 1):
                    if lookup in line:
                        location = num
                        location = location - 1
                        for i in range(0, 16):
                            difference.write(current_lines[location+i])
                        difference.write("\n")
                    else:
                        pass
            myFile.close()
        difference.close()
    else:
        print "\nNo new jobs, bummer."
else:
    print "Rerun this program at a later time to check if there's new jobs."