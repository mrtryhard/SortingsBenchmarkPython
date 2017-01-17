## Sorting Algorithms Tests
Requires *python 3.2.x*.  
Tested on Debian Jessie.  
As a class assignment, this repository contains some sorting algorithms 
programmed with python in the `code` folder. 
  
### Test machine
All test have been running against my personal laptop, within a virtual machine (Virtual Box).
Here are the specs:  

* Host CPU: Intel Core i7 vPro 3250M @ 2.90 GHz
* 2 physical cores allocated for VM
* RAM: 4GB allocated for VM (12GB host).
* Host OS: Windows 8.1 Professional (FR)
* Guest (VM) OS: Debian Jessie 64bits (en)
* Python version: 3.2.3 
* Guest Hard Drive: 15GB free. 
* Physical hard drive: 500GB SSD Samsung EVO.

### Results 
All results and charts are within the `results` directory.   
Please consult the xlsx file for the graphical comparison results.  

### Run yourself 
`$> python3 run_tests.py`  
Will run all tests for all algorithms.   
  
`$> python3 xxxx_sort.py [numbers]`  
To run a specific test where xxxx is the sorting algorithm name and numbers is a number suite (e.g. 35 89 100 3 2 67 0 2 23 ...).

### What tests do
Runs test series from 10 000 elements, and multiplying per 2 each new series up to 5 120 000 elements per test.  
Each series is 30 test. 

### Disclaimer and license
No really license, as it is relatively easy work.  
However, I cannot guarantee the validity of those tests. Feel free to correct them if I am wrong.
