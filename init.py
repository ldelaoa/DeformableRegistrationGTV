from main import *


if __name__ == "__main__":
    #rootpath = "//Zkh/appdata/RTDicom/DAMEproject/LUNGSABR_data_2022/NIFTI_v0/0843413/"
    rootpath = "//home/umcg/Desktop/DeformableRegistration/NiiData/"
    image50 = sitk.ReadImage(rootpath + "0843413_T=50%,PR=44% - 54%,AR()=70 - 78_ct.nii.gz")
    #image_60 = sitk.ReadImage(rootpath + "0843413_T=60%,PR=55% - 64%,AR()=67 - 79_ct.nii.gz")
    image00 = sitk.ReadImage(rootpath + "0843413_T=0%,PR=96% - 5%,AR()=25 - 39_ct.nii")
    gtvimage = sitk.ReadImage(rootpath + "0843413_rtstruct_GTV.nii.gz")
    _ = main(image50,image00,gtvimage,rootpath)
