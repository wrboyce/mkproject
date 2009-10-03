mkproject
=========

A utility for creating skeleton project directories.

## Usage

    $ mkproject TYPE NAME

Where `TYPE` is a project template, and `NAME` is the name of your project. Projects will be made in ~/Dev by default, but this can be overriden with the MKPROJECT_ROOT environmental variable. If you wanted to store your projects in ~/code, simply add `export MKPROJECT_ROOT=~/code` to your bash profile:

    $ echo "export MKPROJECT_ROOT=~/code" >> ~/.bash_profile


## mkprojectrc

mkprojectrc lives at `~/.mkproject/mkprojectrc` and is an ini-style configuration file.

### defaults

The defaults section allows you to provide your defaults for project variables.

    [defaults]
    author_name=Joe Bloggs
    author_email=joe.bloggs@gmail.com
    github_user=joebloggs


## Project Templates

Project templates consist of two parts, a directory structure to be copied and an optional settings file. mkproject will check ~/.mkproject and then /etc/mkproject for a directory called `TYPE`.

### Templates/Variables

Project template files may contain variables in the form `${var}`, which will be replaced on file creation. The only variable available by default is `name`, which contains the project name. Additional variables must be registered in the settings file.

### Settings

If supplied, the settings file must be named `projectname_settings.py` in the same directory as the project skeleton. There are 5 possible settings:

#### variables

All variables aside `name` must be registered with a `varspec` in the format `(var_name, default_value, description)`:

    variables = (
        ('author_name', '', "Author's name"),
        ('author_email', '', "Author's email"),
        ('github_user', '', "Github username"),
    )

#### path

`path` specifies where the directory structure will be copied to, and defaults to `%(name)s`. You may want to change this if, for example, you wanted to create a new virtualenv and copy the skeleton directory into a subdirectory of that environment.

    path = 'src/%(name)s'

#### pre_commands

A tuple of commands to be executed _before_ the project is created. Commands must be provided as a string, and standard python string formatting may be used for any variables. Commands are executed from `$MKPROJECT_ROOT`.

    pre_commands = (
        'mkdir %(name)',
        'virtualenv --no-site-packages ./%(name)',
    )

#### post_commands

A tuple of commands to be executed _after_ the project is created. Commands are executed from `$MKPROJECT_ROOT/%(path)s`.

    post_commands = (
        'git init',
        'git remote add origin git@github.com/%(github_user)s/%(name)s.git',
    )
