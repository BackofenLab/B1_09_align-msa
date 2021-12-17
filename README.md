Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 9: Multiple Sequence Alignment
---

### _Exercise 1 - Multiple Sequence Alignment (MSA)_


**a)**


**b)** Which of the following statements regarding multiple sequence alignment are correct?

- [ ] Multiple sequence alignments are important to identify evolutionary conserved sequence features.
- [ ] A multiple sequence alignment can only be as long as the longest sequence involved in the alignment.
- [ ] There is no exact solution for the multiple sequence alignment problem.
- [ ] The Feng \& Doolittle algorithm implements a progressive alignment approach.
- [ ] The results of Feng \& Doolittle depend on order in which input sequences are processed.


### _Exercise 2 - Progressive Alignment by Feng and Doolittle_

Given the sequences S<sub>1</sub> = CTCACA, S<sub>2</sub> = CAC, S<sub>3</sub> = GTAC and the following scoring function:

<p align="center">
  <img src="./figures/sheet9-exercise2-score.svg" alt="score" width=60%/>
</p>

We want to do progressive alignment following Feng and Doolittle. The needed pairwise alignments are calculated using the Needleman-Wunsch and are as follows:

<p align="center">
  <img src="./figures/sheet9-exercise2-alignments.svg" alt="alignments" width=45%/>
</p>

The following guide trees are given in [Newick format](https://en.wikipedia.org/wiki/Newick_format).

**a)** Given the guide tree ((S<sub>1</sub>, S<sub>3</sub>), S<sub>2</sub>), what are the possible resulting multiple sequence alignments?

Use the Needleman-Wunsch implementation of the [Freiburg RNA tools webserver (Teaching)](http://rna.informatik.uni-freiburg.de/) to recompute the pairwise alignments.

In case the webserver is not available, you can find the resulting here:

<details>
  <summary>Spoiler: (Click to open)</summary>
    <p align="center">
    <img src="./figures/sheet9-exercise2-alignment-sol1.svg" alt="alignement1" width=60%/>
    </p>
</details>

Additionally, calculate the sum-of-pairs scores for each of the computed alignments, when replacing all placeholders ('X') with gaps.

**b)** What are the alignments and sum-of-pairs scores for the guide tree ((S<sub>2</sub>, S<sub>3</sub>), S<sub>1</sub>)?

<details>
  <summary>Spoiler: (Click to open)</summary>
    <p align="center">
    <img src="./figures/sheet9-exercise2-alignment-sol2.svg" alt="alignement1" width=60%/>
    </p>
</details>

### _Exercise 3 - Programming assignment:_

