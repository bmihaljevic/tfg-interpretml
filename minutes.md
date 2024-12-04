
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

