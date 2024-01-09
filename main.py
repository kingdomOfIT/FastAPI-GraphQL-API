from fastapi import FastAPI
import graphene
import models
from db_conf import db_session
from schemas import PostSchema
from schemas import PostModel

from starlette_graphene3 import GraphQLApp, make_graphiql_handler

db = db_session.session_factory()
app = FastAPI()

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostModel)
    post_by_id = graphene.Field(PostModel, post_id=graphene.Int(required=True))

    def resolve_all_posts(self, info):
        query = PostModel.get_query(info)
        return query.all()
    
    def resolve_post_by_id(self, info, post_id):
        return db.query(models.Post).filter(models.Post.id == post_id).first()

class CreateNewPost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
    
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, content):
        post = PostSchema(title=title, content=content)
        db_post = models.Post(title=post.title, content= post.content)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        ok = True
        return CreateNewPost(ok=ok)

class PostMutation(graphene.ObjectType):
    create_new_post = CreateNewPost.Field()

app.mount("/graphql",GraphQLApp(schema=graphene.Schema(query=Query, mutation=PostMutation),on_get=make_graphiql_handler()))