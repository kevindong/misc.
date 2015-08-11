###############################################################################
# tip-calculator                                                              #
#                                                                             #
# A tip calculator that more accurately reflects how people actually tip.     #
###############################################################################
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print "How much is the bill?"
bill_amount = float(raw_input("    $"))
clear_screen()
print "Bill Amount: $" + format(bill_amount, '.2f')
print "\nBy percent:"
print "    15% = $" + format(bill_amount * 1.15, '.2f') # format() shows cent-level
print "    20% = $" + format(bill_amount * 1.20, '.2f') # accuracy.
print "    25% = $" + format(bill_amount * 1.25, '.2f')

print "\nBy whole numbers:"
base = int(bill_amount * 1.2) # This program assumes around a 20% tip.
if base < 75: # If (1.2 * bill_amount) is less than 75...
    for i in range(-2,3,1): # Calculates $1 & $2 (both under and over.) and at.
        a = base + i
        percent = float(a/bill_amount)
        if percent <= 1: # Checks to make sure calculated tip is positive. 
            pass # If not, amount is not calculated/printed. 
        elif percent < 1.1: # If tip is < 10%, only the ones place is shown. Otherwise, tens place too.
            print "    $" + str(a) + " = " + str(percent)[3:4] + "." + str(percent)[4:6] + "%"
        elif percent >= 1.1: # str(percent)[4:6] are the tenths and hundredths place.
            print "    $" + str(a) + " = " + str(percent)[2:4] + "." + str(percent)[4:6] + "%"
        else:
            print "Error"
elif base >= 75: # If (1.2 * bill_amount) is >= 75...
    for i in range(-4,5,2): # Calculates $2 & $4 (both under and over.) and at.
        a = base + i
        percent = a/bill_amount
        if percent <= 1:
            pass
        elif percent < 1.1:
            print "    $" + str(a) + " = " + str(percent)[3:4] + "." + str(percent)[4:6] + "%"
        elif percent >= 1.1:
            print "    $" + str(a) + " = " + str(percent)[2:4] + "." + str(percent)[4:6] + "%"
        else:
            print "Error 1"
else:
    print "Error 2"