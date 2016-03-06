# GenEdMatcher

### Description
At Purdue University, there isn't an easy way to see what classes, that are available to enroll in, satisfy specific degree requirements. For students enrolled in the College of Science, the "General Education" requirement is the worst offender. There's about 1,100 courses on the list. Students must take three of those courses. Within the course registration system, there is no indication of what courses satisfy this requirement. This program will parse through the lists and tell you what courses are available that will satisfy the requirement. 

I came up with this idea when I needed a class to fill a particular timeslot in my schedule while also satisfying a degree requirement. Currently, you have to grab the classes available during a particular timeslot yourself. In the future, I'd like to develop this program to do that for you. For now, I exported the classes (into .csv format) available by using Purdue's UniTime/Scheduling Assistant service and then used Excel to format the .csv file into the correct format. 

tl;dr Input two files (one of the courses available; the other of courses that satisfy a particular requirement) and this program will spit out what courses you can register for that satisfy a given requirement.

### Usage
You will need to input two files to use this program. Both files must be formatted in the following way: 

````
ABC 10000	Alphabet and You!
ABC 20000	Alphabetizing!
XYZ 30000	What is Alphabet?
XYZ 40000	Totally not running out of example text!
````
Please note that each line is formatted like this: `[course-abreviation-and-number][tab][course-title]`

One one of your files is the list of courses that are available during a particular timeslot. The other is the list of courses that satisfy a particular degree requirement (if you're a Purdue College of Science student, feel free to use the `gened.txt` file for the general education requirements). The `input.txt` file is a list of all the classes available during the Spring 2016 semester that occupy the timeslot of TR 3:00pm - 4:15pm. If you'd like, you can use that too. 

Regardless, place both files into the same directory as `GenEdMatcher.java` and run the command in the following format: `java -jar GenEdMatcher.java [available_courses.txt] [GenEd_courses.txt]`. This is a functional example that you can run with nothing but the files within this repo: `java -jar GenEdMatcher.jar input.txt gened.txt`.

### Plan for Future Devlopment
For Purdue students (or rather, students of any university that use UniTime): make an automated way to grab classes from UniTime/Scheduling Assistant for a particular timeslot. 

### Source File
The source is located within this folder. It's named `GenEdMatcher.java`. 

### License
See the root directory of this repo for licensing information.