

## 2024-11-18


### Summary of the Day
- Total Hours Worked: 2.5
- Main Objective: Use our 'interpretml' version. 

### Tasks Completed
1. Modify some part of the source code of the EBMs and verify that 'our' version of the library is working. In order to do that, I uninstalled the original interpretml library and installed it again (both interpret and interpret-core) pointing to our 'interpret' folder. I executed it in editable mode (pip install -e ...) so now every change in the source code will be instantly applied to the library.

### In-Progress
Understanding of 'explain_global' function.
Modify the code of 'global_explain' and 'local_explain' and try other importances. This will allow us to visualize other models. 

### Next Steps for Tomorrow
- Task 1: Modify the code of 'global_explain' and 'local_explain' and try other importances.

### Issues/Blockers
- Still some problems with the library, specifically with 'libebm'. 'libebm' is a shared library that the EBM model needs, but it isn't in the github interpret repository, I think. I had to add a \root folder (which I found in the original interpret package folder in my PC) in the interpret-core folder. Now it is solved.