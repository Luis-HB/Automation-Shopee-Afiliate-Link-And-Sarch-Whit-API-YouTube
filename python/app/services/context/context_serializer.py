class ContextSerializer:

    @staticmethod
    def serialize(context):

        if hasattr(context, "to_dict"):
            return context.to_dict()

        return context