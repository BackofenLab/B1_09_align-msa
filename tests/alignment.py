class RepresentationMSA:
    def __init__(self, *sequences):
        self.sequences = sequences
        self._check_length()
        self._to_sorted_lower()

    def _check_length(self):
        if len(set([len(seq) for seq in self.sequences])) != 1:
            raise ValueError("Sequences of different length are present in the alignment")

    def _to_sorted_lower(self):
        self.sequences = [seq.lower() for seq in self.sequences]
        self.sequences = sorted(self.sequences)

    def __repr__(self):
        return "\n".join(self.sequences)

    def __eq__(self, other):
        return self.sequences == other.sequences


if __name__ == "__main__":
    seq1 = "wabba_dabba_buMM"
    seq2 = "________________"
    seq3 = "__g man_________"

    seq4 = "WABba_dabba_buMM"
    seq5 = "__G MAN_________"
    seq6 = "________________"

    r_1 = RepresentationMSA(seq1, seq2, seq3)
    r_2 = RepresentationMSA(seq4, seq5, seq6)
    print(r_1 == r_2)
    print(r_1)