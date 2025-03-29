#
# Anna McClure
# 3/29/25
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#Open the file
myfile = open('numbers.txt', 'r')

#read and display the file contents
for line in myfile:
  number = int(line)
  print(number)

#close the file
myfile.close()
