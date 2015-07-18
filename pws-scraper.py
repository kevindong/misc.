###############################################################################
# pws-scraper                                                                 #
#                                                                             #
# This program scrapes Purdue University (West Lafayette)'s listing of        #
# work-study jobs and outputs a more polished and readable version of it.     #
###############################################################################

import requests # For easy scraping
import time     # To print the current date and time

class Job(object):
    def __init__(self, categories, title, number, duties, contact, address, remarks, openings, start_date, experience, skill, min_hours, max_hours, min_pay, max_pay, on_campus):
        self.categories = categories
        self.title = title
        self.number = number
        self.duties = duties
        self.contact = contact
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
        return "Category: " + self.categories + "Title: " + self.title + "Job Number: " + self.number + "Duties: " + self.duties + "Contact: " + self.contact + "Address: " + self.address + "Remarks: " + self.remarks + "Openings: " + self.openings + "Start Date: " + self.start_date + "Experience: " + self.experience + "Skill: " + self.skill + "Min. Hours: " + self.min_hours + "Max. Hours: " + self.max_hours + "Min. Pay: " + self.min_pay + "Max. Pay: " + self.max_pay + "On campus: " + self.on_campus + "\n"

page = requests.get('http://www.purdue.edu/webdb/jobposting/JobSearch.cfm?TableName=qryStudentJobs&CriteriaFields=JobTypeInfo&Criteria=Campus%20Jobs%2FWork%20Study&CriteriaOpFields=&CriteriaOps=&OpStatus=&CFID=2024892&CFTOKEN=6f16bd8b971e0b29-C5E4577A-A265-DCBE-B2EB9504DCB435E6') # Grabs webpage
original = open('original.html', 'w')
original.write(page.text) # Writes webpage to file
original.close()
original = open('original.html', 'r')
output = open('output.txt', 'w')
output.write("Generated on: " + time.strftime("%m/%d/%Y at %H:%M:%S") + "\n\n") # Prints date and time

number_of_lines = (sum(1 for line in original) + 1) # Counts the number of lines in the file
original.close()
f=open('original.html', 'r') # This line and following line splits the original
lines = f.readlines()        # webpage into a giant list where each line is an
f.close()                    # index (i.e., lines[0] = first line).
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
transition = {}
for x in range(1,count+1): 
    a = 560 + ((x-1) * 53) - 1
    transition["string{0}".format(x)] = Job(lines[a+5][26:], lines[a+7][29:].replace('&nbsp;',"",2), lines[a+9][23:].replace('&nbsp;',"",2), lines[a+11][26:].replace('&nbsp;',"",2), lines[a+13][27:].replace('&nbsp;',"",2), lines[a+17][27:].replace('&nbsp;',"",2), lines[a+25][27:].replace('&nbsp;',"",2), lines[a+27][28:].replace('&nbsp;',"",2), lines[a+29][23:].replace('&nbsp;',"",2), lines[a+31][34:].replace('&nbsp;',"",2), lines[a+33][18:].replace('&nbsp;',"",2), lines[a+35][29:].replace('&nbsp;',"",2), lines[a+37][22:].replace('&nbsp;',"",2), lines[a+39][20:].replace('&nbsp;',"",2), lines[a+41][20:].replace('&nbsp;',"",2), lines[a+45][22:].replace('&nbsp;',"",2))

# This loop just prints out the value of each key (which stands for each job)
# and writes it to the output file. 
for x in range(1,count+1):
    d = "string" + str(x)
    b = transition[d].return_jobs()
    output.write(b)
output.close()