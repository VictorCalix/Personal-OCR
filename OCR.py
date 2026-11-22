import os
from PIL import ImageGrab, ImageEnhance, ImageFilter
import pytesseract
import pyperclip

print("Ejecutando OCR desde captura... ")
# Usar el Tesseract incluido en el proyecto (OCRdependencias), no el del sistema
base = os.path.dirname(os.path.abspath(__file__))
pytesseract.pytesseract.tesseract_cmd = os.path.join(base, 'OCRdependencias', 'Tesseract', 'tesseract.exe')

# Captura la imagen del portapapeles
imagen = ImageGrab.grabclipboard()

if imagen:
    # Mejorar la imagen: convertirla a escala de grises, mejorar contraste y enfocar
    imagen = imagen.convert('L')  # Convertir a escala de grises
    imagen = imagen.filter(ImageFilter.SHARPEN)  # Enfocar la imagen
    enhancer = ImageEnhance.Contrast(imagen)
    imagen = enhancer.enhance(2)  # Aumentar contraste

    # Extraer texto de la imagen (con configuración especial para números)
    custom_config = r'--oem 3 --psm 6'  # Configuración para mejorar OCR
    texto = pytesseract.image_to_string(imagen, lang='spa', config=custom_config)
    
    # Verificar si el texto no está vacío antes de copiarlo
    if texto.strip():
        # Copiar al portapapeles
        pyperclip.copy(texto)
        print("Texto extraído y copiado al portapapeles:")  # Puedes ver el resultado aquí
        print("-" * 40)
        print(texto)
    else:
        print("No se pudo extraer texto de la imagen.")
else:
    print("No hay imagen en el portapapeles. Copia una captura 📸.")
