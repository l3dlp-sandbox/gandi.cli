""" Status commands module. """

from gandi.cli.core.base import GandiModule


class Status(GandiModule):

    """ Module to handle CLI commands.

    $ gandi status

    """

    base_url = 'https://status.gandi.net/api'

    @classmethod
    def descriptions(cls):
        """ Retrieve status descriptions from status.gandi.net. """
        schema = cls.json_call('%s/status/schema' % cls.base_url)
        descs = {}
        for val in schema['fields']['status']['value']:
            descs.update(val)
        return descs

    @classmethod
    def services(cls):
        """Retrieve services statuses from status.gandi.net."""
        return cls.json_call('%s/services' % cls.base_url)
