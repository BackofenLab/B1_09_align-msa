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

Scoring matrices reflect the fact that amino acids with similar (A) isehcayhilccpmo properties can be more easily substituted than those without similar characteristics, since they are more likely to cause (B) rsistnupoid to the structure and function. This type of disruptive (C) uuttotsbnisi is less likely to be selected in evolution because it renders (D) iouanctfnlonn proteins.

PAM matrices, except PAM1, are derived from an (E) raniyeooutvl model. The increasing PAM numbers correlate with increasing PAM units and thus evolutionary (F) tsnascedi of protein sequences. For example, PAM250, which corresponds to about 20% amino acid (G) tyedniti, represents 250 mutations per 100 residues (a position could mutate several times). In theory, the number of (E) raniyeooutvl changes approximately corresponds to an expected (E) raniyeooutvl span of 2,500 million years. Thus, the PAM250 matrix is normally used for (H) neirtdgve sequences.

BLOSUM matrices are derived based on direct observation for every possible amino acid (C) uuttotsbnisi in multiple sequence alignments. Instead of using the (I) earoopatitnlx function, the BLOSUM matrices are actual percentage identity values of sequences selected for construction of the matrices. For example, BLOSUM62 indicates that the sequences selected for constructing the matrix share an average identity value of 62%.

This is why the PAM matrices are used most often for reconstructing (J) ogctnihpyele trees. However, because of the mathematical (I) earoopatitnlx procedure used, the PAM values may be less realistic for (H) neirtdgve sequences.

### _Exercise 3: Pratical application of multiple sequence alignment_


Multiple sequence alignments (MSA) are a key starting point for the prediction of protein secondary structure, residue accessibility and function. One of the challenges in MSA is the choice of the adequate scoring matrix. In the case of protein sequences, the scoring matrices reflect the physicochemical properties of amino acid residues, as well as the likelihood of certain residues being substituted among true homologous sequences. In this exercise we are going to analyze the effects of using two different scoring matrices on the alignments.

---
**NOTE**

if you are using Windows, there are three possible ways to use MAFFT:

1. You can use an [online service](https://mafft.cbrc.jp/alignment/server/) to run MAFFT
2. You can follow [this tutorial](https://mafft.cbrc.jp/alignment/software/windows_cygwin.html) in order to run the analysis in Cywig, a tool that provides a UNIX/Linux-like shell emulated over Windows.
3. You can create a [bootable Linux USB drive](https://www.lifewire.com/try-lubuntu-16-04-windows-10-4037886).



When using the online tool please select the corresponding Scoring (BLOSUM30/80) via the "Scoring matrix for amino acid sequences:" parameter. You can use the defaults for the remaining settings.

---

First, you need to clone/download the assignment:

```
$ git clone git@github.com:Bioinformatics-teaching/lecture-09-aling-msa-userID.git
$ cd lecture-09-aling-msa-userID.git
```

Do not forget to use your own user ID. Now, we'll install [conda](https://docs.conda.io/projects/conda/en/latest/index.html), an open source package and environment management system.

```
$ curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh

$ conda config --add channels defaults
$ conda config --add channels bioconda
$ conda config --add channels conda-forge
```

Next,  we'll create an environment (a directory that contains a specific collection of packages), and will install the requited package.

```
$ conda create -n alignments
$ conda activate alignmens
$ conda install mafft
```

Finally, let's compute the pairwise alignments of all sequences with the Needleman-Wunsch algorithm by using the BLOSUM30 and BLOSUM80 matrices:

```
$ mafft --bl 30 --reorder --globalpair --clustalout sequences/sars_cov2.fasta > alignment_blosum30.maf
$ mafft --bl 80 --reorder --globalpair --clustalout sequences/sars_cov2.fasta > alignment_blosum80.maf
```

**a)** What is the most similar sequence to the omicron variant when using the BLOSUM30 matrix?

- [ ] A. Beta
- [ ] B. Delta
- [ ] C. Gamma

**b)** And when using the BLOSUM80 matrix?

- [ ] A. Beta
- [ ] B. Delta
- [ ] C. Gamma

**c)** Which result do you think is more acceptable, taking in account that the percentage of identity is over 95%?

- [ ] A. The result obtained when using the BLOSUM80 matrix is more significant, since this matrix is more suitable for sequences that have more evolutionary distance between them.
- [ ] B. The result obtained when using the BLOSUM30 matrix is more significant, since this matrix is more suitable for sequences that have less evolutionary distance between them.
- [ ] C. The result obtained when using the BLOSUM80 matrix is more significant, since this matrix is more suitable for sequences that have less evolutionary distance between them.

Finally, you can remove conda if you consider that you won't need it any more.

```
$ rm -rf ~/miniconda3
```

### _Exercise 4 - Programming assignment:_

