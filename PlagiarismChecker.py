
#Retrieves all text files in the specified directory.
#Reads and returns the content of each file in the provided list.
#Calculates and returns the Jaccard similarity between two documents based on their sets of words.
#Compares each document with every other document to detect similarities and returns a set of results 
# indicating potential plagiarism


import os

def get_student_files(directory='.'):
    return [doc for doc in os.listdir(directory) if doc.endswith('.txt')]

def read_student_notes(files):
    return [open(_file, encoding='utf-8').read() for _file in files]

def jaccard_similarity(doc1, doc2):
    words_doc1 = set(doc1.split())
    words_doc2 = set(doc2.split())
    intersection = words_doc1.intersection(words_doc2)
    union = words_doc1.union(words_doc2)
    return len(intersection) / len(union)

def check_plagiarism(files, notes):
    plagiarism_results = set()
    for i, (student_a, note_a) in enumerate(zip(files, notes)):
        for j, (student_b, note_b) in enumerate(zip(files, notes)):
            if i != j:
                sim_score = jaccard_similarity(note_a, note_b)
                student_pair = tuple(sorted([student_a, student_b]))
                plagiarism_results.add((student_pair[0], student_pair[1], sim_score))
    return plagiarism_results

def main():
    student_files = get_student_files()
    student_notes = read_student_notes(student_files)
    
    plagiarism_results = check_plagiarism(student_files, student_notes)
    for result in plagiarism_results:
        print(result)

if __name__ == "__main__":
    main()
