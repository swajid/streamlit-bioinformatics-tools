import streamlit as st
from Bio.Seq import Seq

def calculate_gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    gc_content = ((g + c) / len(sequence)) * 100
    return gc_content

def transcribe_dna_to_protein(sequence):
    try:
        dna_seq = Seq(sequence.upper())
        protein_seq = dna_seq.translate()
        return str(protein_seq)
    except Exception as e:
        return str(e)

def main():
    st.title("DNA Tools")
    st.write("This app can calculate various properties of a sequence of DNA")

    option = st.selectbox("Choose an option:", ("Calculate GC Content", "Transcribe DNA to Protein"))

    sequence = st.text_area("Enter your DNA sequence here:", height=400)

    if st.button("Submit"):
        if sequence:
            if option == "Calculate GC Content":
                gc_content = calculate_gc_content(sequence.upper())
                st.success(f"The GC content of the given sequence is {gc_content:.2f}%.")
            elif option == "Transcribe DNA to Protein":
                protein = transcribe_dna_to_protein(sequence.upper())
                st.success(f"The translated protein sequence is: {protein}")
        else:
            st.error("Please enter a valid genome sequence.")

if __name__ == "__main__":
    main()

