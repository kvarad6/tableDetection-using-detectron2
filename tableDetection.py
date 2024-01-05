import layoutparser as lp
import cv2
import numpy as np
import os
from pathlib import Path
import io

save_dir = Path('./imgs')
result_dir = Path('./resultImgs')

# Initializing model
model = lp.models.Detectron2LayoutModel(
    config_path='lp://TableBank/faster_rcnn_R_101_FPN_3x/config',  # In model catalog
    label_map={0: "Table"},  # In model`label_map`
    extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.5]  # Optional
)


color_map = {"Table": "green"}

for file in os.listdir(save_dir):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        file_name = os.path.join(save_dir, file)
        img = cv2.imread(file_name)
        image = img[..., ::-1]
        layout = model.detect(image)

        print(layout)

        result_image = lp.draw_box(
            image, layout, box_width=5, color_map=color_map)

        result_array = np.array(result_image)

        result_file_name = f"{result_dir}/result_{file_name[5:]}"
        cv2.imwrite(result_file_name, result_array[..., ::-1])
