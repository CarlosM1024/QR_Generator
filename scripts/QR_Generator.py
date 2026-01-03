"""
Generador de Códigos QR con PyQt5
Versión mejorada con campo de URL y layouts responsivos
"""

import sys
from typing import Optional
import PIL
from PIL import Image, ImageDraw
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    RoundedModuleDrawer, VerticalBarsDrawer, SquareModuleDrawer,
    CircleModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer
)
from qrcode.image.styles.colormasks import SolidFillColorMask
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog, QMessageBox
from PyQt5 import QtCore
from QR_Generator.scripts.UI_QR_Generator import Ui_MainWindow


class QRGenerator(QMainWindow):
    """Clase principal para el generador de códigos QR"""
    
    # Mapeo de estilos de módulos
    MODULE_DRAWERS = {
        "SquareModuleDrawer": SquareModuleDrawer,
        "GappedSquareModuleDrawer": GappedSquareModuleDrawer,
        "CircleModuleDrawer": CircleModuleDrawer,
        "RoundedModuleDrawer": RoundedModuleDrawer,
        "VerticalBarsDrawer": VerticalBarsDrawer,
        "HorizontalBarsDrawer": HorizontalBarsDrawer
    }
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Variables de instancia
        self.imagen_path: Optional[str] = None
        self.color_modulo = QColor(0, 0, 0)  # Negro por defecto
        self.color_inner = QColor(0, 0, 0)
        self.color_outer = QColor(0, 0, 0)
        
        # Configurar PIL para compatibilidad
        if not hasattr(PIL.Image, 'Resampling'):
            PIL.Image.Resampling = PIL.Image
        
        # Conectar señales
        self._conectar_senales()
        
        # Inicializar colores en la UI
        self._actualizar_color_frame(self.ui.frame, self.color_modulo)
        self._actualizar_color_frame(self.ui.frame_2, self.color_inner)
        self._actualizar_color_frame(self.ui.frame_3, self.color_outer)
        
        # URL por defecto
        self.ui.lineEdit_url.setText("https://github.com/CarlosM1024")
        
        # Actualizar barra de estado
        self.ui.statusbar.showMessage("Listo para generar códigos QR")
    
    def _conectar_senales(self):
        """Conecta todas las señales de los widgets"""
        self.ui.pushButton_1.clicked.connect(self.seleccionar_color_modulo)
        self.ui.pushButton_2.clicked.connect(self.seleccionar_color_inner)
        self.ui.pushButton_3.clicked.connect(self.seleccionar_color_outer)
        self.ui.pushButton_4.clicked.connect(self.cargar_imagen)
        self.ui.pushButton.clicked.connect(self.borrar_imagen)
        self.ui.actionGuardar.triggered.connect(self.guardar_qr)
        
        # Conectar señal de cambio de texto en URL
        self.ui.lineEdit_url.textChanged.connect(self._validar_url)
    
    def _validar_url(self, texto):
        """Valida y da feedback sobre el texto ingresado"""
        if not texto.strip():
            self.ui.statusbar.showMessage("⚠️ Ingresa una URL o texto para el QR")
            self.ui.lineEdit_url.setStyleSheet("""
                QLineEdit {
                    background-color: white;
                    border: 2px solid rgb(255, 180, 0);
                    border-radius: 5px;
                    padding: 8px;
                    font-size: 11pt;
                }
            """)
        else:
            self.ui.statusbar.showMessage(f"✓ Listo para generar QR ({len(texto)} caracteres)")
            self.ui.lineEdit_url.setStyleSheet("""
                QLineEdit {
                    background-color: white;
                    border: 2px solid rgb(150, 150, 150);
                    border-radius: 5px;
                    padding: 8px;
                    font-size: 11pt;
                }
                QLineEdit:focus {
                    border: 2px solid rgb(255, 85, 0);
                }
            """)
    
    def cargar_imagen(self):
        """Carga y muestra una imagen para el centro del QR"""
        filtro = "Imágenes (*.jpg *.jpeg *.png)"
        archivo, _ = QFileDialog.getOpenFileName(
            self, 
            "Seleccionar imagen para QR", 
            "", 
            filtro
        )
        
        if not archivo:
            return
        
        try:
            self.imagen_path = archivo
            pixmap = QPixmap(archivo)
            
            # Reescalar imagen
            tamanio = QtCore.QSize(180, 180)
            pixmap_reescalado = pixmap.scaled(
                tamanio, 
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )
            
            self.ui.label.setPixmap(pixmap_reescalado)
            self.ui.statusbar.showMessage(f"✓ Imagen cargada: {archivo.split('/')[-1]}")
            print(f"Imagen cargada: {archivo}")
            
        except Exception as e:
            QMessageBox.warning(
                self, 
                "Error", 
                f"No se pudo cargar la imagen:\n{str(e)}"
            )
            self.ui.statusbar.showMessage("❌ Error al cargar imagen")
    
    def borrar_imagen(self):
        """Borra la imagen cargada"""
        self.imagen_path = None
        self.ui.label.clear()
        self.ui.label.setText("Sin imagen")
        self.ui.statusbar.showMessage("🗑️ Imagen eliminada")
    
    def seleccionar_color_modulo(self):
        """Abre el diálogo para seleccionar color del módulo"""
        color = QColorDialog.getColor(self.color_modulo, self, "Seleccionar color del módulo")
        if color.isValid():
            self.color_modulo = color
            self._actualizar_color_frame(self.ui.frame, color)
            self.ui.statusbar.showMessage(f"✓ Color del módulo actualizado: {color.name()}")
    
    def seleccionar_color_inner(self):
        """Abre el diálogo para seleccionar color del Inner Eye"""
        color = QColorDialog.getColor(self.color_inner, self, "Seleccionar color Inner Eye")
        if color.isValid():
            self.color_inner = color
            self._actualizar_color_frame(self.ui.frame_2, color)
            self.ui.statusbar.showMessage(f"✓ Color Inner Eye actualizado: {color.name()}")
    
    def seleccionar_color_outer(self):
        """Abre el diálogo para seleccionar color del Outer Eye"""
        color = QColorDialog.getColor(self.color_outer, self, "Seleccionar color Outer Eye")
        if color.isValid():
            self.color_outer = color
            self._actualizar_color_frame(self.ui.frame_3, color)
            self.ui.statusbar.showMessage(f"✓ Color Outer Eye actualizado: {color.name()}")
    
    def _actualizar_color_frame(self, frame, color: QColor):
        """Actualiza el color de fondo de un frame"""
        frame.setStyleSheet(f"""
            QFrame {{
                background-color: {color.name()};
                border: 2px solid rgb(150, 150, 150);
                border-radius: 5px;
            }}
        """)
    
    def _obtener_rgb(self, color: QColor) -> tuple:
        """Convierte QColor a tupla RGB"""
        return (color.red(), color.green(), color.blue())
    
    def _crear_mascara_inner_eyes(self, img: Image) -> Image:
        """Crea la máscara para los ojos internos del QR"""
        img_size = img.size[0]
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        
        # Dibujar los tres ojos internos
        draw.rectangle((60, 60, 90, 90), fill=255)  # Superior izquierdo
        draw.rectangle((img_size - 90, 60, img_size - 60, 90), fill=255)  # Superior derecho
        draw.rectangle((60, img_size - 90, 90, img_size - 60), fill=255)  # Inferior izquierdo
        
        return mask
    
    def _crear_mascara_outer_eyes(self, img: Image) -> Image:
        """Crea la máscara para los ojos externos del QR"""
        img_size = img.size[0]
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        
        # Dibujar los tres marcos externos
        draw.rectangle((40, 40, 110, 110), fill=255)
        draw.rectangle((img_size - 110, 40, img_size - 40, 110), fill=255)
        draw.rectangle((40, img_size - 110, 110, img_size - 40), fill=255)
        
        # Quitar el centro (inner eyes)
        draw.rectangle((60, 60, 90, 90), fill=0)
        draw.rectangle((img_size - 90, 60, img_size - 60, 90), fill=0)
        draw.rectangle((60, img_size - 90, 90, img_size - 60), fill=0)
        
        return mask
    
    def _obtener_drawer(self, combo_text: str):
        """Obtiene la clase drawer correspondiente al texto del combo"""
        drawer_class = self.MODULE_DRAWERS.get(combo_text)
        if drawer_class == SquareModuleDrawer:
            return drawer_class(radius_ratio=1)
        return drawer_class()
    
    def _generar_qr_con_estilo(self, qr, drawer, color: QColor, is_eye: bool = False):
        """Genera una imagen QR con el estilo especificado"""
        rgb_color = self._obtener_rgb(color)
        
        kwargs = {
            'image_factory': StyledPilImage,
            'color_mask': SolidFillColorMask(
                back_color=(255, 255, 255),  # Siempre blanco para el fondo
                front_color=rgb_color
            )
        }
        
        # Solo agregar imagen si existe y no está vacía
        if self.imagen_path and len(self.imagen_path) > 0:
            kwargs['embeded_image_path'] = self.imagen_path
        
        if is_eye:
            kwargs['eye_drawer'] = drawer
        else:
            kwargs['module_drawer'] = drawer
        
        return qr.make_image(**kwargs)
    
    def guardar_qr(self):
        """Genera y guarda el código QR con todos los estilos aplicados"""
        # Validar que haya URL
        url_texto = self.ui.lineEdit_url.text().strip()
        if not url_texto:
            QMessageBox.warning(
                self,
                "URL vacía",
                "Por favor ingresa una URL o texto para generar el código QR."
            )
            self.ui.lineEdit_url.setFocus()
            return
        
        try:
            self.ui.statusbar.showMessage("⏳ Generando código QR...")
            
            # Obtener los drawers seleccionados
            drawer_modulo = self._obtener_drawer(self.ui.comboBox.currentText())
            drawer_inner = self._obtener_drawer(self.ui.comboBox_2.currentText())
            drawer_outer = self._obtener_drawer(self.ui.comboBox_3.currentText())
            
            # Crear el objeto QR
            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(url_texto)
            qr.make()  # Importante: generar la matriz del QR
            
            # Generar las tres capas del QR
            qr_modulo = self._generar_qr_con_estilo(qr, drawer_modulo, self.color_modulo, is_eye=False)
            qr_inner = self._generar_qr_con_estilo(qr, drawer_inner, self.color_inner, is_eye=True)
            qr_outer = self._generar_qr_con_estilo(qr, drawer_outer, self.color_outer, is_eye=True)
            
            # Convertir a RGB
            img_modulo_rgb = qr_modulo.convert("RGB")
            img_inner_rgb = qr_inner.convert("RGB")
            img_outer_rgb = qr_outer.convert("RGB")
            
            # Crear máscaras
            mascara_inner = self._crear_mascara_inner_eyes(img_modulo_rgb)
            mascara_outer = self._crear_mascara_outer_eyes(img_modulo_rgb)
            
            # Componer las imágenes
            img_intermedia = Image.composite(img_inner_rgb, img_modulo_rgb, mascara_inner)
            img_final = Image.composite(img_outer_rgb, img_intermedia, mascara_outer)
            
            # Guardar archivo
            filtro = "Imagen PNG (*.png);;Imagen JPG (*.jpg);;Imagen JPEG (*.jpeg);;Todos los archivos (*)"
            nombre_archivo, _ = QFileDialog.getSaveFileName(
                self, 
                "Guardar código QR", 
                "QR_Final.png", 
                filtro
            )
            
            if nombre_archivo:
                img_final.save(nombre_archivo)
                self.ui.statusbar.showMessage(f"✅ QR guardado: {nombre_archivo.split('/')[-1]}")
                QMessageBox.information(
                    self, 
                    "Éxito", 
                    f"Código QR guardado correctamente en:\n{nombre_archivo}\n\n"
                    f"Contenido: {url_texto[:50]}{'...' if len(url_texto) > 50 else ''}"
                )
                print(f"QR guardado: {nombre_archivo}")
            else:
                self.ui.statusbar.showMessage("❌ Guardado cancelado")
            
        except Exception as e:
            import traceback
            error_detallado = traceback.format_exc()
            QMessageBox.critical(
                self, 
                "Error", 
                f"Error al generar el código QR:\n{str(e)}\n\nDetalles:\n{error_detallado}"
            )
            self.ui.statusbar.showMessage(f"❌ Error: {str(e)}")
            print(f"Error completo:\n{error_detallado}")


def main():
    """Función principal"""
    app = QApplication(sys.argv)
    
    # Configurar estilo de la aplicación
    app.setStyle('Fusion')
    
    ventana = QRGenerator()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()