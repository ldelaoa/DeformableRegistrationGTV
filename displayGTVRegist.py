import SimpleITK as sitk
import numpy as np
import matplotlib.pyplot as plt


def displayGTVRegist(CTimage00,gtvImage_resampled_CT,gtvImage_resampled_LM,gtvImage_resampled_LC,ctImage_50,gtvImage_50,savePath):
    arrayGtv_resampled_CT = sitk.GetArrayFromImage(gtvImage_resampled_CT)
    arrayGtv_resampled_CT[arrayGtv_resampled_CT>0]=1

    arrayGtv_resampled_LM = sitk.GetArrayFromImage(gtvImage_resampled_LM)
    arrayGtv_resampled_LM[arrayGtv_resampled_LM>0]=1

    arrayGtv_resampled_LC = sitk.GetArrayFromImage(gtvImage_resampled_LC)
    arrayGtv_resampled_LC[arrayGtv_resampled_LC > 0] = 1

    arraygtv_50 = sitk.GetArrayFromImage(gtvImage_50)
    arrayCT_50 = sitk.GetArrayFromImage(ctImage_50)
    arrayCT_00 = sitk.GetArrayFromImage(CTimage00)
    count = 0
    tumorSlide=arrayGtv_resampled_CT.shape[-2]
    for i in range(0,arrayGtv_resampled_CT.shape[-2],1):
        if np.sum(arrayGtv_resampled_CT[:, i, :]) > 0 or tumorSlide-3<=i:
            tumorSlide=i
            fig, axs = plt.subplots(1, 5, figsize=(12, 4))
            axs[0].imshow(arrayCT_50[20:80, i, 20:80], cmap='gray'), axs[0].axis("off")
            axs[0].contour(arraygtv_50[20:80, i, 20:80])
            plt.gca().invert_yaxis()
            axs[1].imshow(arrayCT_00[20:80, i, 20:80], cmap='gray'), axs[1].axis("off")
            axs[2].imshow(arrayCT_00[20:80, i,20:80], cmap='gray'), axs[2].axis("off")
            axs[2].contour(arrayGtv_resampled_CT[20:80, i, 20:80])
            plt.gca().invert_yaxis()
            axs[3].imshow(arrayCT_00[20:80, i, 20:80], cmap='gray'), axs[3].axis("off")
            axs[3].contour(arrayGtv_resampled_LM[20:80, i, 20:80])
            plt.gca().invert_yaxis()
            axs[4].imshow(arrayCT_00[20:80, i, 20:80], cmap='gray'), axs[4].axis("off")
            axs[4].contour(arrayGtv_resampled_LC[20:80, i, 20:80])
            plt.gca().invert_yaxis()
            plt.tight_layout()
            #plt.show()
            plt.savefig(savePath + "GTVRegist_LC" + str(i) + ".jpeg")
            plt.close()
            count += 1
            if count > 25:
                break
    return 0