# Copyright 2016 Google Inc. All Rights Reserved.
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

"""The targets command group for the gcloud debug command."""

from googlecloudsdk.calliope import base
from surface import debug


class Targets(base.Group):
  """Commands for interacting with Cloud Debugger debug targets.

  Commands to interact with debug targets. A debug target can be an App Engine
  module version or any other entity enabled for use with the cloud debugger.
  """

  detailed_help = {
      'EXAMPLES': """\
          To view all available debug targets, run:

              $ {command} list
       """
  }

  def Filter(self, context, args):
    """Initialize context for Cloud Debugger targets commands.

    Args:
      context: The current context.
      args: The argparse namespace that was specified on the CLI or API.

    Returns:
      The updated context.
    """
    debug.SetApiDefaults()
    return context
