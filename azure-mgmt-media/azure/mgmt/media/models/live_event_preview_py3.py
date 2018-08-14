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


class LiveEventPreview(Model):
    """The Live Event preview.

    :param endpoints: The endpoints for preview.
    :type endpoints: list[~azure.mgmt.media.models.LiveEventEndpoint]
    :param access_control: The access control for LiveEvent preview.
    :type access_control:
     ~azure.mgmt.media.models.LiveEventPreviewAccessControl
    :param preview_locator: The preview locator Guid.
    :type preview_locator: str
    :param streaming_policy_name: The name of streaming policy used for
     LiveEvent preview
    :type streaming_policy_name: str
    :param alternative_media_id: The alternative Media-Id associated with the
     preview
    :type alternative_media_id: str
    """

    _attribute_map = {
        'endpoints': {'key': 'endpoints', 'type': '[LiveEventEndpoint]'},
        'access_control': {'key': 'accessControl', 'type': 'LiveEventPreviewAccessControl'},
        'preview_locator': {'key': 'previewLocator', 'type': 'str'},
        'streaming_policy_name': {'key': 'streamingPolicyName', 'type': 'str'},
        'alternative_media_id': {'key': 'alternativeMediaId', 'type': 'str'},
    }

    def __init__(self, *, endpoints=None, access_control=None, preview_locator: str=None, streaming_policy_name: str=None, alternative_media_id: str=None, **kwargs) -> None:
        super(LiveEventPreview, self).__init__(**kwargs)
        self.endpoints = endpoints
        self.access_control = access_control
        self.preview_locator = preview_locator
        self.streaming_policy_name = streaming_policy_name
        self.alternative_media_id = alternative_media_id
