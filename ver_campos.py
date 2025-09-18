from pdfrw import PdfReader

pdf = PdfReader("I-589_original.pdf")

for page in pdf.pages:
    annotations = page.Annots
    if annotations:
        for annotation in annotations:
            if annotation.Subtype == '/Widget' and annotation.T:
                print(annotation.T)