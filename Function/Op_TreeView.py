'''
树形控件的相关操作函数
'''
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
def prs():
    print('TODO: selection changed')

def TreeView_Init(self):
    # TREEVIEW


    pitem1 = QTreeWidgetItem(self.treeWidget, ['Layers'])
    if self.StyleOn:
        pitem1.setForeground(0, Qt.white)
    pitem1.setFlags(pitem1.flags() & ~Qt.ItemIsSelectable)
    # citem1 = QTreeWidgetItem(pitem1, ['Mountain'])
    # citem11 = QTreeWidgetItem(citem1, ['Mountain Symbol'])
    # citem11.setIcon(0, QIcon('./UI/icon1.png'))
    # citem2 = QTreeWidgetItem(pitem1, ['Street'])
    # citem22 = QTreeWidgetItem(citem2, ['Street Symbol'])
    # citem22.setIcon(0, QIcon('./UI/icon1.png'))
    # citem3 = QTreeWidgetItem(pitem1, ['Water'])
    # citem33 = QTreeWidgetItem(citem3, ['Water Symbol'])
    # citem33.setIcon(0, QIcon('./UI/icon1.png'))
    # citem4 = QTreeWidgetItem(pitem1, ['City'])
    # citem44 = QTreeWidgetItem(citem4, ['City Symbol'])
    #
    # citem44.setForeground(0,Qt.red)
    # citem44.setIcon(0, QIcon('./UI/icon1.png'))
    # citem1.setCheckState(0, Qt.Checked)
    # citem2.setCheckState(0, Qt.Checked)
    # citem3.setCheckState(0, Qt.Checked)
    # citem4.setCheckState(0, Qt.Checked)
    self.treeWidget.itemChanged.connect(prs)

    self.treeWidget.header().setVisible(False)
    self.treeWidget.expandAll()

def NewLayer(self):
    txtName=self.Winnewlayer.lineEdit.text()
    txtType=self.Winnewlayer.comboBox.currentText()
    item=self.treeWidget.findItems('Layers',Qt.MatchStartsWith)[0]
    NewL=QTreeWidgetItem(item, [txtName])
    if self.StyleOn:
        NewL.setForeground(0, Qt.white)
    if txtType=='点':
        NewLchild=QTreeWidgetItem(NewL,[txtType])
        NewLchild.setIcon(0, QIcon('./UI/images/Point_G.png'))
        if self.StyleOn:
            NewLchild.setForeground(0, Qt.white)
            NewLchild.setIcon(0, QIcon('./UI/images/Point.png'))
        NewL.setCheckState(0, Qt.Checked)
        NewLchild.setFlags(NewLchild.flags() & ~Qt.ItemIsSelectable)
    elif txtType=='线':
        NewLchild=QTreeWidgetItem(NewL,[txtType])
        NewLchild.setIcon(0, QIcon('./UI/images/Line_G.png'))
        if self.StyleOn:
            NewLchild.setForeground(0, Qt.white)
            NewLchild.setIcon(0, QIcon('./UI/images/Line.png'))
        NewL.setCheckState(0, Qt.Checked)
        NewLchild.setFlags(NewLchild.flags() & ~Qt.ItemIsSelectable)
    elif txtType=='面':
        NewLchild=QTreeWidgetItem(NewL,[txtType])
        NewLchild.setIcon(0, QIcon('./UI/images/Polygon_G.png'))
        if self.StyleOn:
            NewLchild.setForeground(0, Qt.white)
            NewLchild.setIcon(0, QIcon('./UI/images/Polygon.png'))
        NewL.setCheckState(0, Qt.Checked)
        NewLchild.setFlags(NewLchild.flags() & ~Qt.ItemIsSelectable)
    self.treeWidget.expandAll()

    self.Winnewlayer.close()