# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FaceAttributes(Model):
    """Face Attributes.

    :param age: Age in years
    :type age: float
    :param gender: Possible gender of the face. Possible values include:
     'male', 'female', 'genderless'
    :type gender: str or ~azure.cognitiveservices.vision.face.models.Gender
    :param smile: Smile intensity, a number between [0,1]
    :type smile: float
    :param facial_hair: Properties describing facial hair attributes.
    :type facial_hair: ~azure.cognitiveservices.vision.face.models.FacialHair
    :param glasses: Glasses type if any of the face. Possible values include:
     'noGlasses', 'readingGlasses', 'sunglasses', 'swimmingGoggles'
    :type glasses: str or
     ~azure.cognitiveservices.vision.face.models.GlassesType
    :param head_pose: Properties indicating head pose of the face.
    :type head_pose: ~azure.cognitiveservices.vision.face.models.HeadPose
    :param emotion: Properties describing facial emotion in form of confidence
     ranging from 0 to 1.
    :type emotion: ~azure.cognitiveservices.vision.face.models.Emotion
    :param hair: Properties describing hair attributes.
    :type hair: ~azure.cognitiveservices.vision.face.models.Hair
    :param makeup: Properties describing present makeups on a given face.
    :type makeup: ~azure.cognitiveservices.vision.face.models.Makeup
    :param occlusion: Properties describing occlusions on a given face.
    :type occlusion: ~azure.cognitiveservices.vision.face.models.Occlusion
    :param accessories: Properties describing any accessories on a given face.
    :type accessories:
     list[~azure.cognitiveservices.vision.face.models.Accessory]
    :param blur: Properties describing any presence of blur within the image.
    :type blur: ~azure.cognitiveservices.vision.face.models.Blur
    :param exposure: Properties describing exposure level of the image.
    :type exposure: ~azure.cognitiveservices.vision.face.models.Exposure
    :param noise: Properties describing noise level of the image.
    :type noise: ~azure.cognitiveservices.vision.face.models.Noise
    """

    _attribute_map = {
        'age': {'key': 'age', 'type': 'float'},
        'gender': {'key': 'gender', 'type': 'Gender'},
        'smile': {'key': 'smile', 'type': 'float'},
        'facial_hair': {'key': 'facialHair', 'type': 'FacialHair'},
        'glasses': {'key': 'glasses', 'type': 'GlassesType'},
        'head_pose': {'key': 'headPose', 'type': 'HeadPose'},
        'emotion': {'key': 'emotion', 'type': 'Emotion'},
        'hair': {'key': 'hair', 'type': 'Hair'},
        'makeup': {'key': 'makeup', 'type': 'Makeup'},
        'occlusion': {'key': 'occlusion', 'type': 'Occlusion'},
        'accessories': {'key': 'accessories', 'type': '[Accessory]'},
        'blur': {'key': 'blur', 'type': 'Blur'},
        'exposure': {'key': 'exposure', 'type': 'Exposure'},
        'noise': {'key': 'noise', 'type': 'Noise'},
    }

    def __init__(self, **kwargs):
        super(FaceAttributes, self).__init__(**kwargs)
        self.age = kwargs.get('age', None)
        self.gender = kwargs.get('gender', None)
        self.smile = kwargs.get('smile', None)
        self.facial_hair = kwargs.get('facial_hair', None)
        self.glasses = kwargs.get('glasses', None)
        self.head_pose = kwargs.get('head_pose', None)
        self.emotion = kwargs.get('emotion', None)
        self.hair = kwargs.get('hair', None)
        self.makeup = kwargs.get('makeup', None)
        self.occlusion = kwargs.get('occlusion', None)
        self.accessories = kwargs.get('accessories', None)
        self.blur = kwargs.get('blur', None)
        self.exposure = kwargs.get('exposure', None)
        self.noise = kwargs.get('noise', None)
