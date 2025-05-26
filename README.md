### Working RKNN Yolo11N conversion process w quantization - Single Class Model
#Rockchip has an optimized model in their repository but does not clearly state how they optimized the model
#I went ahead and made a script to replicate it to have a process for this

After training your yolo single class model from a pt file:
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
