# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/prototipoCERTISSIMO.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout, QAbstractItemView, QMainWindow, QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

import random
import locale
import sys

from calculadorafinanceira.delegate.CalculadoraFinanciamentoDelegator import CalculadoraFinanciamentoDelegator
from calculadorafinanceira.model.SistemaFinanciamento import SistemaFinanciamento
from calculadorafinanceira.model.CalculadoraFinanciamentoTableModel import CalculadoraFinanciamentoTableModel
from calculadorafinanceira.view.CalculadoraFinanciamentoTableView import CalculadoraFinanciamentoTableView

class Ui_MainWindow(object):

    estiloInputInvalido = "border-style: solid; border-width: 2px 2px 2px 2px; border-color: red;"
    cabecalhosTabelaResultado = ["Parcela", "Valor da Prestação", "Amortização", "Juros", "Saldo Devedor"]

    def __init__(self):
        self.calculadoraFinanciamentoDelegator = CalculadoraFinanciamentoDelegator(self)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxInput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxInput.setTitle("")
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxInput)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditNumeroDeParcelas = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditNumeroDeParcelas.setObjectName("lineEditNumeroDeParcelas")
        self.lineEditNumeroDeParcelas.setAlignment(Qt.Qt.AlignCenter)
        self.gridLayout.addWidget(self.lineEditNumeroDeParcelas, 1, 2, 1, 1)
        self.lineEditTaxaDeJuros = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditTaxaDeJuros.setObjectName("lineEditTaxaDeJuros")
        self.lineEditTaxaDeJuros.setAlignment(Qt.Qt.AlignCenter)
        self.gridLayout.addWidget(self.lineEditTaxaDeJuros, 1, 1, 1, 1)
        self.pushButtonResetar = QtWidgets.QPushButton(self.groupBoxInput)
        self.pushButtonResetar.setObjectName("pushButtonResetar")
        self.gridLayout.addWidget(self.pushButtonResetar, 1, 5, 1, 1)
        self.labelNumeroDeParcelas = QtWidgets.QLabel(self.groupBoxInput)
        self.labelNumeroDeParcelas.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNumeroDeParcelas.setObjectName("labelNumeroDeParcelas")
        self.gridLayout.addWidget(self.labelNumeroDeParcelas, 0, 2, 1, 1)
        self.labelSistemaDeFinanciamento = QtWidgets.QLabel(self.groupBoxInput)
        self.labelSistemaDeFinanciamento.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSistemaDeFinanciamento.setObjectName("labelSistemaDeFinanciamento")
        self.gridLayout.addWidget(self.labelSistemaDeFinanciamento, 0, 3, 1, 2)
        self.checkBoxPrice = QtWidgets.QCheckBox(self.groupBoxInput)
        self.checkBoxPrice.setObjectName("checkBoxPrice")
        self.gridLayout.addWidget(self.checkBoxPrice, 1, 4, 1, 1)
        self.lineEditValorDoBem = QtWidgets.QLineEdit(self.groupBoxInput)
        self.lineEditValorDoBem.setObjectName("lineEditValorDoBem")
        self.lineEditValorDoBem.setAlignment(Qt.Qt.AlignCenter)
        self.gridLayout.addWidget(self.lineEditValorDoBem, 1, 0, 1, 1)
        self.checkBoxSac = QtWidgets.QCheckBox(self.groupBoxInput)
        self.checkBoxSac.setObjectName("checkBoxSac")
        self.gridLayout.addWidget(self.checkBoxSac, 1, 3, 1, 1)
        self.labelTaxaDeJuros = QtWidgets.QLabel(self.groupBoxInput)
        self.labelTaxaDeJuros.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTaxaDeJuros.setObjectName("labelTaxaDeJuros")
        self.gridLayout.addWidget(self.labelTaxaDeJuros, 0, 1, 1, 1)
        self.pushButtonSimular = QtWidgets.QPushButton(self.groupBoxInput)
        self.pushButtonSimular.setObjectName("pushButtonSimular")
        self.gridLayout.addWidget(self.pushButtonSimular, 0, 5, 1, 1)
        self.labelValorDoBem = QtWidgets.QLabel(self.groupBoxInput)
        self.labelValorDoBem.setAlignment(QtCore.Qt.AlignCenter)
        self.labelValorDoBem.setObjectName("labelValorDoBem")
        self.gridLayout.addWidget(self.labelValorDoBem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxInput)
        self.groupBoxesResultado = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxesResultado.sizePolicy().hasHeightForWidth())
        self.groupBoxesResultado.setSizePolicy(sizePolicy)
        self.groupBoxesResultado.setTitle("")
        self.groupBoxesResultado.setObjectName("groupBoxesResultado")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxesResultado)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.groupBoxesResultado)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.continueUiSetup()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelValorDoBem.setText(_translate("MainWindow", "Valor do bem (R$)"))
        self.labelTaxaDeJuros.setText(_translate("MainWindow", "Taxa de Juros (% a.m.)"))
        self.labelNumeroDeParcelas.setText(_translate("MainWindow", "Numero de Parcelas"))
        self.labelSistemaDeFinanciamento.setText(_translate("MainWindow", "Sistema de Financiamento"))
        self.pushButtonSimular.setText(_translate("MainWindow", "Simular"))
        self.checkBoxSac.setText(_translate("MainWindow", "SAC"))
        self.checkBoxPrice.setText(_translate("MainWindow", "PRICE"))
        self.pushButtonResetar.setText(_translate("MainWindow", "Resetar"))

    def continueUiSetup(self):
        self.pushButtonSimular.clicked.connect(self.onClickPushButtonSimular)
        self.pushButtonResetar.clicked.connect(self.onClickPushButtonResetar)

    def onClickPushButtonSimular(self):
        sistemasFinanciamento = []
        if self.checkBoxSac.isChecked():
            sistemasFinanciamento.append(SistemaFinanciamento.SAC)
        if self.checkBoxPrice.isChecked():
            sistemasFinanciamento.append(SistemaFinanciamento.PRICE)

        self.calculadoraFinanciamentoDelegator.calcula_financiamento(
            self.lineEditValorDoBem.text(), 
            self.lineEditTaxaDeJuros.text(), 
            self.lineEditNumeroDeParcelas.text(), 
            sistemasFinanciamento
            )

    def onClickPushButtonResetar(self):
        self.lineEditValorDoBem.clear()
        self.lineEditTaxaDeJuros.clear()
        self.lineEditNumeroDeParcelas.clear()
        self.checkBoxSac.setChecked(False)
        self.checkBoxPrice.setChecked(False)
        self.valoresValidosInput()
        self.limparGroupBoxResultado()

    def limparGroupBoxResultado(self):
        for i in reversed(range(self.horizontalLayout_2.count())):
            self.horizontalLayout_2.takeAt(i).widget().deleteLater()

    def valorInvalidoLineEditValorDoBem(self):
        self.lineEditValorDoBem.setStyleSheet(self.estiloInputInvalido)

    def valorInvalidoLineEditTaxaDeJuros(self):
        self.lineEditTaxaDeJuros.setStyleSheet(self.estiloInputInvalido)

    def valorInvalidoLineEditNumeroDeParcelas(self):
        self.lineEditNumeroDeParcelas.setStyleSheet(self.estiloInputInvalido)

    def sistemaDeFinanciamentoNaoEscolhido(self):
        self.checkBoxSac.setStyleSheet(self.estiloInputInvalido)
        self.checkBoxPrice.setStyleSheet(self.estiloInputInvalido)

    def valoresValidosInput(self):
        self.lineEditValorDoBem.setStyleSheet("")
        self.lineEditTaxaDeJuros.setStyleSheet("")
        self.lineEditNumeroDeParcelas.setStyleSheet("")
        self.checkBoxSac.setStyleSheet("")
        self.checkBoxPrice.setStyleSheet("")

    def renderizarTabelaResultado(self, resultadoCalculo):
        if (resultadoCalculo.getResultadoSac() is None):
            self.renderizarSistemaCalculoUnico(resultadoCalculo.getResultadoPrice())
        elif (resultadoCalculo.getResultadoPrice() is None):
            self.renderizarSistemaCalculoUnico(resultadoCalculo.getResultadoSac())
        else:
            self.renderizarSistemaCalculoMultiplo(resultadoCalculo)

    def renderizarSistemaCalculoUnico(self, linhas):
        self.tableViewResultado1 = CalculadoraFinanciamentoTableView(self.groupBoxesResultado)
        self.tableViewResultado1.setObjectName("tableViewResultado1")
        self.horizontalLayout_2.addWidget(self.tableViewResultado1)

        self.renderizarTabela(self.tableViewResultado1, linhas)

    def renderizarSistemaCalculoMultiplo(self, resultadoCalculo):
        self.renderizarSistemaCalculoUnico(resultadoCalculo.getResultadoSac())

        self.tableViewResultado2 = CalculadoraFinanciamentoTableView(self.groupBoxesResultado)
        self.tableViewResultado2.setObjectName("tableViewResultado2")
        self.horizontalLayout_2.addWidget(self.tableViewResultado2)

        self.renderizarTabela(self.tableViewResultado2, resultadoCalculo.getResultadoPrice())

    def renderizarTabela(self, tableView, linhas):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tableView.sizePolicy().hasHeightForWidth())
        tableView.setSizePolicy(sizePolicy)
        
        tableModel = CalculadoraFinanciamentoTableModel(linhas, self.cabecalhosTabelaResultado)
        tableView.setModel(tableModel)
        
        tableView.setSpan(len(linhas) - 1, 1, 1, 4)

        horizontalHeader = tableView.horizontalHeader()
        verticalHeader = tableView.verticalHeader()

        horizontalHeader.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        for i in range(1, 5):
            horizontalHeader.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        for i in range(0, len(linhas)):
            verticalHeader.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        tableView.show()

    def renderizarGraficoResultado(self, resultadoCalculo):
        if (resultadoCalculo.getResultadoSac() is None):
            self.renderizarGraficosSistemaCalculoUnico(resultadoCalculo.getResultadoPrice())
        elif (resultadoCalculo.getResultadoPrice() is None):
            self.renderizarGraficosSistemaCalculoUnico(resultadoCalculo.getResultadoSac())
        else:
            self.renderizarGraficosSistemaCalculoMultiplo(resultadoCalculo)

    def renderizarGraficosSistemaCalculoUnico(self, resultadoCalculo):
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        
        parcelas = [x[0] for x in resultadoCalculo[1:-1]]
        amortizacao = [x[2] for x in resultadoCalculo[1:-1]]
        juros = [x[3] for x in resultadoCalculo[1:-1]]
        prestacao = [x[1] for x in resultadoCalculo[1:-1]]

        plt.subplot(211)

        amortizacaoPlot = plt.plot(parcelas, amortizacao, label="Amortização")
        plt.setp(amortizacaoPlot, color="r")
        
        jurosPlot = plt.plot(parcelas, juros, label="Juros")
        plt.setp(jurosPlot, color="g")
        
        prestacaoPlot = plt.plot(parcelas, prestacao, label="Prestação")
        plt.setp(prestacaoPlot, color="b")
        
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)

        plt.subplot(212)

        objects = ["Sac"]
        y_pos = np.arange(len(objects))
        jurosTotal = sum(x[3] for x in resultadoCalculo[1:-1])

        plt.barh(y_pos, jurosTotal, align="center", alpha=0.5)
        plt.yticks(y_pos, objects)
        plt.xlabel("Juros Pago")

        self.horizontalLayout_2.addWidget(self.canvas)

        self.canvas.show()

    def renderizarGraficosSistemaCalculoMultiplo(self, resultadoCalculo):
        fig, axs = plt.subplots(2, 2, figsize=(20,10))

        self.canvas = FigureCanvas(fig)

        parcelasSac = [x[0] for x in resultadoCalculo.getResultadoSac()[1:-1]]
        amortizacaoSac = [x[2] for x in resultadoCalculo.getResultadoSac()[1:-1]]
        jurosSac = [x[3] for x in resultadoCalculo.getResultadoSac()[1:-1]]
        prestacaoSac = [x[1] for x in resultadoCalculo.getResultadoSac()[1:-1]]

        amortizacaoPlot = axs[0, 0].plot(parcelasSac, amortizacaoSac, label="Amortização")
        
        jurosPlot = axs[0, 0].plot(parcelasSac, jurosSac, label="Juros")
        
        prestacaoPlot = axs[0, 0].plot(parcelasSac, prestacaoSac, label="Prestação")

        axs[0, 0].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
        
        parcelasPrice = [x[0] for x in resultadoCalculo.getResultadoPrice()[1:-1]]
        amortizacaoPrice = [x[2] for x in resultadoCalculo.getResultadoPrice()[1:-1]]
        jurosPrice = [x[3] for x in resultadoCalculo.getResultadoPrice()[1:-1]]
        prestacaoPrice = [x[1] for x in resultadoCalculo.getResultadoPrice()[1:-1]]

        amortizacaoPlot = axs[0, 1].plot(parcelasPrice, amortizacaoPrice, label="Amortização")
        
        jurosPlot = axs[0, 1].plot(parcelasPrice, jurosPrice, label="Juros")
        
        prestacaoPlot = axs[0, 1].plot(parcelasPrice, prestacaoPrice, label="Prestação")
        
        axs[0, 1].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
        
        objects = ["Sac", "Price"]
        y_pos = np.arange(len(objects))
        jurosTotalSac = sum(x[3] for x in resultadoCalculo.getResultadoSac()[1:-1])
        jurosTotalPrice = sum(x[3] for x in resultadoCalculo.getResultadoPrice()[1:-1])

        axs[1, 0].barh(y_pos, [jurosTotalSac, jurosTotalPrice], align="center", alpha=0.5)
        axs[1, 0].set_yticks(y_pos)
        axs[1, 0].set_yticklabels(objects)
        axs[1, 0].set_xlabel("Juros Pago")

        axs[1, 1].plot(prestacaoSac, label="Sac")
        axs[1, 1].plot(prestacaoPrice, label="Price")
        axs[1, 1].set_xlabel("Evolução das parcelas")
        axs[1, 1].legend(loc='upper right', ncol=2, borderaxespad=0.)

        self.janelaGraficos = QtWidgets.QWidget()
        self.janelaGraficos.setWindowTitle("Graficos do resultado da simulação")
        self.janelaGraficos.resize(1000, 600)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.janelaGraficos.setLayout(layout)
        self.janelaGraficos.show()