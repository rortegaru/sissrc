import re

# Archivo de entrada y salida
input_file = "Methods.rst"
output_file = "Methods_updated.rst"

# Leer el contenido del archivo
with open(input_file, "r") as f:
    content = f.read()

# Reemplazar :raw-latex:\citealp por :cite:
updated_content = re.sub(r":raw-latex:`\\citealp{([^}]*)}`", r":cite:`\1`", content)
updated_content = re.sub(r":raw-latex:`\\citep{([^}]*)}`", r":cite:`\1`", updated_content)

# Guardar los cambios en un nuevo archivo
with open(output_file, "w") as f:
    f.write(updated_content)

print(f"Archivo actualizado guardado como {output_file}")
