import os
import subprocess

# List of .ts files to be combined
ts_files = ['test1.ts', 'test2.ts', 'test3.ts', 'test4.ts', 'test5.ts']

# Output file name
output_file = 'combined.ts'

# Concatenate the files
with open(output_file, 'wb') as outfile:
    for file_name in ts_files:
        with open(file_name, 'rb') as readfile:
            outfile.write(readfile.read())

# Play the combined file
subprocess.call(['ffplay', '-autoexit', output_file])