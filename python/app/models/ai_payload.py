from dataclasses import dataclass, field, asdict


@dataclass
class AIPayload:

    #
    # Informações do pipeline
    #
    pipeline: dict = field(default_factory=dict)

    #
    # Produto analisado
    #
    produto: dict = field(default_factory=dict)

    #
    # Consultas realizadas
    #
    consultas: list = field(default_factory=list)

    #
    # Informações adicionais
    #
    metadata: dict = field(default_factory=dict)

    #
    # Configuração do agente
    #
    config: dict = field(default_factory=dict)

    # =====================================================

    def to_dict(self):

        return asdict(self)