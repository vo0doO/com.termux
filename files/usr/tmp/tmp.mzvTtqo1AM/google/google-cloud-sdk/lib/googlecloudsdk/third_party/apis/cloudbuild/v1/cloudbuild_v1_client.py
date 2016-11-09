"""Generated client library for cloudbuild version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudbuild.v1 import cloudbuild_v1_messages as messages


class CloudbuildV1(base_api.BaseApiClient):
  """Generated client library for service cloudbuild version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudbuild.googleapis.com/'

  _PACKAGE = u'cloudbuild'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudbuildV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudbuild handle."""
    url = url or self.BASE_URL
    super(CloudbuildV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.operations = self.OperationsService(self)
    self.projects_builds = self.ProjectsBuildsService(self)
    self.projects_triggers = self.ProjectsTriggersService(self)
    self.projects = self.ProjectsService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(CloudbuildV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudbuildOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'cloudbuild.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudbuildOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding below allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`.

      Args:
        request: (CloudbuildOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations',
        http_method=u'GET',
        method_id=u'cloudbuild.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudbuildOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsBuildsService(base_api.BaseApiService):
    """Service class for the projects_builds resource."""

    _NAME = u'projects_builds'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsBuildsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Cancels a requested build in progress.

      Args:
        request: (CloudbuildProjectsBuildsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Build) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudbuild.projects.builds.cancel',
        ordered_params=[u'projectId', u'id'],
        path_params=[u'id', u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/builds/{id}:cancel',
        request_field=u'cancelBuildRequest',
        request_type_name=u'CloudbuildProjectsBuildsCancelRequest',
        response_type_name=u'Build',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      """Starts a build with the specified configuration.

The long-running Operation returned by this method will include the ID of
the build, which can be passed to GetBuild to determine its status (e.g.,
success or failure).

      Args:
        request: (CloudbuildProjectsBuildsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudbuild.projects.builds.create',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/builds',
        request_field=u'build',
        request_type_name=u'CloudbuildProjectsBuildsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Returns information about a previously requested build.

The Build that is returned includes its status (e.g., success or failure,
or in-progress), and timing information.

      Args:
        request: (CloudbuildProjectsBuildsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Build) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudbuild.projects.builds.get',
        ordered_params=[u'projectId', u'id'],
        path_params=[u'id', u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/builds/{id}',
        request_field='',
        request_type_name=u'CloudbuildProjectsBuildsGetRequest',
        response_type_name=u'Build',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished
successfully or unsuccessfully.

      Args:
        request: (CloudbuildProjectsBuildsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBuildsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudbuild.projects.builds.list',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/projects/{projectId}/builds',
        request_field='',
        request_type_name=u'CloudbuildProjectsBuildsListRequest',
        response_type_name=u'ListBuildsResponse',
        supports_download=False,
    )

  class ProjectsTriggersService(base_api.BaseApiService):
    """Service class for the projects_triggers resource."""

    _NAME = u'projects_triggers'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsTriggersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a new BuildTrigger.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BuildTrigger) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudbuild.projects.triggers.create',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/triggers',
        request_field=u'buildTrigger',
        request_type_name=u'CloudbuildProjectsTriggersCreateRequest',
        response_type_name=u'BuildTrigger',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes an BuildTrigger by its project ID and trigger ID.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'cloudbuild.projects.triggers.delete',
        ordered_params=[u'projectId', u'triggerId'],
        path_params=[u'projectId', u'triggerId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/triggers/{triggerId}',
        request_field='',
        request_type_name=u'CloudbuildProjectsTriggersDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets information about a BuildTrigger.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BuildTrigger) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudbuild.projects.triggers.get',
        ordered_params=[u'projectId', u'triggerId'],
        path_params=[u'projectId', u'triggerId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/triggers/{triggerId}',
        request_field='',
        request_type_name=u'CloudbuildProjectsTriggersGetRequest',
        response_type_name=u'BuildTrigger',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists existing BuildTrigger.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBuildTriggersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudbuild.projects.triggers.list',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/triggers',
        request_field='',
        request_type_name=u'CloudbuildProjectsTriggersListRequest',
        response_type_name=u'ListBuildTriggersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates an BuildTrigger by its project ID and trigger ID.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BuildTrigger) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'cloudbuild.projects.triggers.patch',
        ordered_params=[u'projectId', u'triggerId'],
        path_params=[u'projectId', u'triggerId'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/triggers/{triggerId}',
        request_field=u'buildTrigger',
        request_type_name=u'CloudbuildProjectsTriggersPatchRequest',
        response_type_name=u'BuildTrigger',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }