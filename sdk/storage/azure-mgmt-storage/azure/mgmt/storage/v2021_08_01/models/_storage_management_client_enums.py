# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Required for storage accounts where kind = BlobStorage. The access tier used for billing."""

    HOT = "Hot"
    COOL = "Cool"


class AccountImmutabilityPolicyState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ImmutabilityPolicy state defines the mode of the policy. Disabled state disables the
    policy, Unlocked state allows increase and decrease of immutability retention time and also
    allows toggling allowProtectedAppendWrites property, Locked state only allows the increase of
    the immutability retention time. A policy can only be created in a Disabled or Unlocked state
    and can be toggled between the two states. Only a policy in an Unlocked state can transition to
    a Locked state which cannot be reverted.
    """

    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    DISABLED = "Disabled"


class AccountStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the status indicating whether the primary location of the storage account is available or
    unavailable.
    """

    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class ActiveDirectoryPropertiesAccountType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the Active Directory account type for Azure Storage."""

    USER = "User"
    COMPUTER = "Computer"


class AllowedCopyScope(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Restrict copy to and from Storage Accounts within an AAD tenant or with Private Links to the
    same VNet.
    """

    PRIVATE_LINK = "PrivateLink"
    AAD = "AAD"


class BlobInventoryPolicyName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """BlobInventoryPolicyName."""

    DEFAULT = "default"


class BlobRestoreProgressStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of blob restore progress. Possible values are: - InProgress: Indicates that blob
    restore is ongoing. - Complete: Indicates that blob restore has been completed successfully. -
    Failed: Indicates that blob restore is failed.
    """

    IN_PROGRESS = "InProgress"
    COMPLETE = "Complete"
    FAILED = "Failed"


class Bypass(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are
    any combination of Logging|Metrics|AzureServices (For example, "Logging, Metrics"), or None to
    bypass none of those traffics.
    """

    NONE = "None"
    LOGGING = "Logging"
    METRICS = "Metrics"
    AZURE_SERVICES = "AzureServices"


class CorsRuleAllowedMethodsItem(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """CorsRuleAllowedMethodsItem."""

    DELETE = "DELETE"
    GET = "GET"
    HEAD = "HEAD"
    MERGE = "MERGE"
    POST = "POST"
    OPTIONS = "OPTIONS"
    PUT = "PUT"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DefaultAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the default action of allow or deny when no other rules match."""

    ALLOW = "Allow"
    DENY = "Deny"


class DefaultSharePermission(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Default share permission for users using Kerberos authentication if RBAC role is not assigned."""

    NONE = "None"
    STORAGE_FILE_DATA_SMB_SHARE_READER = "StorageFileDataSmbShareReader"
    STORAGE_FILE_DATA_SMB_SHARE_CONTRIBUTOR = "StorageFileDataSmbShareContributor"
    STORAGE_FILE_DATA_SMB_SHARE_ELEVATED_CONTRIBUTOR = "StorageFileDataSmbShareElevatedContributor"


class DirectoryServiceOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the directory service used."""

    NONE = "None"
    AADDS = "AADDS"
    AD = "AD"


class EnabledProtocols(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authentication protocol that is used for the file share. Can only be specified when
    creating a share.
    """

    SMB = "SMB"
    NFS = "NFS"


class EncryptionScopeSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provider for the encryption scope. Possible values (case-insensitive):  Microsoft.Storage,
    Microsoft.KeyVault.
    """

    MICROSOFT_STORAGE = "Microsoft.Storage"
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"


class EncryptionScopeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the encryption scope. Possible values (case-insensitive):  Enabled, Disabled."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExpirationAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SAS expiration action. Can only be Log."""

    LOG = "Log"


class ExtendedLocationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of extendedLocation."""

    EDGE_ZONE = "EdgeZone"


class Format(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This is a required field, it specifies the format for the inventory files."""

    CSV = "Csv"
    PARQUET = "Parquet"


class GeoReplicationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the secondary location. Possible values are: - Live: Indicates that the secondary
    location is active and operational. - Bootstrap: Indicates initial synchronization from the
    primary location to the secondary location is in progress.This typically occurs when
    replication is first enabled. - Unavailable: Indicates that the secondary location is
    temporarily unavailable.
    """

    LIVE = "Live"
    BOOTSTRAP = "Bootstrap"
    UNAVAILABLE = "Unavailable"


class HttpProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol permitted for a request made with the account SAS."""

    HTTPS_HTTP = "https,http"
    HTTPS = "https"


class IdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class ImmutabilityPolicyState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ImmutabilityPolicy state of a blob container, possible values include: Locked and Unlocked."""

    LOCKED = "Locked"
    UNLOCKED = "Unlocked"


class ImmutabilityPolicyUpdateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ImmutabilityPolicy update type of a blob container, possible values include: put, lock and
    extend.
    """

    PUT = "put"
    LOCK = "lock"
    EXTEND = "extend"


class InventoryRuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The valid value is Inventory."""

    INVENTORY = "Inventory"


class KeyPermission(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Permissions for the key -- read-only or full permissions."""

    READ = "Read"
    FULL = "Full"


class KeySource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage,
    Microsoft.Keyvault.
    """

    MICROSOFT_STORAGE = "Microsoft.Storage"
    MICROSOFT_KEYVAULT = "Microsoft.Keyvault"


class KeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Encryption key type to be used for the encryption service. 'Account' key type implies that an
    account-scoped encryption key will be used. 'Service' key type implies that a default service
    key is used.
    """

    SERVICE = "Service"
    ACCOUNT = "Account"


class Kind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of storage account."""

    STORAGE = "Storage"
    STORAGE_V2 = "StorageV2"
    BLOB_STORAGE = "BlobStorage"
    FILE_STORAGE = "FileStorage"
    BLOCK_BLOB_STORAGE = "BlockBlobStorage"


class LargeFileSharesState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class LeaseContainerRequestAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the lease action. Can be one of the available actions."""

    ACQUIRE = "Acquire"
    RENEW = "Renew"
    CHANGE = "Change"
    RELEASE = "Release"
    BREAK_ENUM = "Break"


class LeaseDuration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether the lease on a container is of infinite or fixed duration, only when the
    container is leased.
    """

    INFINITE = "Infinite"
    FIXED = "Fixed"


class LeaseShareAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the lease action. Can be one of the available actions."""

    ACQUIRE = "Acquire"
    RENEW = "Renew"
    CHANGE = "Change"
    RELEASE = "Release"
    BREAK_ENUM = "Break"


class LeaseState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Lease state of the container."""

    AVAILABLE = "Available"
    LEASED = "Leased"
    EXPIRED = "Expired"
    BREAKING = "Breaking"
    BROKEN = "Broken"


class LeaseStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The lease status of the container."""

    LOCKED = "Locked"
    UNLOCKED = "Unlocked"


class ListContainersInclude(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ListContainersInclude."""

    DELETED = "deleted"


class ManagementPolicyName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ManagementPolicyName."""

    DEFAULT = "default"


class MigrationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This property denotes the container level immutability to object level immutability migration
    state.
    """

    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"


class MinimumTlsVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Set the minimum TLS version to be permitted on requests to storage. The default interpretation
    is TLS 1.0 for this property.
    """

    TLS1_0 = "TLS1_0"
    TLS1_1 = "TLS1_1"
    TLS1_2 = "TLS1_2"


class Name(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the policy. The valid value is AccessTimeTracking. This field is currently read only."""

    ACCESS_TIME_TRACKING = "AccessTimeTracking"


class ObjectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This is a required field. This field specifies the scope of the inventory created either at the
    blob or container level.
    """

    BLOB = "Blob"
    CONTAINER = "Container"


class Permissions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed permissions for the account SAS. Possible values include: Read (r), Write (w),
    Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p).
    """

    R = "r"
    D = "d"
    W = "w"
    L = "l"
    A = "a"
    C = "c"
    U = "u"
    P = "p"


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PrivateEndpointServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private endpoint connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the status of the storage account at the time the operation was called."""

    CREATING = "Creating"
    RESOLVING_DNS = "ResolvingDNS"
    SUCCEEDED = "Succeeded"


class PublicAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies whether data in the container may be accessed publicly and the level of access."""

    CONTAINER = "Container"
    BLOB = "Blob"
    NONE = "None"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allow or disallow public network access to Storage Account. Value is optional but if passed in,
    must be 'Enabled' or 'Disabled'.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class Reason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the reason that a storage account name could not be used. The Reason element is only
    returned if NameAvailable is false.
    """

    ACCOUNT_NAME_INVALID = "AccountNameInvalid"
    ALREADY_EXISTS = "AlreadyExists"


class ReasonCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason for the restriction. As of now this can be "QuotaId" or
    "NotAvailableForSubscription". Quota Id is set when the SKU has requiredQuotas parameter as the
    subscription does not belong to that quota. The "NotAvailableForSubscription" is related to
    capacity at DC.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"


class RootSquashType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The property is for NFS share only. The default is NoRootSquash."""

    NO_ROOT_SQUASH = "NoRootSquash"
    ROOT_SQUASH = "RootSquash"
    ALL_SQUASH = "AllSquash"


class RoutingChoice(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Routing Choice defines the kind of network routing opted by the user."""

    MICROSOFT_ROUTING = "MicrosoftRouting"
    INTERNET_ROUTING = "InternetRouting"


class RuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The valid value is Lifecycle."""

    LIFECYCLE = "Lifecycle"


class Schedule(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This is a required field. This field is used to schedule an inventory formation."""

    DAILY = "Daily"
    WEEKLY = "Weekly"


class Services(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed services accessible with the account SAS. Possible values include: Blob (b), Queue
    (q), Table (t), File (f).
    """

    B = "b"
    Q = "q"
    T = "t"
    F = "f"


class ShareAccessTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access tier for specific share. GpV2 account can choose between TransactionOptimized (default),
    Hot, and Cool. FileStorage account can choose Premium.
    """

    TRANSACTION_OPTIMIZED = "TransactionOptimized"
    HOT = "Hot"
    COOL = "Cool"
    PREMIUM = "Premium"


class SignedResource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed services accessible with the service SAS. Possible values include: Blob (b),
    Container (c), File (f), Share (s).
    """

    B = "b"
    C = "c"
    F = "f"
    S = "s"


class SignedResourceTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The signed resource types that are accessible with the account SAS. Service (s): Access to
    service-level APIs; Container (c): Access to container-level APIs; Object (o): Access to
    object-level APIs for blobs, queue messages, table entities, and files.
    """

    S = "s"
    C = "c"
    O = "o"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU name. Required for account creation; optional for update. Note that in older versions,
    SKU name was called accountType.
    """

    STANDARD_LRS = "Standard_LRS"
    STANDARD_GRS = "Standard_GRS"
    STANDARD_RAGRS = "Standard_RAGRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"
    PREMIUM_ZRS = "Premium_ZRS"
    STANDARD_GZRS = "Standard_GZRS"
    STANDARD_RAGZRS = "Standard_RAGZRS"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU tier. This is based on the SKU name."""

    STANDARD = "Standard"
    PREMIUM = "Premium"


class State(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the state of virtual network rule."""

    PROVISIONING = "Provisioning"
    DEPROVISIONING = "Deprovisioning"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    NETWORK_SOURCE_DELETED = "NetworkSourceDeleted"


class StorageAccountExpand(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """StorageAccountExpand."""

    GEO_REPLICATION_STATS = "geoReplicationStats"
    BLOB_RESTORE_STATUS = "blobRestoreStatus"


class UsageUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the unit of measurement."""

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    PERCENT = "Percent"
    COUNTS_PER_SECOND = "CountsPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
