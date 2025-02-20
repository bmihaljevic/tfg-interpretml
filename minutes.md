
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

