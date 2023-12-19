import SimpleITK as sitk
from lungmask import LMInferer
import numpy as np


def cropLungMask(ct_image, rt_image=None, cropBool=True):
    kdiv = 64
    inferer = LMInferer()
    lungmask = inferer.apply(ct_image)
    ct_array = sitk.GetArrayFromImage(ct_image)
    mask_array = lungmask

    if not cropBool:
        return mask_array

    mask_bb = np.where(mask_array > 0)
    min_indices = [np.min(bb) for bb in mask_bb]
    max_indices = [np.max(bb) for bb in mask_bb]

    padding = kdiv - ((max_indices[0] - min_indices[0] + 1) % kdiv)
    padding = max(0, padding)  # Ensure padding is non-negative
    padding = 0
    min_indices = [max(0, idx - padding) for idx in min_indices]
    max_indices = [min(dim_size - 1, idx + padding) for idx, dim_size in zip(max_indices, ct_array.shape)]

    cropped_ct_array = ct_array[min_indices[0]:max_indices[0] + 1, min_indices[1]:max_indices[1] + 1,
                       min_indices[2]:max_indices[2] + 1]
    cropped_ct_image = sitk.GetImageFromArray(cropped_ct_array)
    cropped_ct_image.SetOrigin(ct_image.GetOrigin())
    cropped_ct_image.SetSpacing(ct_image.GetSpacing())

    cropped_mask_array = mask_array[min_indices[0]:max_indices[0] + 1, min_indices[1]:max_indices[1] + 1,
                         min_indices[2]:max_indices[2] + 1]
    cropped_mask_image = sitk.GetImageFromArray(cropped_mask_array)
    cropped_mask_image.SetOrigin(cropped_mask_image.GetOrigin())
    cropped_mask_image.SetSpacing(cropped_mask_image.GetSpacing())

    if rt_image is not None:
        rt_array = sitk.GetArrayFromImage(rt_image)
        cropped_rt_array = rt_array[min_indices[0]:max_indices[0] + 1, min_indices[1]:max_indices[1] + 1,
                           min_indices[2]:max_indices[2] + 1]
        cropped_AidditionalImage = sitk.GetImageFromArray(cropped_rt_array)
        cropped_AidditionalImage.SetOrigin(cropped_AidditionalImage.GetOrigin())
        cropped_AidditionalImage.SetSpacing(cropped_AidditionalImage.GetSpacing())

        return cropped_ct_image, cropped_mask_image, cropped_AidditionalImage

    else:
        return cropped_ct_image, cropped_mask_image
