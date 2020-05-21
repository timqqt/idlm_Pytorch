"""
The parameter file storing the parameters for INN Model
"""

# Define which data set you are using
DATA_SET = 'meta_material'
# DATA_SET = 'gaussian_mixture'
# DATA_SET = 'sine_wave'
# DATA_SET = 'naval_propulsion'
# DATA_SET = 'robotic_arm'
# DATA_SET = 'ballistics'
TEST_RATIO = 0.05

# Architectural Params
DIM_Z = 8
DIM_X = 8
DIM_Y = 300
COUPLE_LAYER_NUM = 15
DIM_SPEC = None
# The below definitions are useless now since we are using the package
SUBNET_LINEAR = []                                          # Linear units for Subnet FC layer
#LINEAR_SE = []                      # Linear units for spectra encoder
#CONV_OUT_CHANNEL_SE = []
#CONV_KERNEL_SIZE_SE = []
#CONV_STRIDE_SE = []
LINEAR_SE = [150, 500, 500, 500, 500, DIM_Y]                                              # Linear units for spectra encoder
CONV_OUT_CHANNEL_SE = [4, 4, 4]
CONV_KERNEL_SIZE_SE = [5, 5, 8]
CONV_STRIDE_SE = [1, 1, 2]

# Loss ratio
LAMBDA_MSE = 3.             # The Loss factor of the MSE loss (reconstruction loss)
LAMBDA_Z = 300.             # The Loss factor of the latent dimension (converging to normal distribution)
LAMBDA_REV = 400.           # The Loss factor of the reverse transformation (let x converge to input distribution)
ZEROS_NOISE_SCALE = 5e-2          # The noise scale to add to
Y_NOISE_SCALE = 1e-1


# Optimization params
OPTIM = "Adam"
REG_SCALE = 2e-5
BATCH_SIZE = 1024
EVAL_BATCH_SIZE = 4096
EVAL_STEP = 20
GRAD_CLAMP = 15
TRAIN_STEP = 500
VERB_STEP = 20
LEARN_RATE = 1e-3
# DECAY_STEP = 25000 # This is for step decay, however we are using dynamic decaying
LR_DECAY_RATE = 0.5
STOP_THRESHOLD = -float('inf')

# Data specific params
X_RANGE = [i for i in range(2, 10 )]
Y_RANGE = [i for i in range(10 , 2011 )]
FORCE_RUN = True
MODEL_NAME  = None
# MODEL_NAME  = 'dim_z_2 + wBN + 100 + lr1e-3 + reg5e-3'
DATA_DIR = '/work/sr365/'      # For server usage
#DATA_DIR = '/home/omar/PycharmProjects/github/idlm_Pytorch-master/forward/'                # For Omar useage
# DATA_DIR = '../'                # For local useage
GEOBOUNDARY =[30, 52, 42, 52]
NORMALIZE_INPUT = True

# Running specific params
USE_CPU_ONLY = False
#EVAL_MODEL = "ballistics_Ben_version"
EVAL_MODEL = "ballistics_Jakob_version"
#EVAL_MODEL = "robotic_armcouple_layer_num6trail_0"
#EVAL_MODEL = "sine_wave"
#EVAL_MODEL = "models/meta_materials/meta_materialcouple_layer_num13trail_1"
#EVAL_MODEL = "retrain_time_evalballistics_Jakob_version"
