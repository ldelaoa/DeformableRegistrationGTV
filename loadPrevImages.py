import SimpleITK as sitk


def LoadPrevNorm(loadPath):
    image00_cropClamp = sitk.ReadImage(loadPath + "CT=00%_ImageCrop"+".nii.gz")
    image00_lungmask = sitk.ReadImage(loadPath + "CT=00%_LungMask"+".nii.gz")
    image50_cropClamp = sitk.ReadImage(loadPath + "CT=50%_ImageCrop"+".nii.gz")
    image50_lungmask = sitk.ReadImage(loadPath + "CT=50%_LungMask"+".nii.gz")
    image50_gtv = sitk.ReadImage(loadPath + "GTV=50%_ImageCrop.nii.gz")
    return image50_cropClamp, image50_lungmask,image50_gtv,image00_cropClamp, image00_lungmask


def LoadPrevRegist(loadPath,suffix):
    resampled_image = sitk.ReadImage(loadPath + "ResampledImage_"+suffix+".nii.gz")
    final_transform = sitk.ReadTransform(loadPath + "transform_" + suffix + ".tfm")
    return resampled_image,final_transform