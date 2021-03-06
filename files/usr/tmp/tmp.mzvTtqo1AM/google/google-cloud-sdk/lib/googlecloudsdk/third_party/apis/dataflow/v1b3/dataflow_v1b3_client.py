"""Generated client library for dataflow version v1b3."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.dataflow.v1b3 import dataflow_v1b3_messages as messages


class DataflowV1b3(base_api.BaseApiClient):
  """Generated client library for service dataflow version v1b3."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://dataflow.googleapis.com/'

  _PACKAGE = u'dataflow'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/userinfo.email']
  _VERSION = u'v1b3'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DataflowV1b3'
  _URL_VERSION = u'v1b3'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new dataflow handle."""
    url = url or self.BASE_URL
    super(DataflowV1b3, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_jobs_debug = self.ProjectsJobsDebugService(self)
    self.projects_jobs_messages = self.ProjectsJobsMessagesService(self)
    self.projects_jobs_workItems = self.ProjectsJobsWorkItemsService(self)
    self.projects_jobs = self.ProjectsJobsService(self)
    self.projects_templates = self.ProjectsTemplatesService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsJobsDebugService(base_api.BaseApiService):
    """Service class for the projects_jobs_debug resource."""

    _NAME = u'projects_jobs_debug'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsDebugService, self).__init__(client)
      self._upload_configs = {
          }

    def GetConfig(self, request, global_params=None):
      """Get encoded debug configuration for component. Not cacheable.

      Args:
        request: (DataflowProjectsJobsDebugGetConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetDebugConfigResponse) The response message.
      """
      config = self.GetMethodConfig('GetConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.debug.getConfig',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/debug/getConfig',
        request_field=u'getDebugConfigRequest',
        request_type_name=u'DataflowProjectsJobsDebugGetConfigRequest',
        response_type_name=u'GetDebugConfigResponse',
        supports_download=False,
    )

    def SendCapture(self, request, global_params=None):
      """Send encoded debug capture data for component.

      Args:
        request: (DataflowProjectsJobsDebugSendCaptureRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SendDebugCaptureResponse) The response message.
      """
      config = self.GetMethodConfig('SendCapture')
      return self._RunMethod(
          config, request, global_params=global_params)

    SendCapture.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.debug.sendCapture',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/debug/sendCapture',
        request_field=u'sendDebugCaptureRequest',
        request_type_name=u'DataflowProjectsJobsDebugSendCaptureRequest',
        response_type_name=u'SendDebugCaptureResponse',
        supports_download=False,
    )

  class ProjectsJobsMessagesService(base_api.BaseApiService):
    """Service class for the projects_jobs_messages resource."""

    _NAME = u'projects_jobs_messages'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsMessagesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Request the job status.

      Args:
        request: (DataflowProjectsJobsMessagesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobMessagesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.messages.list',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[u'endTime', u'minimumImportance', u'pageSize', u'pageToken', u'startTime'],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/messages',
        request_field='',
        request_type_name=u'DataflowProjectsJobsMessagesListRequest',
        response_type_name=u'ListJobMessagesResponse',
        supports_download=False,
    )

  class ProjectsJobsWorkItemsService(base_api.BaseApiService):
    """Service class for the projects_jobs_workItems resource."""

    _NAME = u'projects_jobs_workItems'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsWorkItemsService, self).__init__(client)
      self._upload_configs = {
          }

    def Lease(self, request, global_params=None):
      """Leases a dataflow WorkItem to run.

      Args:
        request: (DataflowProjectsJobsWorkItemsLeaseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LeaseWorkItemResponse) The response message.
      """
      config = self.GetMethodConfig('Lease')
      return self._RunMethod(
          config, request, global_params=global_params)

    Lease.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.workItems.lease',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/workItems:lease',
        request_field=u'leaseWorkItemRequest',
        request_type_name=u'DataflowProjectsJobsWorkItemsLeaseRequest',
        response_type_name=u'LeaseWorkItemResponse',
        supports_download=False,
    )

    def ReportStatus(self, request, global_params=None):
      """Reports the status of dataflow WorkItems leased by a worker.

      Args:
        request: (DataflowProjectsJobsWorkItemsReportStatusRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReportWorkItemStatusResponse) The response message.
      """
      config = self.GetMethodConfig('ReportStatus')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReportStatus.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.workItems.reportStatus',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/workItems:reportStatus',
        request_field=u'reportWorkItemStatusRequest',
        request_type_name=u'DataflowProjectsJobsWorkItemsReportStatusRequest',
        response_type_name=u'ReportWorkItemStatusResponse',
        supports_download=False,
    )

  class ProjectsJobsService(base_api.BaseApiService):
    """Service class for the projects_jobs resource."""

    _NAME = u'projects_jobs'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a dataflow job.

      Args:
        request: (DataflowProjectsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.create',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'replaceJobId', u'view'],
        relative_path=u'v1b3/projects/{projectId}/jobs',
        request_field=u'job',
        request_type_name=u'DataflowProjectsJobsCreateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the state of the specified dataflow job.

      Args:
        request: (DataflowProjectsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.get',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[u'view'],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}',
        request_field='',
        request_type_name=u'DataflowProjectsJobsGetRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def GetMetrics(self, request, global_params=None):
      """Request the job status.

      Args:
        request: (DataflowProjectsJobsGetMetricsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (JobMetrics) The response message.
      """
      config = self.GetMethodConfig('GetMetrics')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetMetrics.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.getMetrics',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[u'startTime'],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/metrics',
        request_field='',
        request_type_name=u'DataflowProjectsJobsGetMetricsRequest',
        response_type_name=u'JobMetrics',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """List the jobs of a project.

      Args:
        request: (DataflowProjectsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.list',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'filter', u'pageSize', u'pageToken', u'view'],
        relative_path=u'v1b3/projects/{projectId}/jobs',
        request_field='',
        request_type_name=u'DataflowProjectsJobsListRequest',
        response_type_name=u'ListJobsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates the state of an existing dataflow job.

      Args:
        request: (DataflowProjectsJobsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'dataflow.projects.jobs.update',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}',
        request_field=u'job',
        request_type_name=u'DataflowProjectsJobsUpdateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

  class ProjectsTemplatesService(base_api.BaseApiService):
    """Service class for the projects_templates resource."""

    _NAME = u'projects_templates'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsTemplatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a dataflow job from a template.

      Args:
        request: (DataflowProjectsTemplatesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.templates.create',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/templates',
        request_field=u'createJobFromTemplateRequest',
        request_type_name=u'DataflowProjectsTemplatesCreateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def WorkerMessages(self, request, global_params=None):
      """Send a worker_message to the service.

      Args:
        request: (DataflowProjectsWorkerMessagesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SendWorkerMessagesResponse) The response message.
      """
      config = self.GetMethodConfig('WorkerMessages')
      return self._RunMethod(
          config, request, global_params=global_params)

    WorkerMessages.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.workerMessages',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/WorkerMessages',
        request_field=u'sendWorkerMessagesRequest',
        request_type_name=u'DataflowProjectsWorkerMessagesRequest',
        response_type_name=u'SendWorkerMessagesResponse',
        supports_download=False,
    )
