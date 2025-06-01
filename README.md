### Working RKNN Yolo11N conversion process w quantization - Single Class Model
#Rockchip has an optimized model in their repository but does not clearly state how they optimized the model
This repository includes both examples for including how one can convert a model using the Rockchip process
#as well as a custom process for getting the equivalent onnx format with a semi-manual process
#I went ahead and made a script to replicate it to have a process for this

WSL - Windows Subsystem for Linux
### Requirements:
* Rockchip's Yolo11 branch: https://github.com/airockchip/ultralytics_yolo11/tree/v8.3.0
* Rockchip's RKNN Model Zoo: https://github.com/airockchip/rknn_model_zoo/tree/v2.3.0
* Rockchip's RKNN Toolkit2: https://github.com/airockchip/rknn-toolkit2/tree/v2.3.0
      - Appropriate wheel file for your python version
      - md5sum.txt
      - requirements.txt (for appropriate Python version)

After training your yolo single class model or full 80 class model from a pt file:
* Rockchip Yolo Export to ONNX
    - nano ~/newvenv/ultralytics_yolo11/ultralytics/cfg/default.yaml (edit model_path, imgsz ...)
    - cd ~/newvenv/ultralytics_yolo11
    - export PYTHONPATH=./
    - python ./ultralytics/engine/exporter.py (Onnx should be in the folder that the pt model was in)
 
* RKNN Export (RKNN Toolkit2)
    - python convert.py ~/newvenv/yolo11_rknn/model/yolo11n.onnx rk3566 i8



### Method #2  RKNN Optimization Process (For models converted to ONNX from the regular Ultralytics "Non-Rockchip" version)
* Post-processing can be removed with the Modify-Onnx.py file to mirror Rockchips modifications
    - This may or may not need different interference
    - simplify in the regular Ultralytics library or Ultralytics Yolo11 has to be put to False
    - Opset must be set to 11
    - single_cls can be True or False

* Next run the run_rknn_conversion.py file to modify your ONNX from the prior step
    - fill in your model name of the ONNX or anything else that seems like a variable
    - this removes post-processing, which can be done on your cpu
    - this adds reduce sums and outputs instead of the traditional Yolo single output

 *RkNN Conversion
   - run the .py file and have your yml file in the same folder.
