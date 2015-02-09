from spinnman import constants as spinnman_constants

from spynnaker.pyNN.buffer_management.command_objects.eieio_command_packet import EIEIOCommandPacket


class EventStopRequest(EIEIOCommandPacket):

    def __init__(self):
        EIEIOCommandPacket.__init__(
            self, spinnman_constants.EIEIO_COMMAND_IDS.EVENT_STOP.value)

    def is_command_packet(self):
        return True

    @staticmethod
    def create_command_from_reader(byte_reader):
        packet = EventStopRequest()
        return packet