from BSplineFun import *


def RegistrationMain(movImg,fixImg,ImgToRegistMov,ImgToRegistFix,savePath,suffix):
    fixed_image = sitk.Cast(fixImg, sitk.sitkFloat32)
    moving_image = sitk.Cast(movImg, sitk.sitkFloat32)

    final_transform = BSplineFun(fixed_image, moving_image)

    resampled_image = sitk.Resample(ImgToRegistMov, ImgToRegistFix, final_transform, sitk.sitkLinear, 0.0,ImgToRegistMov.GetPixelID())

    sitk.WriteImage(resampled_image, savePath + "ResampledImage_"+suffix+".nii.gz")
    sitk.WriteTransform(final_transform, savePath + "transform_"+suffix+".tfm")

    return resampled_image,final_transform
