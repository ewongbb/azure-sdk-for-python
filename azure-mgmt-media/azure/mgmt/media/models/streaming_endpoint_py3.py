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

from .tracked_resource_py3 import TrackedResource


class StreamingEndpoint(TrackedResource):
    """The StreamingEndpoint.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region of the resource.
    :type location: str
    :param description: The StreamingEndpoint description.
    :type description: str
    :param scale_units: Required. The number of scale units.
    :type scale_units: int
    :param availability_set_name: AvailabilitySet name
    :type availability_set_name: str
    :param access_control: The access control definition of the
     StreamingEndpoint.
    :type access_control:
     ~azure.mgmt.media.models.StreamingEndpointAccessControl
    :param max_cache_age: Max cache age
    :type max_cache_age: long
    :param custom_host_names: The custom host names of the StreamingEndpoint
    :type custom_host_names: list[str]
    :ivar host_name: The StreamingEndpoint host name.
    :vartype host_name: str
    :param cdn_enabled: The CDN enabled flag.
    :type cdn_enabled: bool
    :param cdn_provider: The CDN provider name.
    :type cdn_provider: str
    :param cdn_profile: The CDN profile name.
    :type cdn_profile: str
    :ivar provisioning_state: The provisioning state of the StreamingEndpoint.
    :vartype provisioning_state: str
    :ivar resource_state: The resource state of the StreamingEndpoint.
     Possible values include: 'Stopped', 'Starting', 'Running', 'Stopping',
     'Deleting', 'Scaling'
    :vartype resource_state: str or
     ~azure.mgmt.media.models.StreamingEndpointResourceState
    :param cross_site_access_policies: The StreamingEndpoint access policies.
    :type cross_site_access_policies:
     ~azure.mgmt.media.models.CrossSiteAccessPolicies
    :ivar free_trial_end_time: The free trial expiration time.
    :vartype free_trial_end_time: datetime
    :ivar created: The exact time the StreamingEndpoint was created.
    :vartype created: datetime
    :ivar last_modified: The exact time the StreamingEndpoint was last
     modified.
    :vartype last_modified: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'scale_units': {'required': True},
        'host_name': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'resource_state': {'readonly': True},
        'free_trial_end_time': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'scale_units': {'key': 'properties.scaleUnits', 'type': 'int'},
        'availability_set_name': {'key': 'properties.availabilitySetName', 'type': 'str'},
        'access_control': {'key': 'properties.accessControl', 'type': 'StreamingEndpointAccessControl'},
        'max_cache_age': {'key': 'properties.maxCacheAge', 'type': 'long'},
        'custom_host_names': {'key': 'properties.customHostNames', 'type': '[str]'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'cdn_enabled': {'key': 'properties.cdnEnabled', 'type': 'bool'},
        'cdn_provider': {'key': 'properties.cdnProvider', 'type': 'str'},
        'cdn_profile': {'key': 'properties.cdnProfile', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'StreamingEndpointResourceState'},
        'cross_site_access_policies': {'key': 'properties.crossSiteAccessPolicies', 'type': 'CrossSiteAccessPolicies'},
        'free_trial_end_time': {'key': 'properties.freeTrialEndTime', 'type': 'iso-8601'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'last_modified': {'key': 'properties.lastModified', 'type': 'iso-8601'},
    }

    def __init__(self, *, scale_units: int, tags=None, location: str=None, description: str=None, availability_set_name: str=None, access_control=None, max_cache_age: int=None, custom_host_names=None, cdn_enabled: bool=None, cdn_provider: str=None, cdn_profile: str=None, cross_site_access_policies=None, **kwargs) -> None:
        super(StreamingEndpoint, self).__init__(tags=tags, location=location, **kwargs)
        self.description = description
        self.scale_units = scale_units
        self.availability_set_name = availability_set_name
        self.access_control = access_control
        self.max_cache_age = max_cache_age
        self.custom_host_names = custom_host_names
        self.host_name = None
        self.cdn_enabled = cdn_enabled
        self.cdn_provider = cdn_provider
        self.cdn_profile = cdn_profile
        self.provisioning_state = None
        self.resource_state = None
        self.cross_site_access_policies = cross_site_access_policies
        self.free_trial_end_time = None
        self.created = None
        self.last_modified = None
