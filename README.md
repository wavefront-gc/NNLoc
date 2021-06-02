# NNLoc
This is a CNN based model for microearthquake location by fusing waveform data and station location. 

The field data is from NewBerry EGS microearthquake monitoring project [some backgrounds of this project](https://www.sciencedirect.com/science/article/pii/S0375650515001108).

This project contains two main jupyter scripts, 'NewBerry_Raw2Input.ipynb' and 'DLmain_fieldData.ipynb'.

'NewBerry_Raw2Input.ipynb' is used to generate the input data and label data for training the CNN based model. 

In DLmain_fieldData.ipynb, we defined the model structure, training parameters, and a function to execute model training process.

If you want to conduct a fast test of out method, we supply the npz file 'input_labelNewberry0730.npz', which consists of Input1, Input2, and Label, so that you could skip the data generation script (NewBerry_Raw2Input.ipynb) and train the model directly. 