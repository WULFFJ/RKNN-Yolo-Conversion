#Quantized Int 8 Conversion from ONNX to RKNN
import yaml
from rknn.api import RKNN

# Load the YAML config
with open('rknnconvert.yml', 'r') as file:
    config = yaml.safe_load(file)

# Extract relevant settings
model_config = config['models']
subgraphs = model_config['subgraphs']
configs = model_config['configs']

# Initialize RKNN
rknn = RKNN(verbose=True)

# Set RKNN config from YAML
rknn.config(
    mean_values=configs['mean_values'],
    std_values=configs['std_values'],
    target_platform=configs['target_platform'],
    quant_img_RGB2BGR=configs['quant_img_RGB2BGR'],
    quantized_dtype=configs['quantized_dtype'],
    quantized_algorithm=configs['quantized_algorithm'],
    quantized_method=configs['quantize_method'],
    optimization_level=configs['optimization_level'],
    single_core_mode=configs['single_core_mode']
)

# Load the ONNX model (from YAML path)
rknn.load_onnx(model=model_config['model_file_path'])

# Build with quantization and dataset (from YAML)
rknn.build(do_quantization=model_config['quantize'], dataset=model_config['dataset'])

# Export the RKNN model
rknn.export_rknn('/home/shitshow/rknnvenv/ultralytics_yolo11/runs/detect/train3/weights/round2/your.rknn')

# Release resources
rknn.release()
