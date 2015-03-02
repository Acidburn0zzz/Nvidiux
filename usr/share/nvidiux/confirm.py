# -*- coding: utf-8 -*-

# Copyright 2014 Payet Guillaume
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class ConfirmWindow(QWidget):
	def __init__(self,text,parent=None):
		super (ConfirmWindow, self).__init__(parent)
		self.createWidgets(text)
	
	def createWidgets(self,text):
		
		self.resize(520, 510)
		self.setWindowTitle("Confirmation")
		self.labelInfo = QtGui.QLabel(text,self)
		self.labelInfo.move(60,15)
		self.labelInfo.setAlignment(QtCore.Qt.AlignCenter)
		font = QtGui.QFont()
		font.setPointSize(20)
		font.setBold(True)
		font.setWeight(75)
		self.labelInfo.setFont(font)
		font.setStyleStrategy(QtGui.QFont.PreferAntialias)
		self.checkBox = QCheckBox("Je comprend les risques et j'accepte les termes du contrat",self)
		self.checkBox.move(40,435)
		self.buttonConfirm = QPushButton("Confirmer",self);
		self.buttonConfirm.move(370,470)
		self.buttonConfirm.setEnabled(False)
		self.buttonCancel = QPushButton("Annuler",self);
		self.buttonCancel.move(50,470)
		self.texteula = QPlainTextEdit(self)
		self.texteula.move(0,150)
		self.texteula.resize(520,270)
		self.texteula.setPlainText(_fromUtf8("FR Version\nAttention cette pratique peut annuler la garantie du produit et reste à l'entière responsabilité de l'utilisateur du logiciel. Ni le concepteur du logiciel ni la communauté gnu ne pourra pas être tenu responsable de toutes mauvaises manipulations ayant entrainé un quelconque dégât direct ou en conséquence de l'utilisation de Nvidiux.\nNvidiux n'est en aucun cas affilié à Nvidia.\nEN Version\nThe author and community are not responsible of bad use and no liability for damages, direct or consequential, which may result from the use of Nvidiux.\nNvidiux is in no way affiliated to Nvidia."))
		self.texteula.setReadOnly(True)
		self.buttonCancel.connect(self.buttonCancel, SIGNAL("released()"),self.quitapp)
		self.buttonConfirm.connect(self.buttonConfirm, SIGNAL("released()"),self.confirm)
		self.checkBox.connect(self.checkBox, SIGNAL("clicked(bool)"),self.acceptEula)
		
	def quitapp(self):
		self.close()
		
	def acceptEula(self,response):
		self.buttonConfirm.setEnabled(response)
		
	def confirm(self):
		self.emit(SIGNAL("accept(PyQt_PyObject)"), "1")
		self.close()
		
	def retranslateUi(self):
		self.setWindowTitle(_translate("ConfirmWindow", "Confirmation", None))
		self.checkBox.setText(_translate("ConfirmWindow", "Je comprend les risques et j'accepte les termes du contrat", None))
		self.buttonConfirm.setText(_translate("ConfirmWindow", "Confirmer", None))
		self.buttonCancel.setText(_translate("ConfirmWindow", "Annuler", None))
