import os, sys, time

def bubbleSort(array):
  if sys.argv[1] == 'U':	
	  for i in range(len(array)):
	    swapped = False
	    for j in range(0, len(array) - i - 1):
	      if array[j] > array[j + 1]:
	        temp = array[j]
	        array[j] = array[j+1]
	        array[j+1] = temp

	        swapped = True
	          
	    if not swapped:
	      break
  elif sys.argv[1] == 'D':
  	for i in range(len(array)):
	    swapped = False
	    for j in range(0, len(array) - i - 1):
	      if array[j] < array[j + 1]:
	        temp = array[j]
	        array[j] = array[j+1]
	        array[j+1] = temp

	        swapped = True
	          
	    if not swapped:
	      break

def getFileExtension(file):
	chars_list = []
	for i in range(len(file)-1, -1, -1):
		chars_list.append(file[i])
		if file[i] == '.':
			break
	extension = "".join(chars_list)
	return extension[::-1] 


if len(sys.argv) <= 1 or len(sys.argv) > 2:
	sys.stderr.write("Incorrect arguments please specify sorting order...")
	sys.stderr.flush()
else:
	os.chdir(input("Specify path: "))
	my_dir_content = os.listdir()
	my_files = []

	for file in my_dir_content:
		if os.path.isfile(file):
			my_files.append(file)

	bubbleSort(my_files)

	for i in range(len(my_files)):
		os.rename(my_files[i], str(i)+getFileExtension(my_files[i]))
