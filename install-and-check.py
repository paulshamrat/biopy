# Assume you have already installed version of python in you machine
# Open command prompt
# type python
# this will call the python interface if you have installed version of python

# For me I already installed python previously; now time to install biopython

# Step 01: open command prompt
# step 02: type below command

pip install biopython

# This will show something like this if everything is okay

----
C:\Users\shamr>pip install biopython
Collecting biopython
  Downloading biopython-1.79-cp39-cp39-win_amd64.whl (2.3 MB)
     |████████████████████████████████| 2.3 MB 364 kB/s
Requirement already satisfied: numpy in c:\python\python39\lib\site-packages (from biopython) (1.21.4)
Installing collected packages: biopython
Successfully installed biopython-1.79
-----

# Now check the version of your installed biopython

>>> import Bio
>>> print(Bio.__version__)
1.79
>>>

# So you have installed biopython on your windows machine. Now have fun!

# install intoyour Windows subsystem for linux
# ubuntu 20.04

sudo apt-get install python-biopython

# Source 
# Biopython cookbook: http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec5