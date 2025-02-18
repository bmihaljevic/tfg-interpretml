## 2025-02-18

### Summary of the Day
- Total Hours Worked: 3
- Main Objective: Change global visualization of Categorical Naive Bayes and started NAM local visualization to InterpretML.

### Tasks Completed
1. Change the CatNB global visualization as discussed in the mail
2. Studied the code of the NAM wrapper 
3. Implemented a initial version of the local visualization for NAMs (not finished)

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- NAM local contributions and integration with InterpretML.

### Next Steps for Tomorrow
- Investigate how NAM local contributions would work.
- Finish NAM local contributions.
- Work on Gaussian NB global contribution visualization.
- Continue TFG Memory.

### Issues/Blockers
- Difficulty adapting the NAM wrapper to InterpretML because NAM model lacks many of the standard attributes of InterpretML models. So many modifications were made to NAM wrapper, though it worked.
- Possibility of modifying global visualization for CategoricalNB similar to EBM (the mail I sent you).
- Combining Gaussian NB and Categorical NB in the same file.

---

## 2025-02-15, 2025-02-16 and 2025-02-17

### Summary of the Day
- Total Hours Worked: 5
- Main Objective: Achieve global visualization of Categorical Naive Bayes and adapt NAM global visualization to InterpretML.

### Tasks Completed
1. Integrate global visualization of CatNB as commented in the meeting
2. Studied the code of the NAM wrapper 
3. Modified the plot function to better visualize feature contributions
4. Implemented a basic version of the global visualization for NAMs

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- NAM global and local contributions and integration with InterpretML.

### Next Steps for Tomorrow
- Investigate how NAM local contributions would work.
- Work on Gaussian NB global contribution visualization.
- Continue TFG Memory.

### Issues/Blockers
- Difficulty adapting the NAM wrapper to InterpretML because NAM model lacks many of the standard attributes of InterpretML models. So many modifications were made to NAM wrapper, though it worked.
- Possibility of modifying global visualization for CategoricalNB similar to EBM (the mail I sent you).
- Combining Gaussian NB and Categorical NB in the same file.

---

## 2025-02-10

### Summary of the Day
- Total Hours Worked: 2
- Main Objective: Modify NAM wrapper to achieve feature contribution visualization

### Tasks Completed
1. Study the code of the NAM wrapper and modify plot function
2. Feature contributions of NAMs can be visualized
3. Reorganise and continue TFG Memory 

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Look further into NAMs code
- Continue TFG memory

### Issues/Blockers
- Possibility of combining Gaussian NB and Categorical NB in the same file.

---

## 2025-02-04

### Summary of the Day
- Total Hours Worked: 2
- Main Objective: Dive deeper into NAMs architecture

### Tasks Completed
1. Study the code of the NAM wrapper and plot function
2. Try plot function of the model
   
### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- Discriminant Analysis integration on InterpretML
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Look further into NAMs code
- Integrate local and global explanations of QDA

### Issues/Blockers
- Plot function of NAMs model is unfinished (?), maybe have to clone and modify it.
- Problems understanding how features contribute on QDA.
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Lots of problems with versions when installing NAM wrapper. Had to create a new virtual environment to avoid this problem and it finally worked.

---

## 2025-02-03

### Summary of the Day
- Total Hours Worked: 2
- Main Objective: Read and understand Multiclass GAM article (https://arxiv.org/pdf/1810.09092)

### Tasks Completed
1. Read the article introducing Multiclass GAM
2. Understand API (Additive Post-Processing for Interpretability) and how it improves interpretability.

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- Discriminant Analysis integration on InterpretML
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Look further into NAMs code
- Integrate local and global explanations of QDA

### Issues/Blockers
- Problems understanding how features contribute on QDA.
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Lots of problems with versions when installing NAM wrapper. Had to create a new virtual environment to avoid this problem and it finally worked.

---

## 2025-01-31

### Summary of the Day
- Total Hours Worked: 2
- Main Objective: Investigate about QDA and start "Memoria TFG"

### Tasks Completed
1. Organized "Memoria TFG" by sections and start Introduction
2. Investigate how QDA features contribute to the prediction

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- Discriminant Analysis integration on InterpretML
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Read Multiclass GAM article
- Integrate local and global explanations of QDA

### Issues/Blockers
- Problems understanding how features contribute on QDA.
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Lots of problems with versions when installing NAM wrapper. Had to create a new virtual environment to avoid this problem and it finally worked.

---

## 2025-01-30

### Summary of the Day
- Total Hours Worked: 2.5
- Main Objective: Finish LDA integration and start QDA

### Tasks Completed
1. Integrate local explanation of LDA
2. Try local explanation on Iris dataset 
3. Integrate local explanation of LDA

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- Discriminant Analysis integration on InterpretML
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Integrate local and global explanations of QDA
- Start "Memoria TFG"

### Issues/Blockers
- Some problems understanding how features contribute on Discriminant Analysis.
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Lots of problems with versions when installing NAM wrapper. Had to create a new virtual environment to avoid this problem and it finally worked.

---

## 2025-01-29

### Summary of the Day
- Total Hours Worked: 2
- Main Objective: Start integrating Discriminant Analysis

### Tasks Completed
1. Integrate local explanation of LDA
2. Try local explanation on Iris dataset 
3. Keep investigating on NAMs example

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- Discriminant Analysis integration on InterpretML
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Integrate local and global explanations of LDA
- Integrate local and global explanations of QDA

### Issues/Blockers
- Some problems understanding how features contribute on Discriminant Analysis.
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Lots of problems with versions when installing NAM wrapper. Had to create a new virtual environment to avoid this problem and it finally worked.

---

## 2025-01-28

### Summary of the Day
- Total Hours Worked: 2.5
- Main Objective: Add an example using Categorical NB and try NAM wrapper

### Tasks Completed
1. Use Iris dataset with a discretization to try the updated Categorical NB.
2. Use NAM wrapper (https://github.com/lemeln/nam) on two datasets

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- Discriminant Analysis integration on InterpretML
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Keep investigating about NAMs code and try it on datasets.
- Start creating Discriminant Analysis files

### Issues/Blockers
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Lots of problems with versions when installing NAM wrapper. Had to create a new virtual environment to avoid this problem and it finally worked.

---


## 2025-01-15

### Summary of the Day
- Total Hours Worked: 2.5
- Main Objective: Try Categorical NB on a dataset and read NAMs code.

### Tasks Completed
1. Use Iris dataset with a discretization to try Categorical NB.
2. Read NAMs code and understand how it works.

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global Explanation Visualization.
- NAMs understanding and experiments.

### Next Steps for Tomorrow
- Keep investigating about NAMs code and try it on datasets.

### Issues/Blockers
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Problem with categorical NB to continuous features.

---


## 2025-01-14

### Summary of the Day
- Total Hours Worked: 2
- Main Objective: Create conditional probabilities for Categorical NB

### Tasks Completed
1. Understand how conditional probabilities work in CategoricalNB
2. Investigate the option of bayesian estimation (alpha in the formula)
3. Investigate about the problem of applying categorial NB to continuous features

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global and Local Explanation Visualization.

### Next Steps for Tomorrow
- Complete Local Explanation of Categorical Naive Bayes
- Look further into NAMs.

### Issues/Blockers
- Possibility of combining Gaussian NB and Categorical NB in the same file.
- Problem with categorical NB to continuous features.

---


## 2025-01-13

### Summary of the Day
- Total Hours Worked: 2.5
- Main Objective: Start creating Categorical Naive Bayes file

### Tasks Completed
1. Re-read and understand how a model and its explanations are coded in a file.
2. Create the file for Categorical Naive Bayes (maybe not necessary).
3. Understand how conditional probabilities work in CategoricalNB

### In-Progress
- Gaussian Naive Bayes Global Explanation Visualization.
- Categorical Naive Bayes Global and Local Explanation Visualization.

### Next Steps for Tomorrow
- Complete Local Explanation of Categorical Naive Bayes
- Look further into NAMs.

### Issues/Blockers
- Possibility of combining Gaussian NB and Categorical NB in the same file.

---

## 2024-12-09 and 2024-12-10

### Summary of the Day
- Total Hours Worked: 2
- Main Objective: Read about NAMs and check how categorical features are treated by EBMs explanations. 

### Tasks Completed
1. Read this introductory paper about NAMs: https://arxiv.org/abs/2004.13912
2. Created a notebook solving a binary classification problem to see how categorical features were treated by Interpret Explanations.

### In-Progress
- Naive Bayes Implementation and Visualization for Binary Classification.
- Naive Bayes Global Explanation Visualization.
- Reading and comprehension about NAMs.

### Next Steps for Tomorrow
- Look further into NAMs.
- Check some interesting visualizations in Yellowbrick that can be useful. 

### Issues/Blockers
-