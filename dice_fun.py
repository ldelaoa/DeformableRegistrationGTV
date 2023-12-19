from cropLungMask import *


def dice_coefficient(image1, image2):
    intersection = np.sum(image1 & image2)
    union = np.sum(image1 | image2)

    dice = (2.0 * intersection) / (union + intersection)
    return dice


def Metrics(resampled_image,fixedImage):
    lungMask_resampled = cropLungMask(resampled_image, rt_image=None, cropBool=False)
    fixed_array = sitk.GetArrayFromImage(fixedImage)
    binary_fixed_array = (fixed_array > 0.5).astype(int)
    binary_moved_array = (lungMask_resampled > 0.5).astype(int)
    metric = dice_coefficient(binary_fixed_array, binary_moved_array)
    print("Dice between registrated Lungs:", metric)
    return metric
