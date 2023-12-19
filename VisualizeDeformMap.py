import matplotlib.pyplot as plt
from MakeDeformationMap import *
from matplotlib.collections import LineCollection


def plot_grid(x,y, ax, **kwargs):
    segs1 = np.stack((x, y), axis=2)
    segs2 = segs1.transpose(1, 0, 2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


def VisualizeDeformationMap(fixed_image, moving_image,gtv_image,final_transform_CT,savePath):
    array00 =sitk.GetArrayFromImage(fixed_image)
    array50=sitk.GetArrayFromImage(moving_image)
    arraygtv50=sitk.GetArrayFromImage(gtv_image)
    count = 0
    density_value = 8
    x = np.arange(0, 232,density_value)
    y = np.arange(0, 99,density_value)
    X, Y = np.meshgrid(x, y)

    for i in range(0,array00.shape[-2],20):
        if True:#np.sum(arraygtv50[:, i, :]) > 0:
            deformation_array,displacement_magnitude = DeformationMap(fixed_image,final_transform_CT,i)

            U = deformation_array[::density_value,::density_value,0]
            V = deformation_array[::density_value,::density_value,1]
            W = deformation_array[::density_value,::density_value,2]
            deformU = U.copy()
            deformW = W.copy()

            flipped_array50 = np.flipud(array50[:, i, :])
            flipped_array00 = np.flipud(array00[:, i, :])

            fig, axs = plt.subplots(1, 3, figsize=(12, 4))

            axs[0].imshow(flipped_array00, cmap='gray'), axs[0].axis("off")
            axs[0].imshow(flipped_array50, cmap='hot', alpha=0.5), axs[0].axis("off")
            axs[0].quiver(X, Y, -U, -W, scale=1, scale_units='xy', angles='xy', color='r')
            print(1, U.min(), U.max(), W.min(), W.max())
            axs[1].imshow(flipped_array00, cmap='gray'), axs[2].axis("off")
            axs[1].imshow(flipped_array50, cmap='hot', alpha=0.5), axs[2].axis("off")
            plot_grid(X + deformU, Y - deformW, ax=axs[1], color="C0")
            print(2, U.min(), U.max(), W.min(), W.max())
            axs[2].imshow(flipped_array00, cmap='gray'), axs[1].axis("off")
            axs[2].imshow(flipped_array50, cmap='hot', alpha=0.5), axs[1].axis("off")
            im = axs[2].imshow(displacement_magnitude, cmap='rainbow', alpha=0.8), axs[1].axis("off")
            cbar = plt.colorbar(im[0], ax=axs[2], shrink=0.4)
            print(3,U.min(), U.max(), W.min(), W.max())
            plt.tight_layout()
            #plt.show()
            plt.savefig(savePath+"DeformationMap_"+str(i)+".jpeg")
            count += 1
            if count > 20:
                break

    return 0