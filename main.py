import strawberry
import typing

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from cgan import generator_inference


@strawberry.type
class AddressPath:
    path: str


@strawberry.input
class ImageClass:
  class_number: int


@strawberry.type
class Mutation:
  @strawberry.field
  def generate_class_photo(self, image_cls: ImageClass) -> typing.List[AddressPath]:
    return [AddressPath(path=path_value) for path_value in generator_inference(image_cls.class_number)]


schema = strawberry.Schema(query=AddressPath, mutation=Mutation)


graphql_app = GraphQLRouter(schema)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")