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
      - Appropriate wheel file for your Python version
      - md5sum.txt
      - requirements.txt (for appropriate Python version)

After training your yolo single class model or full 80 class model from a pt file:
* export via yolo in Onnx format
    - yolo export model='model_path' simplify=False imgsz=640 opset=11 batch=1
    - single_cls can be added if necessary
    - if simplify is not put as False, this will not work
    - Opset must be 11 to mimmick their model

* Next run the run_rknn_conversion.py file to modify your ONNX from the prior step
    - fill in your model name of the ONNX or anything else that seems like a variable
    - this removes post-processing, which can be done on your cpu
    - this adds reduce sums and outputs instead of the traditional Yolo single output

 *RkNN Conversion Timne
   - run the .py file and have your yml file in the same folder.
