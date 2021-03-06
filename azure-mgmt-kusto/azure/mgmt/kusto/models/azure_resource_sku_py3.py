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


class AzureResourceSku(Model):
    """AzureResourceSku.

    :param resource_type: Resource Namespace and Type.
    :type resource_type: str
    :param sku: The SKU details.
    :type sku: ~azure.mgmt.kusto.models.AzureSku
    :param capacity: The SKU capacity.
    :type capacity: ~azure.mgmt.kusto.models.AzureCapacity
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'AzureSku'},
        'capacity': {'key': 'capacity', 'type': 'AzureCapacity'},
    }

    def __init__(self, *, resource_type: str=None, sku=None, capacity=None, **kwargs) -> None:
        super(AzureResourceSku, self).__init__(**kwargs)
        self.resource_type = resource_type
        self.sku = sku
        self.capacity = capacity
