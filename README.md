# IndicGEC2025

Grammatical Error Correction for Indian languages under low resource setting with less than 1000 training samples for each language. Indian languages are low resource and this task tries to imitate that.

The training (train.csv) and validation (dev.csv) are available under folder for each language.
The final testing data will be available later.

The languages available are:

1. **Hindi**
2. **Telugu**
3. **Bangla** 
4. **Malayalam**
5. **Tamil**

Tamil GEC is under extreme low-resource setting with less than 100 training samples.

This is part of the Shared Task co-located with 1st BHASHA workshop 2025.

The urls for the competitions for final phase are:

1. [Hindi](https://www.codabench.org/competitions/10927/?secret_key=f65c4502-df61-4f26-b959-86d63d72cbe3)

2. [Malayalam](https://www.codabench.org/competitions/10941/?secret_key=b09e982e-9aa2-47b1-b4c7-ab85ac08ae8d)

3. [Telugu](https://www.codabench.org/competitions/10942/?secret_key=87b473ac-c2e1-473f-abc1-8e556f4c6b38)

4. [Bangla](https://www.codabench.org/competitions/10937/?secret_key=cb10e8e7-b16b-45b2-9bc0-2a8da4769881)

5. [Tamil](https://www.codabench.org/competitions/10938/?secret_key=fda54ec5-1fd9-45f8-94b7-e404b4762bc9)

## Rules for participation

1. Max Team Size: **4**
2. An individual cannot be part of multiple teams.
3. Submission is from one CodaBench account.
4. CodaBench account is required for participation.
5. Google Form for registration of teams: https://forms.gle/gftDLz69Vv9aB3AEA.

## Evaluation Criteria

**GLEU score** will be used for evaluation

Your submission should contatin a .zip of **predictions.csv** file. The **predictions.csv** file should contain 2 columns named
**Input sentence** and **Output sentence**.
Submissions that do not conform to this requirements will not be evaluated by the system.

All participating teams are expected to submit a system paper describing methodologies adopted and findings.

P.S:- All characters which are not in **native script** will be counted as **incorrect**.



