import copy

from templer.zope import BasicZope
from templer.core.vars import StringVar, EASY, EXPERT

try:
    from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
    from templer.localcommands import LOCAL_COMMANDS_MESSAGE
except ImportError:
    SUPPORTS_LOCAL_COMMANDS = False

HELP_TEXT = """
This creates a Plone add-on package with the required infrastructure
to create custom Dexterity content types.
"""

POST_RUN_TEXT = """"""

if SUPPORTS_LOCAL_COMMANDS:
    HELP_TEXT += """
This template supports local commands.  These commands allow you to
generate skeleton content types and behaviors to your new package.
"""
    POST_RUN_TEXT = LOCAL_COMMANDS_MESSAGE


class Dexterity(BasicZope):
    _template_dir = 'templates/dexterity'
    summary = 'A Plone project that uses Dexterity content types'
    help = HELP_TEXT
    post_run_msg = POST_RUN_TEXT
    required_templates = ['plone_basic']
    default_required_structures = ['egg_docs', 'bootstrap', ]
    category = "Plone Development"
    use_cheetah = True
    use_local_commands = SUPPORTS_LOCAL_COMMANDS

    vars = copy.deepcopy(BasicZope.vars)
    vars.insert(1, StringVar(
        'title',
        title='Project Title',
        description='Title of the project',
        modes=(EASY, EXPERT),
        default='Example Name',
        help="""
This becomes the title of the project. It is used in the
GenericSetup registration for the project and, as such, appears
in Plone's Add/Remove products form.
""",
    ))

    def pre(self, command, output_dir, vars):
        super(Dexterity, self).pre(command, output_dir, vars)
        vars['use_localcommands'] = self.use_local_commands
