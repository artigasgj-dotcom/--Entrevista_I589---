from pdfrw import PdfReader, PdfWriter, PageMerge

# Mapeo de campos del formulario PDF (usa nombres reales del PDF)
campos = {
    'topmostSubform[0].Page1[0].Line1_FullName[0]': 'JORGE ARTIGAS',
    'topmostSubform[0].Page1[0].Line2_DOB[0]': '1985-07-12',
    'topmostSubform[0].Page1[0].Line3_Country[0]': 'URUGUAY',
    'topmostSubform[0].Page1[0].Line4_Gender[0]': 'Masculino',
    'topmostSubform[0].Page1[0].Line5_MaritalStatus[0]': 'Soltero',
    # Agrega más campos según el formulario
}

def llenar_formulario(input_pdf, output_pdf, datos):
    template = PdfReader(input_pdf)
    for page in template.pages:
        annotations = page.Annots
        if annotations:
            for annotation in annotations:
                if annotation.Subtype == '/Widget' and annotation.T:
                    key = annotation.T[1:-1]  # Elimina paréntesis
                    if key in datos:
                        annotation.V = f'({datos[key]})'
                        annotation.AP = None  # Refresca visualmente

    PdfWriter().write(output_pdf, template)

# Ejecutar
llenar_formulario("I-589_original.pdf", "I-589_lleno.pdf", campos)