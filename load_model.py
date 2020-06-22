from numpy import loadtxt
from keras.models import load_model

# load model
model = load_model('face_detect.h5')
# summarize model.
model.summary()
