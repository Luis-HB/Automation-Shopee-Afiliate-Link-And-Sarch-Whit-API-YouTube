from dataclasses import asdict

class PayloadSerializer:

    def serialize(self, payload):

        return asdict(payload)