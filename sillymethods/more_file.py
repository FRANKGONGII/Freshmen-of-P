from sys import argv
from os.path import exists
script, from_file, to_file = argv
print("Copying from %s to %s" % (from_file, to_file))
file_data = open(from_file).read()
print("The input file is %d bytes long" % len(file_data))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit return to continue, ^c to stop")
input()
output = open(to_file, 'w')
output.write(file_data)
print("Done")
output.close()
output = open(to_file)
print(output.read())








