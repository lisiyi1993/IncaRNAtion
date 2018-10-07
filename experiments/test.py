import os
import subprocess

file_directory1 = 'C:\\Users\Alex\Desktop\IncaRNAtion\experiments\\test_samples.txt'
file_directory2 = 'C:\\Users\Alex\Desktop\IncaRNAtion\scripts\\rnastrand_dataset_filtered_100seq_up150nt.txt'
option = str(0.4)
subprocess.call(['C:\\Users\Alex\Desktop\IncaRNAtion\src\incarnation_3.py',
                 '-d', file_directory1,
                 '-a', option,
                 '-s_gc', '0.3', '10',
                 '-gc_data', 'result.txt'],
                shell=True)