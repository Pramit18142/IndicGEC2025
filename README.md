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

The urls for the competitions are:

1. [Hindi](https://www.codabench.org/competitions/10840/?secret_key=c30c3264-632c-45a6-957e-81ade9c0e198)

2. [Malayalam](https://www.codabench.org/competitions/10475/?secret_key=151c0997-3c00-4068-b351-b8cf0bf03052)

3. [Telugu](https://www.codabench.org/competitions/10675/?secret_key=97557fab-4caa-4297-8344-ae0b8904b1b8)

4. [Bangla](https://www.codabench.org/competitions/10482/?secret_key=f4ee606f-a9cb-4092-ad1c-f3cc82d5f5c5)

5. [Tamil](https://www.codabench.org/competitions/10838/?secret_key=74681fea-4907-46b3-8502-69835f97e4e1)

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



