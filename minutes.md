
# Weekly Progress Meeting Minutes

**Date:** 2025-02-20

---

## 1. Summary of Weekly Progress  

- **Main Objectives:** Global contributions of NB and integration of NAMs
- **Key Accomplishments:**
  - NAM "completely" integrated, both global and local visualizations using InterpretML visuals 
  - Global CategoricalNB implemented, using specific categorical visualization
  - Global GaussianNB started, has to be reviewed.
  - Continued TFG Memory
- **Overall Status:** On Track  

## 2. Task Summary  

| Task                                   | Status     | Time Spent | Summary                                                                                  |  
|----------------------------------------|------------|------------|------------------------------------------------------------------------------------------|  
| Global Contributions NAM  | Completed | 1.5h | Using the "plot" function as a base, it wasn't difficult to recreate it with InterpretML visuals. |  
| Reorganized lots of NAM attributes and methods | Completed | 2h | As NAM wrapper was made by an independent guy, there were some difficulties integrating its code. |  
| Local Contributions NAM | Completed | 1.5h | Used global functions to obtain each local value and plot it using InterpretML visuals. |  
| Global Contributions GaussianNB | Completed | 1h | Made an initial version of the GaussianNB features global contributions. |  
| Global Contributions CategoricalNB | Completed | 2.5h | Not many problems with the calculus but the visualization, as the model was considering coded categorical features as numerical. |  
| Continued "Memoria TFG" | In progress | 1h | Read and wrote about Linear, GLM and GAM models. |  

## 3. Challenges/Issues  

- **Issue 1**: **Handling Different Feature Types in Naive Bayes Models**  
  - **Impact**: The base models I used as a base for Naive Bayes supported both continuous and categorical features. However, adapting them to work with InterpretML required modifying some of its built-in attributes and functions, which caused difficulties.   
  - **Proposed Solution**: Customize each Naive Bayes model to properly handle the type.

- **Issue 2**: **Limited Attributes and Methods in the Original NAM Wrapper**  
  - **Impact**:  The NAM model is well-designed, but its original wrapper lacks many attributes and methods necessary for a smooth adaptation to InterpretML. This required removing and adding several elements to make it compatible. 
  - **Proposed Solution**: Expand and refine the wrapper to improve its integration with InterpretML.  

### 4. Feedback & Discussion Points
- [Any feedback from progress meeting]
- [Discussion points raised during the meeting]

### 5. Goals for Next Week
- **Goal 1:** 
- **Goal 2:** 

### 6. Action Items
| Action Item | Due Date |
|-------------|----------|
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |

---
---

**Date:** 2025-02-05

---

## 1. Summary of Weekly Progress  

- **Main Objectives:** Integrate local and global explanation of LDA and QDA, and investigate more about NAMs
- **Key Accomplishments:**
  - LDA completely integrated, global and local explanation.  
  - QDA not integrated, but studied. Problem with explanations. 
  - Use NAMs wrapper (https://github.com/lemeln/nam) and try it.
  - Started "Memoria TFG" and organized it.
- **Overall Status:** On Track  

## 2. Task Summary  

| Task                                   | Status     | Time Spent | Summary                                                                                  |  
|----------------------------------------|------------|------------|------------------------------------------------------------------------------------------|  
| Study and integrate LDA | Completed | 2.5h | Researched LDA decision function and integrated local and global explanation. |  
| Study and integrate QDA | In progress | 3h | Investigated about QDA and how it works; didn't understand how the model features contributes to the prediction |  
| Explore and investigate about NAMs | In progress | 3h | Read NAMs paper, used the wrapper, try it on two datasets |  
| Started "Memoria TFG" | In progress | 1.5h | Read other final projects, organized and started ours |  
| Read Multiclass Interpretation paper (https://arxiv.org/pdf/1810.09092) |  Completed | 1h | Read it and understand the intuition behind API technique |  

## 3. Challenges/Issues  

- **Issue 1**: **Local and global explanations of QDA**  
  - **Impact**: As QDA is a quadratic method, it's difficult to me understand exactly how a feature contribute to the prediction made by the model.
  - **Proposed Solution**: -

- **Issue 2**: **NAMs wrapper seems incomplete (?)**  
  - **Impact**: NAMs wrapper have a good implementation of Neural Additive Models but it might be unfinished, specifically the visualization part of the model. 
  - **Proposed Solution**: Clone the repo and complete the implementation.

### 4. Feedback & Discussion Points
- [Any feedback from progress meeting]
- [Discussion points raised during the meeting]

### 5. Goals for Next Week
- **Goal 1:** 
- **Goal 2:** 

### 6. Action Items
| Action Item | Due Date |
|-------------|----------|
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |

---
---

**Date:** 2025-01-14

---

## 1. Summary of Weekly Progress  

- **Main Objectives:** Integrate local explanation of Categorical Naive Bayes with custom visualization functions of InterpretML. 
- **Key Accomplishments:**
  - Explored conditional probabilities of Categorical Naive Bayes.  
  - Implemented local contributions for Categorical Naive Bayes and tested its behavior.  
  - Investigated about the problem of continuous features with Categorical NB.  
  - Read about NAMs.
- **Overall Status:** On Track  

## 2. Task Summary  

| Task                                   | Status     | Time Spent | Summary                                                                                  |  
|----------------------------------------|------------|------------|------------------------------------------------------------------------------------------|  
| Understand local contributions for Categorical Naive Bayes | Completed | 1h | Researched how to compute local contributions. |  
| Implemented local explanation for Categorical Naive Bayes | In progress | 1.5h | Did a first version of local explanation. |  
| Study the problem of Categorical NB for continuous features | In progress | 1h |  |  
| Read about NAMs | Completed | 1.5h | Read documentation, examined the structure of these networks. |  

## 3. Challenges/Issues  

- **Issue 1**: **Treating continuous features with Categorical NB**  
  - **Impact**: Continuous features can lead to inaccurate probabilities and reduced model performance since Categorical NB assumes discrete inputs.
  - **Proposed Solution**: Discretize continuous features into bins.

### 4. Feedback & Discussion Points
- [Any feedback from progress meeting]
- [Discussion points raised during the meeting]

### 5. Goals for Next Week
- **Goal 1:** 
- **Goal 2:** 

### 6. Action Items
| Action Item | Due Date |
|-------------|----------|
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |

---
---

# Weekly Progress Meeting Minutes

**Date:** 2024-12-04  

---

## 1. Summary of Weekly Progress  

- **Main Objectives:** Integrate local explanation of Gaussian Naive Bayes with custom visualization functions of InterpretML. 
- **Key Accomplishments:**  
  - Implemented local contributions for Naive Bayes and tested its behavior.  
  - Explored and tested LDA and QDA models, analyzing their internal attributes and decision functions.  
  - Discovered that Gaussian Naive Bayes does not natively handle missing data, despite NB should ignore it.
  - Investigated how libraries in PyPI are structured and published.  
- **Overall Status:** On Track  

## 2. Task Summary  

| Task                                   | Status     | Time Spent | Summary                                                                                  |  
|----------------------------------------|------------|------------|------------------------------------------------------------------------------------------|  
| Understand local contributions for Naive Bayes | Completed | 2h | Researched how to compute local contributions and implemented a version. |  
| Explore and test LDA and QDA models | Completed | 2h | Read documentation, examined the decision functions and attributes of LDA and QDA in a notebook. |  
| Investigate missing data handling in GaussianNB | Completed | 1h | Verified that GaussianNB does not support missing data directly and considered alternatives. |  
| Modify InterpretML for visualization | Completed | 2.5h | Adapted custom visualization functions for local contributions and tested them. |  
| Study PyPI repository structure | Completed | 1h | Investigated packaging and publishing workflows for Python libraries. |  
| Implement `_naivebayes.py` module | In progress | 2h | Created a module for Naive Bayes and started integrating it with the visualization functions. |  

## 3. Challenges/Issues  

- **Issue 1**: **Naive Bayes integration with visualization**  
  - **Impact**: It was challenging to align the probabilistic outputs of Naive Bayes with the existing framework for visualization.  
  - **Proposed Solution**: Took _linear.py and _decisiontree.py as a base to create _naivebayes.py, allowing me to understand the organization of the code.

### 4. Feedback & Discussion Points
- [Any feedback from progress meeting]
- [Discussion points raised during the meeting]

### 5. Goals for Next Week
- **Goal 1:** Problems on missing data on Gaussian Naive Bayes of Scikit Learn
- **Goal 2:** Understand how to make a package installable with pip

### 6. Action Items
| Action Item | Due Date |
|-------------|----------|
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |

---
---

## Weekly Progress Meeting Minutes

**Date:** 2024-11-26

---

### 1. Summary of Weekly Progress
- **Main Objectives:** Import 'our' interpretml library and modify it in order to control the visualizations.
- **Key Accomplishments:** 
  - Understanding of both 'explain_global' and 'explain_local'.
  - Cloned interpretml repo and was able to modify it and use the custom functions.
  - Set constant contributions in both functions and visualize them, observing how the visualizations are.
- **Overall Status:** On Track

### 2. Task Summary
| Task | Status | Time Spent | Summary |
|------|--------|------------|---------|
| Understand both visualization functions | Completed | 2h |  |
| Clone interpret repo and use it | Completed | 2.5h | Struggled a bit trying to use our interpret folder as a library |
| Modify _ebm.py | Completed | 1.5h | By modifying the code it was easier to understand what the internal variables were doing. Set constant contributions and visualized it. |
| Naive Bayes Understanding | Completed | 1h | Tried to understand how to integrate Naive Bayes with this visualization functions |
| Naive Bayes Implementation | In progress | 2h | Created _naivebayes.py and started to program it |
| Autoimmune Disease ML Challenge - Data Understanding | Completed | 2h | Visualized and understood how the data is organized |
| Autoimmune Disease ML Challenge - Features extraction notebook | Completed | 1.5h | Created an initialization notebook that gets the features of the cell |

### 3. Challenges/Issues
  **Issue 1**: Difficulty modifying and using the source code of the InterpretML library
  **Impact**: It took significant time to understand and adapt the process since it was the first time modifying a library's source code.
  **Proposed Solution**: -

### 4. Feedback & Discussion Points
- [Any feedback from progress meeting]
- [Discussion points raised during the meeting]

### 5. Goals for Next Week
- **Goal 1:** Problems on missing data on Gaussian Naive Bayes of Scikit Learn
- **Goal 2:** Understand how to make a package installable with pip

### 6. Action Items
| Action Item | Due Date |
|-------------|----------|
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |

---
---

## Weekly Progress Meeting Minutes

**Date:** 2024-11-21

---

### 1. Summary of Weekly Progress
- **Main Objectives:** Import 'our' interpretml library and modify it in order to control the visualizations.
- **Key Accomplishments:** 
  - Understanding of both 'explain_global' and 'explain_local'.
  - Cloned interpretml repo and was able to modify it and use the custom functions.
  - Set constant contributions in both functions and visualize them, observing how the visualizations are.
- **Overall Status:** On Track

### 2. Task Summary
| Task | Status | Time Spent | Summary |
|------|--------|------------|---------|
| Understand both visualization functions | Completed | 2h |  |
| Clone interpret repo and use it | Completed | 2.5h | Struggled a bit trying to use our interpret folder as a library |
| Modify _ebm.py | In progress | 1.5h | By modifying the code it was easier to understand what the internal variables were doing. Set constant contributions and visualized it. |
| Naive Bayes Understanding | In progress | 1h | Tried to understand how to integrate Naive Bayes with this visualization functions |
| Autoimmune Disease ML Challenge - Data Understanding | Completed | 2h | Visualized and understood how the data is organized |

### 3. Challenges/Issues
  **Issue 1**: Difficulty modifying and using the source code of the InterpretML library
  **Impact**: It took significant time to understand and adapt the process since it was the first time modifying a library's source code.
  **Proposed Solution**: -

### 4. Feedback & Discussion Points
- [Any feedback from progress meeting]
- [Discussion points raised during the meeting]

### 5. Goals for Next Week
- **Goal 1:** [Description of goal or task for the following week]
- **Goal 2:** [Description of goal or task for the following week]

### 6. Action Items
| Action Item | Due Date |
|-------------|----------|
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |

---
---

## Weekly Progress Meeting Minutes

**Date:** 2024-11-14

---

### 1. Summary of Weekly Progress
- **Main Objectives:** Analyze and understand the visualization functions: 'global_explain' and 'local_explain'
- **Key Accomplishments:** 
  - Mostly understood 'global_explain' and the internal variables that interfere in the calculus.
  - Controlled the 'global_explain' visualizations, so now I can manage to change the contributions. This could be effective to use the visualizations for another model.
- **Overall Status:** On Track

### 2. Task Summary
| Task | Status | Time Spent | Summary |
|------|--------|------------|---------|
| Understand 'global_explain' function | Completed | 2h | Having read the source code now I can understand which internal variables are important |
| Control global explanations | Completed | 1h | The internal variable 'term_scores' is fundamental for the visualization |
| Understand 'local_explain' function | In progress | 2h | There are some internal functions with an undefined role that I have to analyse |
| Control local explanations | Blocked | | |


### 3. Challenges/Issues
- **Issue 1:** Issues understanding how are the calculations made to create the local contributions of each instance
  - **Impact:** Need some more days to fully comprehend the functionality
  - **Proposed Solution:** Fork the EBM repository to control all the internal functions and see what are they doing

### 4. Feedback & Discussion Points
- [Any feedback from progress meeting]
- [Discussion points raised during the meeting]

### 5. Goals for Next Week
- **Goal 1:** [Description of goal or task for the following week]
- **Goal 2:** [Description of goal or task for the following week]

### 6. Action Items
| Action Item | Due Date |
|-------------|----------|
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |
| [Action Item Description] | [Date] |

