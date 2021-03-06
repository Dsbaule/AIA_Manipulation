import json
from zipfile import ZipFile

project_properties = '\
main=appinventor.ai_dsbaule.AllComponents.Screen1\n\
name=AllComponents\n\
assets=../assets\nn\
source=../src\n\
build=../build\n\
versioncode=1\n\
versionname=1.0\n\
useslocation=False\n\
aname=AllComponents\n\
sizing=Responsive\n\
showlistsasjson=True\n\
actionbar=False\n\
theme=Classic\n\
color.primary=&HFF3F51B5\n\
color.primary.dark=&HFF303F9F\n\
color.accent=&HFFFF4081\
'

screen1_scm = '\
#|\n\
$JSON\n\
{"authURL":["ai2.appinventor.mit.edu"],"YaVersion":"206","Source":"Form","Properties":{"$Name":"Screen1","$Type":"Form","$Version":"27","AppName":"AllComponents","Title":"Screen1","Uuid":"0","$Components":[{"$Name":"Organiza\u00e7\u00e3oHorizontal1","$Type":"HorizontalArrangement","$Version":"3","Uuid":"-152979349","$Components":[{"$Name":"Organiza\u00e7\u00e3oVertical1","$Type":"VerticalArrangement","$Version":"3","Uuid":"-1039475197","$Components":[{"$Name":"Bot\u00e3o1","$Type":"Button","$Version":"6","Text":"Texto para Bot\u00e3o1","Uuid":"1517351599"},{"$Name":"CaixaDeSele\u00e7\u00e3o1","$Type":"CheckBox","$Version":"2","Text":"Texto para CaixaDeSele\u00e7\u00e3o1","Uuid":"1900023744"},{"$Name":"Imagem1","$Type":"Image","$Version":"4","Uuid":"-2010102754"},{"$Name":"Legenda1","$Type":"Label","$Version":"5","Text":"Texto para Legenda1","Uuid":"-1816039873"},{"$Name":"EscolheLista1","$Type":"ListPicker","$Version":"9","Text":"Texto para EscolheLista1","Uuid":"-933708149"},{"$Name":"Deslizador1","$Type":"Slider","$Version":"2","Uuid":"96903718"},{"$Name":"ListaSuspensa1","$Type":"Spinner","$Version":"1","Uuid":"-1854827404"},{"$Name":"Switch1","$Type":"Switch","$Version":"1","Text":"Texto para Switch1","Uuid":"-594038957"},{"$Name":"CaixaDeTexto1","$Type":"TextBox","$Version":"6","Hint":"Dica para CaixaDeTexto1","Uuid":"-1361540991"}]}]}]}}\n\
|#\
'

savePath = "../Result/testFile.aia"

with ZipFile(savePath, 'x') as myzip:
	with myzip.open("youngandroidproject/project.properties", 'w') as project_properties_file:
		project_properties_file.write(bytes(project_properties, 'utf-8'))
	with myzip.open('src/appinventor/ai_dsbaule/AllComponents/Screen1.scm', 'w') as screen1_scm_file:
		screen1_scm_file.write(bytes(screen1_scm, 'utf-8'))
	with myzip.open('src/appinventor/ai_dsbaule/AllComponents/Screen1.bky', 'w') as screen1_bky_file:
		screen1_bky_file.write(bytes('', 'utf-8'))
