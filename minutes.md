
# Weekly Progress Meeting Minutes

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

