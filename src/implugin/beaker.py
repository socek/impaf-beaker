from impaf.application import Application
from impaf.requestable import Requestable


class BeakerApplication(Application):

    def _create_config(self):
        super()._create_config()
        self.config.include('pyramid_beaker')


class BeakerRequestable(Requestable):

    def _unpack_request(self, request):
        super()._unpack_request(request)
        self.session = request.session
