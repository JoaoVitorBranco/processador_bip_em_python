import os
import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QFont

class Mem_Interface(QMainWindow):
    memoria: dict

    def __init__(self, UI_string, memoria: dict):
        super().__init__()
        self.memoria = memoria

        uic.loadUi(f'src/GUI/{UI_string}.ui', self)
        self.setWindowIcon(QtGui.QIcon(self.resource_path('src/GUI/assets/icone.ico')))

        # region Formata a tabela

        self.num_linhas = self.tableWidget.rowCount()
        self.num_colunas = self.tableWidget.columnCount()
        self.tableWidget.setHorizontalHeaderLabels([hex(i)[-1].upper() for i in range(self.num_colunas)])
        self.tableWidget.setVerticalHeaderLabels(['0x' + hex(i).split('x')[1].upper().zfill(2) + 'X' for i in range(self.num_linhas)])
        
        self.preenche_tabela(memoria)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.itemChanged.connect(self.on_changed)

        #endregion

    # region Funções de formatação da UI

    def preenche_tabela(self, memoria):
        self.memoria = memoria
        for i in range(self.num_linhas):
            linha = '0x' + hex(i).split('x')[1].upper().zfill(2)
            for j in range(self.num_colunas):
                coluna = hex(j)[-1].upper()
                item = QtWidgets.QTableWidgetItem()
                font = QFont()
                font.setCapitalization(QFont.AllUppercase)
                item.setFont(font)
                item.setText(self.memoria.get(linha).get(coluna))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(i, j, item)

    # endregion


    # region Função de controle

    def resource_path(self,relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


    # endregion

    def on_changed(self, item):
        pass
