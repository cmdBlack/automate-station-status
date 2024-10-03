#VARIABLES

rr_vigan = 180
rr_bantay = 200
rr_dolores = 450
rr_luba = 1

#RISING
#RECEDING
#NSC

wl_bantay = "RECEDING"
wl_lapaz = "RECEDING"
wl_dolores = "RECEDING"

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
#today = "2024-10-02"

project = QgsProject.instance()
            
manager = project.layoutManager()
#layoutName = "RG-WL_STAT"
layouts_list = manager.printLayouts()




layout = QgsPrintLayout(project)
layout.initializeDefaults()

        
document = QDomDocument()

# read template content
template_file = open('C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\WL change monitoring\\WL_RR.qpt')
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


BANTAY_WL_STAT = wl_bantay + "_BANTAY"
DOLORES_WL_STAT = wl_dolores + "_DOLORES"
LAPAZ_WL_STAT = wl_lapaz + "_LAPAZ"


layout = QgsProject.instance().layoutManager().layoutByName("RG-WL_STAT")

vigan_rr_img = layout.itemById("VIGAN RG")
vigan_rr_value = layout.itemById("VIGAN_RG_AMT")

vigan_rr_value.setText(str(rr_vigan) + " mm")
vigan_rr_img.setPicturePath(vigan_rain)

luba_rr_img = layout.itemById("LUBA_RG")
luba_rr_value = layout.itemById("LUBA_RG_AMT")

luba_rr_value.setText(str(rr_luba) + " mm")
luba_rr_img.setPicturePath(luba_rain)

dolores_rr_img = layout.itemById("DOLORES_RG")
dolores_rr_value = layout.itemById("DOLORES_RG_AMT")

dolores_rr_value.setText(str(rr_dolores) + " mm")
dolores_rr_img.setPicturePath(dolores_rain)

bantay_rr_img = layout.itemById("BANTAY_RG")
bantay_rr_value = layout.itemById("BANTAY_RG_AMT")

bantay_rr_value.setText(str(rr_bantay) + " mm")
bantay_rr_img.setPicturePath(bantay_rain)


#waterlevels
bantay_wl_img_status = layout.itemById(BANTAY_WL_STAT)
bantay_wl_img_status.setVisibility(1)

lapaz_wl_img_status = layout.itemById(LAPAZ_WL_STAT)
lapaz_wl_img_status.setVisibility(1)

dolores_wl_img_status = layout.itemById(DOLORES_WL_STAT)
dolores_wl_img_status.setVisibility(1)




#base_path = os.path.join()
svg_path = os.path.join("C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\OUTPUTS\\WL-CHANGE\\", str(today) + "-abra_data.svg")
png_path = os.path.join("C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\OUTPUTS\\WL-CHANGE\\", str(today) + "-abra_data.png")

exporter = QgsLayoutExporter(layout)
exporter.exportToSvg(svg_path, QgsLayoutExporter.SvgExportSettings())
exporter.exportToImage(png_path, QgsLayoutExporter.ImageExportSettings())



##########################  HF TEMPLATE
layoutHF = QgsPrintLayout(project)
layoutHF.initializeDefaults()

documentHF = QDomDocument()

# read template content
template_file = open('C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\WL change monitoring\\HF.qpt')
template_content = template_file.read()
template_file.close()
documentHF.setContent(template_content)


# load layout from template and add to Layout Manager
layoutHF.loadFromTemplate(documentHF, QgsReadWriteContext()) 
project.layoutManager().addLayout(layoutHF)


layoutHF = QgsProject.instance().layoutManager().layoutByName("HFORECAST HMD MAIN")
station_status_img = layoutHF.itemById("RG_WL_STATUS")

folder_path = "C:\\Users\\User\\Documents\\KAI FILES\\AbRBFFWC OBSERVER DIRECTORY\\ABRA BASIN DIRECTORY\\ABRA BASIN DIRECTORY\\DAILY REPORT\\OUTPUTS\\WL-CHANGE\\"
filename = str(today) + "-abra_data.svg"

station_status_img.setPicturePath(folder_path + filename)

#########################################################
