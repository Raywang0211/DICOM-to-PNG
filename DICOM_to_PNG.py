from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

def DICOM_to_PNG(address,save_address):
    print('all_data ',os.listdir(address))
    all_data_name=os.listdir(address)
    print(len(all_data_name))

    for i in range(len(all_data_name)):
        path=address+all_data_name[i]
        ds=dcmread(path)
        print(ds.pixel_array.shape)
        print('MAX',np.max(ds.pixel_array))
        print('MAX',np.min(ds.pixel_array))
        print(type(ds.pixel_array))
        ds_nor=((ds.pixel_array/np.max(ds.pixel_array))*255).astype('uint8')
        im=Image.fromarray(ds_nor,'L')
        save_name=save_address+all_data_name[i]+'.png'
        im.save(save_name)

if __name__ == '__main__':
    address='C:/Users/Raywang/PycharmProjects/20200717Rocket/raw/'
    save_address='C:/Users/Raywang/PycharmProjects/20200717Rocket/img/'
    DICOM_to_PNG(address,save_address)