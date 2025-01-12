from django.shortcuts import render
from .models import MyTable  # Importa el modelo de tu tabla

def my_table_view(request):
    # Obtén todos los datos de la tabla
    rows = MyTable.objects.all()
    # Pasa los datos al template
    return render(request, 'testapp/my_table.html', {'rows': rows})
