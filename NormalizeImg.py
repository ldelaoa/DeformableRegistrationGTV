from cropLungMask import *


def NormalizeImages(image,gtv=None,savePath=None):
    if gtv is not None:
        image_crop, image_lungmask, gtv_crop = cropLungMask(image, gtv)
        print(sitk.GetArrayFromImage(image_lungmask).shape, sitk.GetArrayFromImage(image_crop).shape,sitk.GetArrayFromImage(gtv_crop).shape)
        image_cropClamp = sitk.Clamp(image_crop, lowerBound=-1024, upperBound=600)
        sitk.WriteImage(image_cropClamp, savePath + "CT=50%_ImageCrop.nii.gz")
        sitk.WriteImage(image_lungmask, savePath + "CT=50%_LungMask.nii.gz")
        sitk.WriteImage(gtv_crop, savePath + "GTV=50%_ImageCrop.nii.gz")

    else:
        gtv_crop = None
        image_crop, image_lungmask = cropLungMask(image)
        image_cropClamp = sitk.Clamp(image_crop, lowerBound=-1024, upperBound=600)
        sitk.WriteImage(image_cropClamp, savePath + "CT=00%_ImageCrop.nii.gz")
        sitk.WriteImage(image_lungmask, savePath + "CT=00%_LungMask.nii.gz")

    return image_cropClamp,image_lungmask,gtv_crop
