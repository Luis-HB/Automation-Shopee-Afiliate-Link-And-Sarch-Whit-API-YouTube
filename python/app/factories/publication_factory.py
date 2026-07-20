from models.publication import Publication


class PublicationFactory:

    @staticmethod
    def from_dict(data):

        return Publication(

            produto_id=data["produto_id"],

            video_id=data["video_id"],

            score=data.get("score", 0),

            legenda=data.get("legenda", ""),

            hashtags=data.get("hashtags", ""),

            status=data.get("status", "PENDENTE"),

            data_agendada=data.get("data_agendada")

        )