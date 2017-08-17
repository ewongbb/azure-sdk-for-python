# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class EventSubscriptionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`EventSubscription <azure.mgmt.eventgrid.models.EventSubscription>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EventSubscription]'}
    }

    def __init__(self, *args, **kwargs):

        super(EventSubscriptionPaged, self).__init__(*args, **kwargs)