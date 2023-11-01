from rest_framework.generics import CreateAPIView
from .serializers import AccountSerializer
from .models import Account
from drf_spectacular.utils import extend_schema


class AccountView(CreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    @extend_schema(
        description="Rota para criação de Accounts",
        tags=["Criação de Account"],
        parameters=[
            AccountSerializer,
        ],
    )
    def post(self, request):
        return self.create(request)
