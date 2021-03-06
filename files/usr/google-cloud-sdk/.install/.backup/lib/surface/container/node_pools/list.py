# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""List node pools command."""
from apitools.base.py import exceptions as apitools_exceptions

from googlecloudsdk.api_lib.container import util
from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import properties

DETAILED_HELP = {
    'DESCRIPTION': """\
        *{command}* displays all node pools in the Google Container Engine
        cluster.
        """,
    'EXAMPLES': """\
        To list all node pools in the cluster "sample-cluster" in table form,
        run:

          $ {command} --cluster=sample-cluster
     """,
}


class List(base.ListCommand):
  """List existing node pools for a cluster."""

  @staticmethod
  def Args(parser):
    """Register flags for this command.

    Args:
      parser: An argparse.ArgumentParser-like object. It is mocked out in order
          to capture some information, but behaves like an ArgumentParser.
    """
    parser.add_argument(
        '--cluster',
        help='The name of the cluster.',
        action=actions.StoreProperty(properties.VALUES.container.cluster))

  def Run(self, args):
    """This is what gets called when the user runs this command.

    Args:
      args: an argparse namespace. All the arguments that were provided to this
        command invocation.

    Returns:
      Some value that we want to have printed later.
    """
    adapter = self.context['api_adapter']

    project = properties.VALUES.core.project.Get(required=True)
    cluster = properties.VALUES.container.cluster.Get(required=True)
    zone = properties.VALUES.compute.zone.Get(required=True)

    try:
      res = adapter.ListNodePools(project, zone, cluster)
      return res.nodePools
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(error, util.HTTP_ERROR_FORMAT)

  def Collection(self):
    return 'container.projects.zones.clusters.nodePools'


List.detailed_help = DETAILED_HELP
