# HPC4WC_group7
Comparison of high-level programming techniques for stencil computation (Coursework HPC4WC 2020)

Numba (http://numba.pydata.org/ 
https://nyu-cds.github.io/python-numba/
https://www.youtube.com/watch?v=x58W9A2lnQc 

### Setup environment:
- open the console
- which python --> prints the current environment
- source HPC4WC_venv/bin/activate --> loads the correct environment
- check again with which python, if it worked

### Run stencil_main.py
- move to its folder
- run with:
python3 stencil_main.py --dim_stencil 3 --nx 10 --ny 10 --nz 10 --num_iter 100 --stencil_type test


### Validation and performance report options
- Set the option create_field = True (Default) to create a new random field that is saved as a .npy file.
- Set then the option create_field to False to validate the out fields of different stencils to the original numpy field.
- With each new field automatically a new csv-report is generated, where the properties of the run and the elapsed work time is summed up as a table.
- Further validation runs are added as a row to the already generated performance report.
- If the field shapes of the original and the control file are not equal, the program stops. To generate however a report with stencils of different field sizes and no validation set the option create_newreport to False. 


  
