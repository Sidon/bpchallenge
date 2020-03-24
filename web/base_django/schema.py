import graphene
from web.base_django.api.customer import schema as core_schema


class Query(
    # core_schema.ClienteQuery,
    core_schema.ItemQuery,
    graphene.ObjectType):

    pass

# class Mutation(users.schema.Mutation):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query)
