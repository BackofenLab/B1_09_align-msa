Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 9: Multiple Sequence Alignment
---

### _Exercise 1 - Progressive Alignment by Feng and Doolittle_

Given the sequences S<sub>1</sub> = CTCACA, S<sub>2</sub> = CAC, S<sub>3</sub> = GTAC and the following scoring function:

<p align="center">
  <img src="./figures/sheet9-exercise2-score.svg" alt="score" width=80%/>
</p>

We want to do progressive alignment following Feng and Doolittle. The needed pairwise alignments are calculated using the Needleman-Wunsch and are as follows:

<p align="center">
  <img src="./figures/sheet9-exercise2-alignments.svg" alt="alignments" width=45%/>
</p>


We want to follow one step of the algorithm introduced in the lecture.
The following guide trees are given in [Newick format](https://en.wikipedia.org/wiki/Newick_format).

**a)** Starting with the guide tree **((S<sub>1</sub>, S<sub>3</sub>), S<sub>2</sub>)**, what would be the starting **group<sub>1</sub>**?

**b)** Use the Needleman-Wunsch algorithm to generate all pairwise alignments against **group<sub>1</sub>** and calculate their respective **similarity score**.

**c)** Based on the previously calculated pairwise alignments what are the possible choices for **group<sub>2</sub>**?

**d)** Calculate the sum-of-pairs scores for each of the possible **group<sub>2</sub>** choices.

**e)** Which alignment will be chosen as **group<sub>2</sub>** for the next step?

**f)** Based on what you have learned, what are the alignments and sum-of-pairs scores for the guide tree **((S<sub>2</sub>, S<sub>3</sub>), S<sub>1</sub>)**?


### _Exercise 2: Scoring Matrices_
Determine the correct text by replacing the highlighted words with the correct anagrams:

Scoring matrices reflect the fact that amino acids with similar **(A) isehcayhilccpmo** properties can be more easily substituted than those without similar characteristics, since they are more likely to cause **(B) rsistnupoid** to the structure and function. This type of disruptive **(C) uuttotsbnisi** is less likely to be selected in evolution because it renders **(D) iouanctfnlonn** proteins.

PAM matrices, except PAM1, are derived from an **(E) raniyeooutvl** model. The increasing PAM numbers correlate with increasing PAM units and thus evolutionary **(F) tsnascedi** of protein sequences. For example, PAM250, which corresponds to about 20% amino acid **(G) tyedniti**, represents 250 mutations per 100 residues (a position could mutate several times). In theory, the number of **(E) raniyeooutvl** changes approximately corresponds to an expected **(E) raniyeooutvl** span of 2,500 million years. Thus, the PAM250 matrix is normally used for **(H) neirtdgve** sequences.

BLOSUM matrices are derived based on direct observation for every possible amino acid **(C) uuttotsbnisi** in multiple sequence alignments. Instead of using the **(I) earoopatitnlx** function, the BLOSUM matrices are actual percentage identity values of sequences selected for construction of the matrices. For example, BLOSUM62 indicates that the sequences selected for constructing the matrix share an average identity value of 62%.

This is why the PAM matrices are used most often for reconstructing **(J) ogctnihpyele** trees. However, because of the mathematical **(I) earoopatitnlx** procedure used, the PAM values may be less realistic for **(H) neirtdgve** sequences.

