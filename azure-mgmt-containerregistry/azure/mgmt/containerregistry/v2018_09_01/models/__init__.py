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

try:
    from .import_source_py3 import ImportSource
    from .import_image_parameters_py3 import ImportImageParameters
    from .registry_name_check_request_py3 import RegistryNameCheckRequest
    from .registry_name_status_py3 import RegistryNameStatus
    from .operation_display_definition_py3 import OperationDisplayDefinition
    from .operation_metric_specification_definition_py3 import OperationMetricSpecificationDefinition
    from .operation_service_specification_definition_py3 import OperationServiceSpecificationDefinition
    from .operation_definition_py3 import OperationDefinition
    from .sku_py3 import Sku
    from .status_py3 import Status
    from .storage_account_properties_py3 import StorageAccountProperties
    from .registry_py3 import Registry
    from .registry_update_parameters_py3 import RegistryUpdateParameters
    from .registry_password_py3 import RegistryPassword
    from .registry_list_credentials_result_py3 import RegistryListCredentialsResult
    from .regenerate_credential_parameters_py3 import RegenerateCredentialParameters
    from .registry_usage_py3 import RegistryUsage
    from .registry_usage_list_result_py3 import RegistryUsageListResult
    from .quarantine_policy_py3 import QuarantinePolicy
    from .trust_policy_py3 import TrustPolicy
    from .registry_policies_py3 import RegistryPolicies
    from .replication_py3 import Replication
    from .replication_update_parameters_py3 import ReplicationUpdateParameters
    from .webhook_py3 import Webhook
    from .webhook_create_parameters_py3 import WebhookCreateParameters
    from .webhook_update_parameters_py3 import WebhookUpdateParameters
    from .event_info_py3 import EventInfo
    from .callback_config_py3 import CallbackConfig
    from .target_py3 import Target
    from .request_py3 import Request
    from .actor_py3 import Actor
    from .source_py3 import Source
    from .event_content_py3 import EventContent
    from .event_request_message_py3 import EventRequestMessage
    from .event_response_message_py3 import EventResponseMessage
    from .event_py3 import Event
    from .resource_py3 import Resource
    from .run_request_py3 import RunRequest
    from .image_descriptor_py3 import ImageDescriptor
    from .image_update_trigger_py3 import ImageUpdateTrigger
    from .source_trigger_descriptor_py3 import SourceTriggerDescriptor
    from .platform_properties_py3 import PlatformProperties
    from .agent_properties_py3 import AgentProperties
    from .run_py3 import Run
    from .source_upload_definition_py3 import SourceUploadDefinition
    from .run_filter_py3 import RunFilter
    from .run_update_parameters_py3 import RunUpdateParameters
    from .run_get_log_result_py3 import RunGetLogResult
    from .base_image_dependency_py3 import BaseImageDependency
    from .task_step_properties_py3 import TaskStepProperties
    from .auth_info_py3 import AuthInfo
    from .source_properties_py3 import SourceProperties
    from .source_trigger_py3 import SourceTrigger
    from .base_image_trigger_py3 import BaseImageTrigger
    from .trigger_properties_py3 import TriggerProperties
    from .task_py3 import Task
    from .platform_update_parameters_py3 import PlatformUpdateParameters
    from .task_step_update_parameters_py3 import TaskStepUpdateParameters
    from .auth_info_update_parameters_py3 import AuthInfoUpdateParameters
    from .source_update_parameters_py3 import SourceUpdateParameters
    from .source_trigger_update_parameters_py3 import SourceTriggerUpdateParameters
    from .base_image_trigger_update_parameters_py3 import BaseImageTriggerUpdateParameters
    from .trigger_update_parameters_py3 import TriggerUpdateParameters
    from .task_update_parameters_py3 import TaskUpdateParameters
    from .proxy_resource_py3 import ProxyResource
    from .argument_py3 import Argument
    from .docker_build_request_py3 import DockerBuildRequest
    from .set_value_py3 import SetValue
    from .build_task_request_py3 import BuildTaskRequest
    from .task_run_request_py3 import TaskRunRequest
    from .quick_task_run_request_py3 import QuickTaskRunRequest
    from .docker_build_step_py3 import DockerBuildStep
    from .build_task_step_py3 import BuildTaskStep
    from .run_task_step_py3 import RunTaskStep
    from .docker_build_step_update_parameters_py3 import DockerBuildStepUpdateParameters
    from .build_task_step_update_parameters_py3 import BuildTaskStepUpdateParameters
    from .run_task_step_update_parameters_py3 import RunTaskStepUpdateParameters
except (SyntaxError, ImportError):
    from .import_source import ImportSource
    from .import_image_parameters import ImportImageParameters
    from .registry_name_check_request import RegistryNameCheckRequest
    from .registry_name_status import RegistryNameStatus
    from .operation_display_definition import OperationDisplayDefinition
    from .operation_metric_specification_definition import OperationMetricSpecificationDefinition
    from .operation_service_specification_definition import OperationServiceSpecificationDefinition
    from .operation_definition import OperationDefinition
    from .sku import Sku
    from .status import Status
    from .storage_account_properties import StorageAccountProperties
    from .registry import Registry
    from .registry_update_parameters import RegistryUpdateParameters
    from .registry_password import RegistryPassword
    from .registry_list_credentials_result import RegistryListCredentialsResult
    from .regenerate_credential_parameters import RegenerateCredentialParameters
    from .registry_usage import RegistryUsage
    from .registry_usage_list_result import RegistryUsageListResult
    from .quarantine_policy import QuarantinePolicy
    from .trust_policy import TrustPolicy
    from .registry_policies import RegistryPolicies
    from .replication import Replication
    from .replication_update_parameters import ReplicationUpdateParameters
    from .webhook import Webhook
    from .webhook_create_parameters import WebhookCreateParameters
    from .webhook_update_parameters import WebhookUpdateParameters
    from .event_info import EventInfo
    from .callback_config import CallbackConfig
    from .target import Target
    from .request import Request
    from .actor import Actor
    from .source import Source
    from .event_content import EventContent
    from .event_request_message import EventRequestMessage
    from .event_response_message import EventResponseMessage
    from .event import Event
    from .resource import Resource
    from .run_request import RunRequest
    from .image_descriptor import ImageDescriptor
    from .image_update_trigger import ImageUpdateTrigger
    from .source_trigger_descriptor import SourceTriggerDescriptor
    from .platform_properties import PlatformProperties
    from .agent_properties import AgentProperties
    from .run import Run
    from .source_upload_definition import SourceUploadDefinition
    from .run_filter import RunFilter
    from .run_update_parameters import RunUpdateParameters
    from .run_get_log_result import RunGetLogResult
    from .base_image_dependency import BaseImageDependency
    from .task_step_properties import TaskStepProperties
    from .auth_info import AuthInfo
    from .source_properties import SourceProperties
    from .source_trigger import SourceTrigger
    from .base_image_trigger import BaseImageTrigger
    from .trigger_properties import TriggerProperties
    from .task import Task
    from .platform_update_parameters import PlatformUpdateParameters
    from .task_step_update_parameters import TaskStepUpdateParameters
    from .auth_info_update_parameters import AuthInfoUpdateParameters
    from .source_update_parameters import SourceUpdateParameters
    from .source_trigger_update_parameters import SourceTriggerUpdateParameters
    from .base_image_trigger_update_parameters import BaseImageTriggerUpdateParameters
    from .trigger_update_parameters import TriggerUpdateParameters
    from .task_update_parameters import TaskUpdateParameters
    from .proxy_resource import ProxyResource
    from .argument import Argument
    from .docker_build_request import DockerBuildRequest
    from .set_value import SetValue
    from .build_task_request import BuildTaskRequest
    from .task_run_request import TaskRunRequest
    from .quick_task_run_request import QuickTaskRunRequest
    from .docker_build_step import DockerBuildStep
    from .build_task_step import BuildTaskStep
    from .run_task_step import RunTaskStep
    from .docker_build_step_update_parameters import DockerBuildStepUpdateParameters
    from .build_task_step_update_parameters import BuildTaskStepUpdateParameters
    from .run_task_step_update_parameters import RunTaskStepUpdateParameters
from .registry_paged import RegistryPaged
from .operation_definition_paged import OperationDefinitionPaged
from .replication_paged import ReplicationPaged
from .webhook_paged import WebhookPaged
from .event_paged import EventPaged
from .run_paged import RunPaged
from .task_paged import TaskPaged
from .container_registry_management_client_enums import (
    ImportMode,
    SkuName,
    SkuTier,
    ProvisioningState,
    PasswordName,
    RegistryUsageUnit,
    PolicyStatus,
    TrustPolicyType,
    WebhookStatus,
    WebhookAction,
    RunStatus,
    RunType,
    OS,
    Architecture,
    Variant,
    TaskStatus,
    BaseImageDependencyType,
    SourceControlType,
    TokenType,
    SourceTriggerEvent,
    TriggerStatus,
    BaseImageTriggerType,
)

__all__ = [
    'ImportSource',
    'ImportImageParameters',
    'RegistryNameCheckRequest',
    'RegistryNameStatus',
    'OperationDisplayDefinition',
    'OperationMetricSpecificationDefinition',
    'OperationServiceSpecificationDefinition',
    'OperationDefinition',
    'Sku',
    'Status',
    'StorageAccountProperties',
    'Registry',
    'RegistryUpdateParameters',
    'RegistryPassword',
    'RegistryListCredentialsResult',
    'RegenerateCredentialParameters',
    'RegistryUsage',
    'RegistryUsageListResult',
    'QuarantinePolicy',
    'TrustPolicy',
    'RegistryPolicies',
    'Replication',
    'ReplicationUpdateParameters',
    'Webhook',
    'WebhookCreateParameters',
    'WebhookUpdateParameters',
    'EventInfo',
    'CallbackConfig',
    'Target',
    'Request',
    'Actor',
    'Source',
    'EventContent',
    'EventRequestMessage',
    'EventResponseMessage',
    'Event',
    'Resource',
    'RunRequest',
    'ImageDescriptor',
    'ImageUpdateTrigger',
    'SourceTriggerDescriptor',
    'PlatformProperties',
    'AgentProperties',
    'Run',
    'SourceUploadDefinition',
    'RunFilter',
    'RunUpdateParameters',
    'RunGetLogResult',
    'BaseImageDependency',
    'TaskStepProperties',
    'AuthInfo',
    'SourceProperties',
    'SourceTrigger',
    'BaseImageTrigger',
    'TriggerProperties',
    'Task',
    'PlatformUpdateParameters',
    'TaskStepUpdateParameters',
    'AuthInfoUpdateParameters',
    'SourceUpdateParameters',
    'SourceTriggerUpdateParameters',
    'BaseImageTriggerUpdateParameters',
    'TriggerUpdateParameters',
    'TaskUpdateParameters',
    'ProxyResource',
    'Argument',
    'DockerBuildRequest',
    'SetValue',
    'BuildTaskRequest',
    'TaskRunRequest',
    'QuickTaskRunRequest',
    'DockerBuildStep',
    'BuildTaskStep',
    'RunTaskStep',
    'DockerBuildStepUpdateParameters',
    'BuildTaskStepUpdateParameters',
    'RunTaskStepUpdateParameters',
    'RegistryPaged',
    'OperationDefinitionPaged',
    'ReplicationPaged',
    'WebhookPaged',
    'EventPaged',
    'RunPaged',
    'TaskPaged',
    'ImportMode',
    'SkuName',
    'SkuTier',
    'ProvisioningState',
    'PasswordName',
    'RegistryUsageUnit',
    'PolicyStatus',
    'TrustPolicyType',
    'WebhookStatus',
    'WebhookAction',
    'RunStatus',
    'RunType',
    'OS',
    'Architecture',
    'Variant',
    'TaskStatus',
    'BaseImageDependencyType',
    'SourceControlType',
    'TokenType',
    'SourceTriggerEvent',
    'TriggerStatus',
    'BaseImageTriggerType',
]
