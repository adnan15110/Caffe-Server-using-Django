import json


class test_class(object):
    """docstring for test_class"""
    def __init__(self):
        pass

    def functionOne(self, image_path):
        model_name = "test model"
        predicted_class = "class_label"
        image_loaction = "path to image"
        all_results = {'airplane': 0.66}

        return [model_name, predicted_class, image_loaction, all_results]
