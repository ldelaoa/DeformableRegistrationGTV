from dice_fun import *
from NormalizeImg import *
from display import *
from RegistrationMain import *
from loadPrevImages import *
from VisualizeDeformMap import *
from displayGTVRegist import *
from GetContourFromMasks import *


def main(image_50,image_00,gtv_image,savePath):
    usePrevNorm = True
    usePrevRegist = True
    if usePrevNorm:
        #LOAD PREVIOUS NORM
        image50_cropClamp, image50_lungmask,gtv_crop,image00_cropClamp, image00_lungmask = LoadPrevNorm(savePath)
    else:
        #NORMALIZE
        image50_cropClamp, image50_lungmask, gtv_crop = NormalizeImages(image_50,gtv_image,savePath)
        image00_cropClamp, image00_lungmask, _ =NormalizeImages(image_00,savePath=savePath)

    image50_LungContour = create_contour_image(image50_lungmask)
    image00_LungContour = create_contour_image(image00_lungmask)
    gtv50_LungContour = create_contour_image(gtv_crop)

    if usePrevRegist:
        resampled_image_LM,final_transform_LM =LoadPrevRegist(savePath, suffix="LM")
        resampled_image_CT, final_transform_CT = LoadPrevRegist(savePath, suffix="CT")
        resampled_image_LC, final_transform_LC = LoadPrevRegist(savePath, suffix="LC")
    else:
        #REGIST
        resampled_image_LC, final_transform_LC = RegistrationMain(image50_LungContour, image00_LungContour,image50_cropClamp, image00_cropClamp, savePath, "LC")
        resampled_image_LM,final_transform_LM = RegistrationMain(image50_lungmask, image00_lungmask, image50_cropClamp,image00_cropClamp,savePath,"LM")
        resampled_image_CT, final_transform_CT = RegistrationMain(image50_cropClamp, image00_cropClamp, image50_cropClamp,image00_cropClamp,savePath,"CT")

    resampled_GTV_LM = sitk.Resample(gtv_crop, image00_lungmask, final_transform_LM, sitk.sitkNearestNeighbor, 0.0,gtv_crop.GetPixelID())
    resampled_GTV_CT = sitk.Resample(gtv_crop, image00_lungmask, final_transform_CT, sitk.sitkNearestNeighbor, 0.0,gtv_crop.GetPixelID())
    resampled_GTV_LC = sitk.Resample(gtv50_LungContour, image00_LungContour, final_transform_LC, sitk.sitkNearestNeighbor, 0.0,gtv50_LungContour.GetPixelID())

    #DISPLAY Before Regist
    #alphaVal = .5
    #displayLoadImgs(alphaVal,image50_cropClamp,image00_cropClamp,resampled_image_LC,resampled_GTV_LC,resampled_image_LM, resampled_GTV_LM,resampled_image_CT, resampled_GTV_CT,savePath)

    #_ = displayGTVRegist(image00_cropClamp, resampled_GTV_LC, resampled_GTV_LM,resampled_GTV_LC, image50_cropClamp, gtv_crop,savePath)

    #METRICS
    #metric_LM = Metrics(resampled_image_LM, fixedImage=image00_lungmask)
    #metric_CT = Metrics(resampled_image_CT, fixedImage=image00_lungmask)
    #metric_LC = Metrics(resampled_image_LC, fixedImage=image00_lungmask)
    #print("Metric LM",metric_LM,"CT",metric_CT,"LC",metric_LC)

    #DISPLACEMENT MAP
    #VisualizeDeformationMap(image00_cropClamp, resampled_image_CT, gtv_crop,final_transform_CT,savePath)

    return 0