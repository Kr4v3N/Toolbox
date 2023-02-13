import pyshark

target_ip = '192.168.0.28'

capture = pyshark.LiveCapture('wlp2s0')

for p in capture.sniff_continuously():
    if hasattr(p, 'udp'):
        try:
            protocol = p.transport_layer
            source_address = p.ip.src
            source_port = p[protocol].srcport
            destination_address = p.ip.dst
            destination_port = p[protocol].dstport
            packettime = p.sniff_time

            if source_address == target_ip or destination_address == target_ip:
                print(f'{protocol=} {source_address=} {source_port=} {destination_address=} {destination_port=} {packettime=}')

        except Exception as ex:
            pass