
"""
Description: A script to automate generation of Daily Hydrological Forecast
             for Abra River Basin located in Northern Luzon Philippines.
            
AUTHOR: KAIZER MACNI

"""


#VARIABLES


rr_vigan = 0.0
rr_bantay = 0.0
rr_dolores = 0.0
rr_luba = 4.0
rr_lapaz = 0.0
rr_lagayan = 0.0
rr_danglas = 0.0

#rr_vigan = input("Vigan Rainfall: ")
#rr_bantay = input("Bantay Rainfall: ")
#rr_dolores = input("Dolores Rainfall: ")
#rr_luba = input("Luba Rainfall: ")
#rr_lapaz = input("LaPaz Rainfall: ")
#rr_lagayan = input("Lagayan Rainfall: ")
#rr_danglas = input("Danglas Rainfall: ")


#RISING
#RECEDING
#NSC

wl_bantay = "NSC"
wl_lapaz = "NSC"
wl_dolores = "NSC"

#wl_bantay = str(input("Bantay WL TREND: "))
#wl_lapaz = str(input("LaPaz WL TREND: "))
#wl_dolores = str(input("Dolores WL TREND: "))


#NORMAL
#ALERT
#ALARM
#CRITICAL
wl_bantay_stat = "NORMAL"
wl_lapaz_stat = "NORMAL"
wl_dolores_stat = "NORMAL"

#wl_bantay_stat = str(input("Bantay WL STATUS: "))
#wl_lapaz_stat = str(input("LaPaz WL STATUS: "))
#wl_dolores_stat = str(input("Dolores WL STATUS: "))

#BANTAY ALERT=6.5, ALARM=7.5, CRITICAL=9.4
#LAPAZ ALERT=39, ALARM=40, CRITICAL=42
#DOLORES ALERT=53, ALARM=54, CRITICAL=56



###########################################################

import os

from qgis.core import (
    QgsGeometry,
    QgsMapSettings,
    QgsPrintLayout,
    QgsMapSettings,
    QgsMapRendererParallelJob,
    QgsLayoutItemLabel,
    QgsLayoutItemLegend,
    QgsLayoutItemMap,
    QgsLayoutItemPolygon,
    QgsLayoutItemScaleBar,
    QgsLayoutExporter,
    QgsLayoutItem,
    QgsLayoutPoint,
    QgsLayoutSize,
    QgsUnitTypes,
    QgsProject,
    QgsFillSymbol,
    QgsAbstractValidityCheck,
    check,
)

from qgis.PyQt.QtGui import (
    QPolygonF,
    QColor,
)

from qgis.PyQt.QtCore import (
    QPointF,
    QRectF,
    QSize,
)

from datetime import date

today = date.today()
#today = "2024-10-03"

project = QgsProject.instance()
            
manager = project.layoutManager()
layouts_list = manager.printLayouts()




layout = QgsPrintLayout(project)
layout.initializeDefaults()

        
document = QDomDocument()

# read template content
template_file = open('C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\WL change monitoring\\WL_RR-X2.qpt')
template_content = template_file.read()
template_file.close()
document.setContent(template_content)


# load layout from template and add to Layout Manager
layout.loadFromTemplate(document, QgsReadWriteContext()) 
project.layoutManager().addLayout(layout)

#STATIC VARIABLES
n_rains = "C:/Users/User/Documents/KAI FILES/AbRBFFWC OBSERVER DIRECTORY/ABRA BASIN DIRECTORY/ABRA BASIN DIRECTORY/DAILY REPORT/DAILY_RR_GIS/rainicon/NORAIN.png"
l_rains = "C:/Users/User/Documents/KAI FILES/AbRBFFWC OBSERVER DIRECTORY/ABRA BASIN DIRECTORY/ABRA BASIN DIRECTORY/DAILY REPORT/DAILY_RR_GIS/rainicon/LGTRAINS.png"
m_rains = "C:/Users/User/Documents/KAI FILES/AbRBFFWC OBSERVER DIRECTORY/ABRA BASIN DIRECTORY/ABRA BASIN DIRECTORY/DAILY REPORT/DAILY_RR_GIS/rainicon/MODRAINS.png"
h_rains = "C:/Users/User/Documents/KAI FILES/AbRBFFWC OBSERVER DIRECTORY/ABRA BASIN DIRECTORY/ABRA BASIN DIRECTORY/DAILY REPORT/DAILY_RR_GIS/rainicon/HEAVYRAINS.png"

NORMAL = QgsFillSymbol.createSimple({'color': 'green'})
ALERT = QgsFillSymbol.createSimple({'color': 'yellow'})
ALARM = QgsFillSymbol.createSimple({'color': 'orange'})
CRITICAL = QgsFillSymbol.createSimple({'color': 'red'})



if rr_vigan == 0:
    vigan_rain = n_rains
elif rr_vigan < 61:
    vigan_rain = l_rains
elif 60 < rr_vigan < 181:
    vigan_rain = m_rains
elif rr_vigan > 180:
    vigan_rain = h_rains
    
if rr_bantay == 0:
    bantay_rain = n_rains
elif rr_bantay < 61:
    bantay_rain = l_rains
elif 60 < rr_bantay < 181:
    bantay_rain = m_rains
elif rr_bantay > 180:
    bantay_rain = h_rains
    
if rr_luba == 0:
    luba_rain = n_rains
elif rr_luba < 61:
    luba_rain = l_rains
elif 60 < rr_luba < 181:
    luba_rain = m_rains
elif rr_luba > 180:
    luba_rain = h_rains
    
if rr_dolores == 0:
    dolores_rain = n_rains
elif rr_dolores < 61:
    dolores_rain = l_rains
elif 60 < rr_dolores < 181:
    dolores_rain = m_rains
elif rr_dolores > 180:
    dolores_rain = h_rains
 
if rr_lapaz == 0:
    lapaz_rain = n_rains
elif rr_lapaz < 61:
    lapaz_rain = l_rains
elif 60 < rr_lapaz < 181:
    lapaz_rain = m_rains
elif rr_lapaz > 180:
    lapaz_rain = h_rains
    
if rr_lagayan == 0:
    lagayan_rain = n_rains
elif rr_lagayan < 61:
    lagayan_rain = l_rains
elif 60 < rr_lagayan < 181:
    lagayan_rain = m_rains
elif rr_lagayan > 180:
    lagayan_rain = h_rains
    
if rr_danglas == 0:
    danglas_rain = n_rains
elif rr_danglas < 61:
    danglas_rain = l_rains
elif 60 < rr_danglas < 181:
    danglas_rain = m_rains
elif rr_danglas > 180:
    danglas_rain = h_rains 
    
    


BANTAY_WL_STAT = wl_bantay + "_BANTAY"
DOLORES_WL_STAT = wl_dolores + "_DOLORES"
LAPAZ_WL_STAT = wl_lapaz + "_LAPAZ"


layout = QgsProject.instance().layoutManager().layoutByName("RG-WL_STAT-X2")

vigan_rr_img = layout.itemById("VIGAN RG")
vigan_rr_value = layout.itemById("VIGAN_RG_AMT")

vigan_rr_value.setText(str(rr_vigan))
vigan_rr_img.setPicturePath(vigan_rain)

luba_rr_img = layout.itemById("LUBA_RG")
luba_rr_value = layout.itemById("LUBA_RG_AMT")

luba_rr_value.setText(str(rr_luba))
luba_rr_img.setPicturePath(luba_rain)

dolores_rr_img = layout.itemById("DOLORES_RG")
dolores_rr_value = layout.itemById("DOLORES_RG_AMT")

dolores_rr_value.setText(str(rr_dolores))
dolores_rr_img.setPicturePath(dolores_rain)

bantay_rr_img = layout.itemById("BANTAY_RG")
bantay_rr_value = layout.itemById("BANTAY_RG_AMT")

bantay_rr_value.setText(str(rr_bantay))
bantay_rr_img.setPicturePath(bantay_rain)

lapaz_rr_img = layout.itemById("LAPAZ_RG")
lapaz_rr_value = layout.itemById("LAPAZ_RG_AMT")

lapaz_rr_value.setText(str(rr_lapaz))
lapaz_rr_img.setPicturePath(lapaz_rain)

lagayan_rr_img = layout.itemById("LAGAYAN_RG")
lagayan_rr_value = layout.itemById("LAGAYAN_RG_AMT")

lagayan_rr_value.setText(str(rr_lagayan))
lagayan_rr_img.setPicturePath(lagayan_rain)

danglas_rr_img = layout.itemById("DANGLAS_RG")
danglas_rr_value = layout.itemById("DANGLAS_RG_AMT")

danglas_rr_value.setText(str(rr_danglas))
danglas_rr_img.setPicturePath(danglas_rain)


#waterlevels
bantay_wl_img_status = layout.itemById(BANTAY_WL_STAT)
bantay_wl_img_status.setVisibility(1)

if wl_bantay_stat == "NORMAL":
    bantay_wl_img_status.setSymbol(NORMAL)
elif wl_bantay_stat == "ALERT":
    bantay_wl_img_status.setSymbol(ALERT)
elif wl_bantay_stat == "ALARM":
    bantay_wl_img_status.setSymbol(ALARM)
elif wl_bantay_stat == "CRITICAL":
    bantay_wl_img_status.setSymbol(CRITICAL)
else:
    bantay_wl_img_status.setSymbol(NORMAL)
    


lapaz_wl_img_status = layout.itemById(LAPAZ_WL_STAT)
lapaz_wl_img_status.setVisibility(1)

if wl_lapaz_stat == "NORMAL":
    lapaz_wl_img_status.setSymbol(NORMAL)
elif wl_lapaz_stat == "ALERT":
    lapaz_wl_img_status.setSymbol(ALERT)
elif wl_lapaz_stat == "ALARM":
    lapaz_wl_img_status.setSymbol(ALARM)
elif wl_lapaz_stat == "CRITICAL":
    lapaz_wl_img_status.setSymbol(CRITICAL)
else:
    lapaz_wl_img_status.setSymbol(NORMAL)

dolores_wl_img_status = layout.itemById(DOLORES_WL_STAT)
dolores_wl_img_status.setVisibility(1)

if wl_dolores_stat == "NORMAL":
    dolores_wl_img_status.setSymbol(NORMAL)
elif wl_dolores_stat == "ALERT":
    dolores_wl_img_status.setSymbol(ALERT)
elif wl_dolores_stat == "ALARM":
    dolores_wl_img_status.setSymbol(ALARM)
elif wl_dolores_stat == "CRITICAL":
    dolores_wl_img_status.setSymbol(CRITICAL)
else:
    dolores_wl_img_status.setSymbol(NORMAL)


#base_path = os.path.join()
svg_path = os.path.join("C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\OUTPUTS\\WL-CHANGE\\svg\\", str(today) + "-abra_data.svg")
png_path = os.path.join("C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\OUTPUTS\\WL-CHANGE\\", str(today) + "-abra_data.png")

exporter = QgsLayoutExporter(layout)
exporter.exportToSvg(svg_path, QgsLayoutExporter.SvgExportSettings())
exporter.exportToImage(png_path, QgsLayoutExporter.ImageExportSettings())
print("done")

##########################  HF TEMPLATE
layoutHF = QgsPrintLayout(project)
layoutHF.initializeDefaults()

documentHF = QDomDocument()

# read template content
template_fileHF = open('C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\WL change monitoring\\HF-X2.qpt')
template_content = template_fileHF.read()
template_fileHF.close()
documentHF.setContent(template_content)


# load layout from template and add to Layout Manager
layoutHF.loadFromTemplate(documentHF, QgsReadWriteContext()) 
project.layoutManager().addLayout(layoutHF)


layoutHF = QgsProject.instance().layoutManager().layoutByName("HFORECAST HMD MAIN X2")
station_status_img = layoutHF.itemById("RG_WL_STATUS")

folder_path = "C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\OUTPUTS\\WL-CHANGE\\svg\\"
filename = str(today) + "-abra_data.svg"

station_status_img.setPicturePath(folder_path + filename)
#station_status_img.refreshPicture()

print("done")

#########################################################
