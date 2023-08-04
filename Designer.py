from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from project import Ui_MainWindow
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas



class Myapp(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(Myapp,self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.rig_butt.clicked.connect(self.Rig_Emission)  
        self.graph = QtWidgets.QHBoxLayout(self.frame_4)
        self.graph.setObjectName("graphs")
        self.figure=plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.graph.addWidget(self.canvas)
        self.valve_butt.clicked.connect(self.Valve_Emission)
        self.degasser_butt.clicked.connect(self.Degasser_Emission)
        self.desander_butt.clicked.connect(self.Desander_Emission)
        self.desilter_valve.clicked.connect(self.Desilter_Emission)
        self.desander_butt_2.clicked.connect(self.Pump_Emission)
        self.scope12_butt.clicked.connect(self.Scope1_2)
        self.scope3_butt.clicked.connect(self.Scope3)
        self.total_butt.clicked.connect(self.Total_Emissions)
        self.intensity_butt.clicked.connect(self.Carbon_Intensity)
        self.pushButton.clicked.connect(self.Graph)
        self.m_butt.clicked.connect(self.Mitigation)

    def Rig_Emission(self):
        Gal_oil= float(self.fuel.text())
        Years_O = float(self.year.text())
        RE =round((365* Gal_oil *9.98 *Years_O),3)
        self.listWidget_8.clear()
        self.listWidget_8.addItem(str(RE))
    
    def Valve_Emission(self):
        val= float(self.valves.text())
        Years_O = float(self.year.text())
        ve =round((365* val *0.3 *Years_O),3)
        self.listWidget_9.clear()
        self.listWidget_9.addItem(str(ve))
    
    def Degasser_Emission(self):
        elec = float(self.electricity.text())
        d_e = float(self.degasser.text())
        Years_O = float(self.year.text())
        D_e = round(((elec * 0.79 *365 *24 * Years_O) /d_e ),3)
        self.listWidget_4.clear()
        self.listWidget_4.addItem(str(D_e))

    def Desilter_Emission(self):
        elec = float(self.electricity.text())
        d_s = float(self.desilter.text())
        Years_O = float(self.year.text())
        Ds_e = round(((elec * 0.79 *365 *24 * Years_O) /d_s),3) 
        self.listWidget_5.clear()
        self.listWidget_5.addItem(str(Ds_e))

    def Desander_Emission(self):
        elec = float(self.electricity.text())
        d_sa = float(self.desander.text())
        Years_O = float(self.year.text())
        Da_e = round(((elec * 0.79 *365 *24 * Years_O) /d_sa),3) 
        self.listWidget_6.clear()
        self.listWidget_6.addItem(str(Da_e))
    
    def Pump_Emission(self):
        elec = float(self.electricity.text())
        p_e = float(self.desander_3.text())
        Years_O = float(self.year.text())
        P_e = round(((elec * 0.79 *365 *24 * Years_O) /p_e),3) 
        self.listWidget_7.clear()
        self.listWidget_7.addItem(str(P_e))
    
    def Scope1_2(self,row):
        P_E = self.listWidget_7.item(row)
        Pump_Emission= float(P_E.text())
        Desander = self.listWidget_6.item(row)
        Desander_Emission = float(Desander.text())
        Desilter = self.listWidget_5.item(row)
        Desilter_Emision = float(Desilter.text())
        Degasser = self.listWidget_4.item(row)
        Degasser_Emission = float(Degasser.text())
        S1_2 = round((Pump_Emission+Desander_Emission+Degasser_Emission+Desilter_Emision),3)
        self.listWidget.clear()
        self.listWidget.addItem(str(S1_2))


    def Scope3(self):
        bop = float(self.barrels.text())
        dor = float(self.ratio.text())
        S3 = round((dor*bop * 0.43),3)
        self.listWidget_2.clear()
        self.listWidget_2.addItem(str(S3))

    def Total_Emissions(self,row):
        scope1_2 = self.listWidget.item(row)
        S1_2 = float(scope1_2.text())
        scope3 = self.listWidget_2.item(row)
        S3 = float(scope3.text())
        T_emissions =S1_2+S3
        self.listWidget_3.clear()
        self.listWidget_3.addItem(str(T_emissions))

    def Carbon_Intensity(self,row):
        T_emissions = self.listWidget_3.item(row)
        T = float(T_emissions.text())
        depth = float(self.depth.text())
        n_wells = float(self.wells.text())
        CI = T*n_wells/depth
        self.listWidget_12.clear()
        self.listWidget_12.addItem(str(CI))
    
    def Graph(self,row):
        self.figure.clear()
        scope1_2 = self.listWidget.item(row)
        S1_2 = float(scope1_2.text())
        scope3 = self.listWidget_2.item(row)
        S3 = float(scope3.text())
        x=('Scope1 and 2','Scope 3')
        y = (S1_2,S3)
        plt.bar(x,y)
        plt.grid()
        self.completed =0
        while self.completed < 100:
            self.completed += 1
            self.progressBar.setValue(self.completed)
        self.canvas.draw()
    

    def Mitigation(self,row):
        self.tableWidget.clearContents()
        scope1_2 = self.listWidget.item(row)
        S1_2 = float(scope1_2.text())
        scope3 = self.listWidget_2.item(row)
        S3 = float(scope3.text())
        Years_O = float(self.year.text())
        M1 = 'To mitigate Scope 1 and 2 Emissions:\n 1. Use renewable sources of energy such as solar energy and hydrogen to fuel the rig \n 2. Use equipment with higher efficiencies to reduce their emissions\n 3. For components with potential gas leaks, seals should be use to reduce such emissions '
        M2 = f"Use {round(((S3/2300)*Years_O),3)} acres of land to plant trees to offset scope 3 emissions"

        if S1_2>0:
            for row in range(self.tableWidget.rowCount()):
                item = QtWidgets.QTableWidgetItem(M1)
                self.tableWidget.setItem(0,0,item)
        if S3>0:
            for row in range(self.tableWidget.rowCount()):
                item=QtWidgets.QTableWidgetItem(M2)
                self.tableWidget.setItem(0,1,item)




if __name__ == '__main__':
    app =QtWidgets.QApplication([])
    qt_app = Myapp()
    qt_app.show()
    app.exec_()







