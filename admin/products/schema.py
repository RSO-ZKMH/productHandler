import graphene
from graphene_django import DjangoObjectType
from .models import Product

class ProductType(DjangoObjectType):
    class Meta: 
        model = Product
        fields = ('id','title', 'price', 'store')

class Query(graphene.ObjectType):
    products = graphene.List(ProductType)
    def resolve_products(root, info, **kwargs):
        # Querying a list
        return Product.objects.all()
schema = graphene.Schema(query=Query)