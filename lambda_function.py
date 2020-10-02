import cv2
import numpy as np
import boto3


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    bucket_name = "layers-opencv-adil"
    file_obj = s3.get_object(Bucket="layers-opencv-adil", Key="obj_scene.jpeg")
    file_content = file_obj["Body"].read()

    np_array = np.fromstring(file_content, np.uint8)
    image_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("/tmp/gray_obj.jpg", gray)

    s3.put_object(Bucket="layers-opencv-adil", Key="grayscale.jpg", Body=open("/tmp/gray_obj.jpg", "rb").read())

    return "Thanks"
