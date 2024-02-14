import os
import random
import shutil

from nnunetv2.dataset_conversion.generate_dataset_json import generate_dataset_json
from nnunetv2.paths import nnUNet_raw


def split_images_and_labels(images_tr_path, images_ts_path, labels_tr_path):
    image_filenames = [filename for filename in os.listdir(images_tr_path) if filename.endswith("_0000.png")]

    # 20% of the data will be moved to imagesTs
    num_images_to_move = int(0.2 * len(image_filenames))
    images_to_move = random.sample(image_filenames, num_images_to_move)

    # Move selected images from imagesTr to imagesTs and remove corresponding labels from labelsTr
    for image_filename in images_to_move:
        label_filename = image_filename.replace("_0000.png", ".png")

        src_image = os.path.join(images_tr_path, image_filename)
        dst_image = os.path.join(images_ts_path, image_filename)
        shutil.move(src_image, dst_image)

        src_label = os.path.join(labels_tr_path, label_filename)
        os.remove(src_label)

def move_rename_training_images(folder_path, new_folder_path):
    for count, filename in enumerate(os.listdir(folder_path)):

        original_src = os.path.join(folder_path, filename)

        new_filename = f"SEGK_{str(count).zfill(3)}_0000.png"
        new_dst = os.path.join(new_folder_path, new_filename)

        shutil.copyfile(original_src, new_dst)

def move_rename_labels(folder_path, new_folder_path):
    for count, filename in enumerate(os.listdir(folder_path)):
 
        original_src = os.path.join(folder_path, filename)

        new_filename = f"SEGK_{str(count).zfill(3)}.png"
        new_dst = os.path.join(new_folder_path, new_filename)

        shutil.copyfile(original_src, new_dst)


if __name__ == "__main__":
    import argparse

    dataset_name = 'Dataset001_Kidney'

    # imagestr = join(nnUNet_raw, dataset_name, 'imagesTr')
    # imagests = join(nnUNet_raw, dataset_name, 'imagesTs')
    # labelstr = join(nnUNet_raw, dataset_name, 'labelsTr')
    # labelsts = join(nnUNet_raw, dataset_name, 'labelsTs')
    # maybe_mkdir_p(imagestr)
    # maybe_mkdir_p(imagests)
    # maybe_mkdir_p(labelstr)
    # maybe_mkdir_p(labelsts)
        
    # images_tr_path = "C:/Users/Maha/Desktop/research/code/nnUNetFrame/dataset/nnUnet_raw/Dataset501_Kidney/imagesTr"
    # images_ts_path = "C:/Users/Maha/Desktop/research/code/nnUNetFrame/dataset/nnUnet_raw/Dataset501_Kidney/imagesTs"
    # labels_tr_path = "C:/Users/Maha/Desktop/research/code/nnUNetFrame/dataset/nnUnet_raw/Dataset501_Kidney/labelsTr"

    # training_data_path = "C:/Users/Maha/Desktop/research/data/kidneyUS_images_14_june_2022/kidneyUS_images_14_june_2022"
    # labels_data_path = "C:/Users/Maha/Desktop/research/data/kidneyUS/labels/reviewed_masks_2/regions"

    # split_images_and_labels(images_tr_path, images_ts_path, labels_tr_path)

    # move_rename_training_images(training_data_path, images_tr_path)

    # move_rename_labels(labels_data_path, labels_tr_path)

    num_train = 428

    output_folder = "C:/Users/Maha/Desktop/research/code/nnUNetFrame/dataset/nnUNet_raw/Dataset501_Kidney"
    output_folder1 = "C:/Users/Maha/Desktop/research/code/nnUNetFrame/nnUNet/nnunetv2/nnUNet_raw"

    generate_dataset_json(
        output_folder=output_folder,
        channel_names={
                0: "ultrasound",
            },
        labels={
            "background": 0,
            "Central Echo Complex": 1,
            "Medulla": 2,
            "Cortex": 3,
        },
        file_ending=".png",
        num_training_cases=num_train,
        dataset_name=dataset_name,
        overwrite_image_reader_writer= "PILIO",
    )
