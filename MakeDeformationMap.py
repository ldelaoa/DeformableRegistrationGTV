import SimpleITK as sitk
import numpy as np


def DeformationMap(fixed_image,final_transform,slice_index):
    deformation_field = sitk.Image(fixed_image.GetSize(), sitk.sitkVectorFloat64)
    deformation_field.CopyInformation(fixed_image)
    absextreme=0
    for x in range(fixed_image.GetSize()[0]):
        for y in range(fixed_image.GetSize()[2]):
            index = (x, slice_index, y)
            fixed_point = fixed_image.TransformIndexToPhysicalPoint(index)
            moving_point = final_transform.TransformPoint(fixed_point)
            if (np.abs(np.array(moving_point) - np.array(fixed_point))> absextreme).any():
                absextreme = np.abs(np.array(moving_point) - np.array(fixed_point))
            deformation_vector = np.array(moving_point) - np.array(fixed_point)
            deformation_field.SetPixel(index, deformation_vector)

    deformation_field_slice = deformation_field[:, slice_index,:]
    deformation_array = sitk.GetArrayViewFromImage(deformation_field_slice)
    displacement_magnitude = np.sqrt(deformation_array[:, :, 0] ** 2 + deformation_array[:, :, 2] ** 2)
    return deformation_array,displacement_magnitude
