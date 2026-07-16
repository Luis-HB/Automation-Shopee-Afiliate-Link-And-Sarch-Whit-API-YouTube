from models.publicacao import Publicacao


class PublicacaoFactory:

    @staticmethod
    def from_dict(dados):

        return Publicacao(

            produto_id=dados["produto_id"],

            video_id=dados["video_id"],

            score=dados.get("score", 0),

            legenda=dados.get("legenda", ""),

            hashtags=dados.get("hashtags", ""),

            status=dados.get("status", "PENDENTE"),

            data_agendada=dados.get("data_agendada")
        )