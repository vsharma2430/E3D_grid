@ECHO ON
SETLOCAL
SET SourceDir=C:\Users\D097\source\repos\E3D_Grid\E3D_grid\dist\grid_ui_qt 
SET TargetDir=\\10.40.10.46\itstrl\RELEASE\TCCLIVE\TeklaModules\grid_ui_qt 
if not exist "%TargetDir%" mkdir "%TargetDir%"
ROBOCOPY "%SourceDir%" "%TargetDir%" *.* /PURGE /S /NP /R:5 /TS /FP