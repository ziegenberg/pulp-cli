from typing import Any

import click

from pulpcore.cli.common.context import PluginRequirement, PulpContext, pass_pulp_context
from pulpcore.cli.common.generic import pulp_group
from pulpcore.cli.python.content import content
from pulpcore.cli.python.distribution import distribution
from pulpcore.cli.python.publication import publication
from pulpcore.cli.python.remote import remote
from pulpcore.cli.python.repository import repository


@pulp_group(name="python")
@pass_pulp_context
def python_group(pulp_ctx: PulpContext) -> None:
    pulp_ctx.needs_plugin(PluginRequirement("python", min="3.1"))


def mount(main: click.Group, **kwargs: Any) -> None:
    python_group.add_command(repository)
    python_group.add_command(remote)
    python_group.add_command(publication)
    python_group.add_command(distribution)
    python_group.add_command(content)
    main.add_command(python_group)
