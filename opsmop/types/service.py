
from opsmop.core.field import Field
from opsmop.core.fields import Fields
from opsmop.core.resource import Resource
from opsmop.types.type import Type

class Service(Type):

    """
    Represents a OS background service.
    """

    def fields(self):
        return Fields(
            name = Field(kind=str),
            started = Field(kind=bool, default=True),
            enabled = Field(kind=bool, default=True),
            restarted = Field(kind=bool, default=False),
        )

    def validate(self):
        pass

    def get_provider(self, method):
        if method == 'brew':
            from opsmop.providers.service.brew import Brew
            return Brew
        raise ValidationError("unsupported provider: %s" % method)

    def default_provider(self, facts):
        return facts.default_service_manager()
