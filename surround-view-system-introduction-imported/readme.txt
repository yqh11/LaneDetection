solve problem: PyLint not recognizing cv2 members
1. C:\Users\James\AppData\Roaming\Python\Python38\Scripts\pylint.exe --generate-rcfile > .pylintrc
2. At the beginning of the generated .pylintrc file you will see

# A comma-separated list of package or module names from where C extensions may
# be loaded. Extensions are loading into the active Python interpreter and may
# run arbitrary code.
extension-pkg-whitelist=
Add cv2 so you end up with

# A comma-separated list of package or module names from where C extensions may
# be loaded. Extensions are loading into the active Python interpreter and may
# run arbitrary code.
extension-pkg-whitelist=cv2
Save the file. The lint errors should disappear.


calibrate_camera.py：用于相机内参标定。
show_undistorted_cameras.py：用于显示校正后的画面和查看设备号与相机对应关系。
paramsettings.py：用于设置投影区域的各参数。
get_projection_maps.py：用于手动标定获取到地面的投影矩阵。
stitch_images.py：用于显示静态的鸟瞰图拼接效果。
surroundview.py：用于在实车上运行的最终版本。


http://pywonderland.com/surround-view-system-introduction/

