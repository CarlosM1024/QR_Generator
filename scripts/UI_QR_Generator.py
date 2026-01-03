# -*- coding: utf-8 -*-

"""
UI para Generador de Códigos QR
Versión mejorada con campo de URL y layouts responsivos

ADVERTENCIA: Este archivo puede ser regenerado por pyuic5.
Las mejoras personalizadas están claramente marcadas.
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """Interfaz de usuario para el generador de códigos QR"""
    
    def setupUi(self, MainWindow):
        """Configura la interfaz de usuario"""
        # Configuración de la ventana principal
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 650)
        MainWindow.setMinimumSize(QtCore.QSize(600, 650))
        
        # Widget central
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(79, 159, 118);")
        self.centralwidget.setObjectName("centralwidget")
        
        # Layout principal
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(20, 15, 20, 15)
        main_layout.setSpacing(10)
        
        # === TÍTULO ===
        self._setup_title(main_layout)
        
        # Layout horizontal para las dos columnas
        content_layout = QtWidgets.QHBoxLayout()
        content_layout.setSpacing(20)
        
        # === COLUMNA IZQUIERDA: Controles ===
        left_widget = self._setup_controls_section()
        content_layout.addWidget(left_widget, stretch=3)
        
        # === COLUMNA DERECHA: Preview y URL ===
        right_widget = self._setup_right_section()
        content_layout.addWidget(right_widget, stretch=2)
        
        main_layout.addLayout(content_layout)
        
        # === MENÚ Y BARRA DE ESTADO ===
        self._setup_menu_bar(MainWindow)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Conectar señales
        self._connect_signals()
        
        # Traducir textos
        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def _setup_title(self, parent_layout):
        """Configura el título de la aplicación"""
        self.label_3 = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255); padding: 5px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        parent_layout.addWidget(self.label_3)
    
    def _setup_controls_section(self):
        """Configura la sección de controles de estilo"""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)
        
        # === MÓDULO CENTRAL ===
        self._setup_module_controls(layout)
        
        # Separador
        layout.addWidget(self._create_separator())
        
        # === INNER EYES ===
        self._setup_inner_eye_controls(layout)
        
        # Separador
        layout.addWidget(self._create_separator())
        
        # === OUTER EYES ===
        self._setup_outer_eye_controls(layout)
        
        # Espaciador al final
        layout.addStretch()
        
        return widget
    
    def _setup_right_section(self):
        """Configura la sección derecha con URL, preview y botones"""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        
        # === SECCIÓN URL ===
        url_group = QtWidgets.QGroupBox()
        url_group.setStyleSheet("""
            QGroupBox {
                background-color: rgba(255, 255, 255, 0.1);
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                margin-top: 10px;
                padding: 15px;
                font-weight: bold;
                color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        url_group.setTitle("URL del Código QR")
        
        url_layout = QtWidgets.QVBoxLayout(url_group)
        url_layout.setSpacing(8)
        
        # Label de instrucción
        self.label_url_info = QtWidgets.QLabel()
        self.label_url_info.setStyleSheet("color: white; font-weight: normal; font-style: italic;")
        self.label_url_info.setWordWrap(True)
        url_layout.addWidget(self.label_url_info)
        
        # Campo de texto para URL
        self.lineEdit_url = QtWidgets.QLineEdit()
        self.lineEdit_url.setStyleSheet("""
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
        self.lineEdit_url.setPlaceholderText("https://ejemplo.com")
        self.lineEdit_url.setClearButtonEnabled(True)
        self.lineEdit_url.setObjectName("lineEdit_url")
        url_layout.addWidget(self.lineEdit_url)
        
        layout.addWidget(url_group)
        
        # === SECCIÓN IMAGEN ===
        image_group = QtWidgets.QGroupBox()
        image_group.setStyleSheet("""
            QGroupBox {
                background-color: rgba(255, 255, 255, 0.1);
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                margin-top: 10px;
                padding: 15px;
                font-weight: bold;
                color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        image_group.setTitle("Imagen del QR (Opcional)")
        
        image_layout = QtWidgets.QVBoxLayout(image_group)
        image_layout.setSpacing(10)
        
        # Preview de imagen
        self.label = QtWidgets.QLabel()
        self.label.setMinimumSize(QtCore.QSize(180, 180))
        self.label.setMaximumSize(QtCore.QSize(180, 180))
        self.label.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 255, 255);
                border: 2px solid rgb(200, 200, 200);
                border-radius: 5px;
            }
        """)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Sin imagen")
        self.label.setObjectName("label")
        image_layout.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)
        
        # Botón seleccionar imagen
        self.pushButton_4 = QtWidgets.QPushButton()
        self.pushButton_4.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 85, 0);
                color: rgb(255, 255, 255);
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
                font-size: 10pt;
            }
            QPushButton:hover {
                background-color: rgb(255, 105, 20);
            }
            QPushButton:pressed {
                background-color: rgb(235, 75, 0);
            }
        """)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        image_layout.addWidget(self.pushButton_4)
        
        # Botón borrar imagen
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(180, 180, 180);
                color: rgb(50, 50, 50);
                border: none;
                border-radius: 5px;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgb(200, 200, 200);
            }
            QPushButton:pressed {
                background-color: rgb(160, 160, 160);
            }
        """)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        image_layout.addWidget(self.pushButton)
        
        layout.addWidget(image_group)
        
        # Espaciador
        layout.addStretch()
        
        return widget
    
    def _setup_module_controls(self, parent_layout):
        """Configura los controles del módulo central"""
        # Título de sección
        self.label_2 = self._create_section_label("Centro:", 12, bold=True)
        parent_layout.addWidget(self.label_2)
        
        # Subtítulo
        self.label_8 = self._create_subtitle_label("Forma del centro del QR")
        parent_layout.addWidget(self.label_8)
        
        # ComboBox de formas
        self.comboBox = self._create_styled_combobox()
        self.comboBox.setObjectName("comboBox")
        self._populate_combobox(self.comboBox)
        parent_layout.addWidget(self.comboBox)
        
        # Subtítulo de color
        self.label_9 = self._create_subtitle_label("Color del centro del QR")
        parent_layout.addWidget(self.label_9)
        
        # Layout horizontal para botón y preview de color
        color_layout = QtWidgets.QHBoxLayout()
        color_layout.setSpacing(10)
        
        self.pushButton_1 = self._create_color_button("pushButton_1")
        color_layout.addWidget(self.pushButton_1)
        
        self.frame = self._create_color_preview_frame("frame")
        color_layout.addWidget(self.frame)
        
        parent_layout.addLayout(color_layout)
    
    def _setup_inner_eye_controls(self, parent_layout):
        """Configura los controles del Inner Eye"""
        # Título de sección
        self.label_4 = self._create_section_label("Inner Eyes:", 12, bold=True)
        parent_layout.addWidget(self.label_4)
        
        # Subtítulo
        self.label_10 = self._create_subtitle_label("Forma del Inner Eye")
        parent_layout.addWidget(self.label_10)
        
        # ComboBox de formas
        self.comboBox_2 = self._create_styled_combobox()
        self.comboBox_2.setObjectName("comboBox_2")
        self._populate_combobox(self.comboBox_2)
        parent_layout.addWidget(self.comboBox_2)
        
        # Subtítulo de color
        self.label_11 = self._create_subtitle_label("Color del Inner Eye")
        parent_layout.addWidget(self.label_11)
        
        # Layout horizontal para botón y preview de color
        color_layout = QtWidgets.QHBoxLayout()
        color_layout.setSpacing(10)
        
        self.pushButton_2 = self._create_color_button("pushButton_2")
        color_layout.addWidget(self.pushButton_2)
        
        self.frame_2 = self._create_color_preview_frame("frame_2")
        color_layout.addWidget(self.frame_2)
        
        parent_layout.addLayout(color_layout)
    
    def _setup_outer_eye_controls(self, parent_layout):
        """Configura los controles del Outer Eye"""
        # Título de sección
        self.label_5 = self._create_section_label("Outer Eyes:", 12, bold=True)
        parent_layout.addWidget(self.label_5)
        
        # Subtítulo
        self.label_12 = self._create_subtitle_label("Forma del Outer Eye")
        parent_layout.addWidget(self.label_12)
        
        # ComboBox de formas
        self.comboBox_3 = self._create_styled_combobox()
        self.comboBox_3.setObjectName("comboBox_3")
        self._populate_combobox(self.comboBox_3)
        parent_layout.addWidget(self.comboBox_3)
        
        # Subtítulo de color
        self.label_13 = self._create_subtitle_label("Color del Outer Eye")
        parent_layout.addWidget(self.label_13)
        
        # Layout horizontal para botón y preview de color
        color_layout = QtWidgets.QHBoxLayout()
        color_layout.setSpacing(10)
        
        self.pushButton_3 = self._create_color_button("pushButton_3")
        color_layout.addWidget(self.pushButton_3)
        
        self.frame_3 = self._create_color_preview_frame("frame_3")
        color_layout.addWidget(self.frame_3)
        
        parent_layout.addLayout(color_layout)
    
    def _setup_menu_bar(self, MainWindow):
        """Configura el menú y barra de estado"""
        # Barra de menú
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        
        # Menú Archivo
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        
        MainWindow.setMenuBar(self.menubar)
        
        # Barra de estado
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Acciones del menú
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar.setShortcut("Ctrl+S")
        
        self.menuArchivo.addAction(self.actionGuardar)
        self.menubar.addAction(self.menuArchivo.menuAction())
    
    def _connect_signals(self):
        """Conecta las señales de los widgets"""
        self.pushButton.clicked.connect(self.label.clear)
    
    # === MÉTODOS AUXILIARES PARA CREAR WIDGETS ===
    
    def _create_section_label(self, text, point_size, bold=False):
        """Crea una etiqueta de sección"""
        label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(point_size)
        font.setBold(bold)
        font.setWeight(75 if bold else 50)
        label.setFont(font)
        label.setStyleSheet("color: white; padding: 5px 0;")
        return label
    
    def _create_subtitle_label(self, text):
        """Crea una etiqueta de subtítulo en itálica"""
        label = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setItalic(True)
        font.setPointSize(9)
        label.setFont(font)
        label.setStyleSheet("color: rgba(255, 255, 255, 0.9); padding: 2px 0;")
        return label
    
    def _create_separator(self):
        """Crea una línea separadora"""
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setStyleSheet("background-color: rgba(255, 255, 255, 0.3);")
        line.setFixedHeight(2)
        return line
    
    def _create_styled_combobox(self):
        """Crea un ComboBox con estilo personalizado"""
        combobox = QtWidgets.QComboBox()
        combobox.setStyleSheet("""
            QComboBox {
                background-color: rgb(255, 255, 255);
                border: 2px solid rgb(150, 150, 150);
                border-radius: 5px;
                padding: 6px 10px;
                min-height: 25px;
                font-size: 10pt;
            }
            QComboBox:hover {
                border: 2px solid rgb(255, 85, 0);
                background-color: rgb(255, 255, 255);
            }
            QComboBox:focus {
                border: 2px solid rgb(255, 85, 0);
            }
            QComboBox::drop-down {
                border: none;
                width: 25px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid rgb(80, 80, 80);
                margin-right: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                border: 2px solid rgb(150, 150, 150);
                selection-background-color: rgb(255, 85, 0);
                selection-color: white;
                padding: 5px;
            }
        """)
        combobox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        return combobox
    
    def _create_color_button(self, object_name):
        """Crea un botón para selección de color"""
        button = QtWidgets.QPushButton()
        button.setStyleSheet("""
            QPushButton {
                background-color: rgb(255, 255, 255);
                border: 2px solid rgb(150, 150, 150);
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;
                color: rgb(50, 50, 50);
            }
            QPushButton:hover {
                background-color: rgb(255, 255, 255);
                border: 2px solid rgb(255, 85, 0);
            }
            QPushButton:pressed {
                background-color: rgb(240, 240, 240);
            }
        """)
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        button.setObjectName(object_name)
        return button
    
    def _create_color_preview_frame(self, object_name):
        """Crea un frame para mostrar preview del color"""
        frame = QtWidgets.QFrame()
        frame.setStyleSheet("""
            QFrame {
                background-color: rgb(0, 0, 0);
                border: 2px solid rgb(150, 150, 150);
                border-radius: 5px;
            }
        """)
        frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Plain)
        frame.setMinimumSize(QtCore.QSize(60, 35))
        frame.setMaximumSize(QtCore.QSize(80, 35))
        frame.setObjectName(object_name)
        return frame
    
    def _populate_combobox(self, combobox):
        """Llena un ComboBox con las opciones de estilos"""
        items = [
            "SquareModuleDrawer",
            "GappedSquareModuleDrawer",
            "CircleModuleDrawer",
            "RoundedModuleDrawer",
            "VerticalBarsDrawer",
            "HorizontalBarsDrawer"
        ]
        for item in items:
            combobox.addItem(item)
    
    def retranslateUi(self, MainWindow):
        """Traduce todos los textos de la interfaz"""
        _translate = QtCore.QCoreApplication.translate
        
        # Ventana principal
        MainWindow.setWindowTitle(_translate("MainWindow", "Generador de Códigos QR"))
        
        # Título
        self.label_3.setText(_translate("MainWindow", "🔲 Generador de Códigos QR"))
        
        # URL
        self.label_url_info.setText(_translate("MainWindow", 
            "Ingresa la URL o texto que deseas codificar en el QR:"))
        self.lineEdit_url.setPlaceholderText(_translate("MainWindow", 
            "https://ejemplo.com"))
        
        # Botones de imagen
        self.pushButton_4.setText(_translate("MainWindow", "📁 Seleccionar Imagen"))
        self.pushButton.setText(_translate("MainWindow", "🗑️ Borrar Imagen"))
        
        # Sección Centro
        self.label_2.setText(_translate("MainWindow", "📍 Centro"))
        self.label_8.setText(_translate("MainWindow", "Forma del centro del QR"))
        self.label_9.setText(_translate("MainWindow", "Color del centro"))
        self.pushButton_1.setText(_translate("MainWindow", "🎨 Seleccionar Color"))
        
        # Sección Inner Eyes
        self.label_4.setText(_translate("MainWindow", "👁️ Inner Eyes"))
        self.label_10.setText(_translate("MainWindow", "Forma del Inner Eye"))
        self.label_11.setText(_translate("MainWindow", "Color del Inner Eye"))
        self.pushButton_2.setText(_translate("MainWindow", "🎨 Seleccionar Color"))
        
        # Sección Outer Eyes
        self.label_5.setText(_translate("MainWindow", "⭕ Outer Eyes"))
        self.label_12.setText(_translate("MainWindow", "Forma del Outer Eye"))
        self.label_13.setText(_translate("MainWindow", "Color del Outer Eye"))
        self.pushButton_3.setText(_translate("MainWindow", "🎨 Seleccionar Color"))
        
        # Menú
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionGuardar.setText(_translate("MainWindow", "💾 Guardar QR"))
        
        # Tooltips
        self.lineEdit_url.setToolTip(_translate("MainWindow", 
            "Ingresa la URL o texto para el código QR"))
        self.pushButton_4.setToolTip(_translate("MainWindow", 
            "Selecciona una imagen para el centro del código QR"))
        self.pushButton.setToolTip(_translate("MainWindow", 
            "Limpia la imagen seleccionada"))
        self.actionGuardar.setToolTip(_translate("MainWindow", 
            "Genera y guarda el código QR (Ctrl+S)"))


def main():
    """Función para probar la interfaz"""
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()