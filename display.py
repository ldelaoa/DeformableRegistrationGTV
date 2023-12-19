import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt


def displayLoadImgs(alphaVal,image50_crop,image00_crop,image50_resampled_LC,imagegtv_resampled_LC,image50_resampled_LM,imagegtv_resampled_LM,image50_resampled_CT,imagegtv_resampled_CT,savePath):
    array50 = sitk.GetArrayFromImage(image50_crop)
    array00 = sitk.GetArrayFromImage(image00_crop)

    array50R_LM = sitk.GetArrayFromImage(image50_resampled_LM)
    array50R_CT = sitk.GetArrayFromImage(image50_resampled_CT)
    array50R_LC = sitk.GetArrayFromImage(image50_resampled_LC)

    arraygtvR_LM= sitk.GetArrayFromImage(imagegtv_resampled_LM)
    arraygtvR_CT = sitk.GetArrayFromImage(imagegtv_resampled_CT)
    arraygtvR_LC = sitk.GetArrayFromImage(imagegtv_resampled_LC)


    count = 0
    for i in range(0,array00.shape[-2],1):
        if np.sum(arraygtvR_LM[:, i, :]) > 0:
            plt.subplot(221), plt.imshow(array00[:, i, :], cmap='gray'), plt.axis("off")
            plt.imshow(array50[:, i, :], cmap='hot', alpha=alphaVal, ), plt.axis("off")
            plt.gca().invert_yaxis(), plt.title("Unregist")

            plt.subplot(222), plt.imshow(array00[:, i, :], cmap='gray'), plt.axis("off")
            plt.imshow(array50R_LM[:, i, :], cmap='hot', alpha=alphaVal, ), plt.axis("off")
            plt.gca().invert_yaxis(), plt.title("Regist LM")

            plt.subplot(223), plt.imshow(array00[:, i, :], cmap='gray'), plt.axis("off")
            plt.imshow(array50R_CT[:, i, :], cmap='hot', alpha=alphaVal, ), plt.axis("off")
            plt.gca().invert_yaxis(), plt.title("Regist CT")

            plt.subplot(224), plt.imshow(array00[:, i, :], cmap='gray'), plt.axis("off")
            plt.imshow(array50R_LC[:, i, :], cmap='hot', alpha=alphaVal, ), plt.axis("off")
            plt.gca().invert_yaxis(), plt.title("Regist LC")
            plt.tight_layout()

            #plt.show()
            plt.savefig(savePath + "BeforeAfterR_LC" + str(i) + ".jpeg")
            count += 1
            if count > 15:
                break

    return 0

