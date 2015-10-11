import sys
import numpy as np
# need to change
# caffe_root = '/install_dir/caffe/'
caffe_root = '/home/akhan/caffe-cpu/caffe'
sys.path.insert(0, caffe_root + 'python')
import caffe
import caffe.proto.caffe_pb2


class classifier(object):
    """docstring for Classifier"""
    def __init__(self, deployment_model, caffe_model, img_mean):
        """
        constructor for  instantiating a caffe model.

        :param deployment_model: deployment.prototxt path
        :type deployment_model: str
        :param caffe_model: .caffe_model file path
        :type caffe_model: str
        :param img_mean: path to the  image_mean.npy file
        :type img_mean: str
        :return:
        """
        self.label_dict = {
            3: 'car_side',
            7: 'bonsai',
            6: 'watch',
            2: 'ketch',
            10: 'hawksbill',
            8: 'chandelier',
            4: 'Faces_easy',
            1: 'Faces',
            9: 'airplanes',
            5: 'Leopards',
            0: 'Motorbikes'}

        self.img_shape = (300, 200)
        # instruction to use gpu zero
        # caffe.set_device(0)
        # set caffe mode cpu or gpu. check model_solver.prototxt.
        caffe.set_mode_cpu()
        self.net = caffe.Net(deployment_model, caffe_model, caffe.TEST)
        # getshape of the input "data" layer
        self.transformer = caffe.io.Transformer({'data': self.net.blobs['data'].data.shape})
        # change to h*w*c to c*h*w
        self.transformer.set_transpose('data', (2, 0, 1))
        # mean pixel, set mean.npy
        self.transformer.set_mean('data', np.load(img_mean))

    def classify(self, img_path):
        """
        classify input image

        :param img_path: The path to input image.
        :type img_path: str
        :return: predicted label (string)
        """
        im = caffe.io.load_image(img_path)
        im = caffe.io.resize_image(im, self.img_shape)
        self.net.blobs['data'].data[0] = self.transformer.preprocess('data', im)
        out = self.net.forward()
        predicted_output = np.argmax(out['ip2'][0])
        return self.label_dict[predicted_output]

    def get_predicition_result(self, img_path):
        """
        compute the output vector in the last layer

        :param img_path: The path to input image.
        :type img_path: str
        :return: whole vector
        """
        im = caffe.io.load_image(img_path)
        im = caffe.io.resize_image(im, self.img_shape)
        self.net.blobs['data'].data[0] = self.transformer.preprocess('data', im)
        out = self.net.forward()
        output_vector = out['ip2'][0]
        predicted_output = np.argmax(output_vector)
        normalized_output = output_vector/float(np.max(output_vector))
        return [output_vector, normalized_output, self.label_dict[predicted_output]]


if __name__ == '__main__':
    pass
