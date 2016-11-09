# Copyright 2013 Google Inc. All Rights Reserved.
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

"""Command to list properties."""

from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.config import completers
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.configurations import named_configs


class BadConfigListInvocation(exceptions.Error):
  """Exception for incorrect invocations of `config list`."""


class List(base.ListCommand):
  """View Cloud SDK properties.

  Lists all properties in your active configuration. These include the
  account used to authorize access to the Cloud Platform, the current Cloud
  Platform project, and the default Compute Engine region and zone, if set. See
  `gcloud topic configurations` for more information.

  ## AVAILABLE PROPERTIES

  {properties}

  ## EXAMPLES

  To list the project property in the core section, run:

    $ {command} project

  To list the zone property in the compute section, run:

    $ {command} compute/zone

  To list all the properties, run:

    $ {command} --all

  Note you cannot specify both --all and a property name.
  """

  detailed_help = {'properties': properties.VALUES.GetHelpString()}

  @staticmethod
  def Args(parser):
    """Adds args for this command."""
    parser.add_argument(
        '--all', action='store_true',
        help='List all set and unset properties that match the arguments.')
    property_arg = parser.add_argument(
        'property',
        metavar='SECTION/PROPERTY',
        nargs='?',
        help='The property to be listed. Note that SECTION/ is optional while '
        'referring to properties in the core section.')
    property_arg.completer = completers.PropertiesCompleter
    base.PAGE_SIZE_FLAG.RemoveFromParser(parser)
    base.URI_FLAG.RemoveFromParser(parser)

  def _GetPropertiesToDisplay(self, args):
    """List available regular properties."""
    section, prop = properties.ParsePropertyString(args.property)

    if prop:
      return {section: {
          prop: properties.VALUES.Section(section).Property(prop).Get()}}
    if section:
      return {section: properties.VALUES.Section(section).AllValues(
          list_unset=args.all)}
    return properties.VALUES.AllValues(list_unset=args.all)

  def Run(self, args):
    if args.all and args.property:
      raise BadConfigListInvocation('`gcloud config list` cannot take both '
                                    'a property name and the `--all` flag.')

    config_name = named_configs.ConfigurationStore.ActiveConfig().name
    log.status.write('Your active configuration is: [{0}]\n\n'.format(
        config_name))
    return self._GetPropertiesToDisplay(args)

  def Format(self, _):
    return 'config'
