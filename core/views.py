from django.shortcuts import render , redirect, get_object_or_404
from .models import Proveedor
from.forms import ProveedorForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def contacto(request):
    return render(request, 'core/contacto.html')
def seccion_gatos(request):
    return render(request, 'core/seccion-gatos.html')
def seccion_perros(request):
    return render(request, 'core/seccion-perros.html')
def formulario_enviado(request):
    return render(request, 'core/formulario-enviado.html')

def agregar_proveedor(request):
    return render(request, 'core/proveedor/agregar.html')
@login_required
@permission_required('app.add_proveedor')
def agregar_proveedor(request):

    data = {
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor agregado exitosamente")
            return redirect(to="listar-proveedor")
        else:
            data["form"] = formulario    


    return render(request, 'core/proveedor/agregar.html', data)
@login_required
@permission_required('app.view_proveedor')
def listar_proveedor(request):
    proveedor = Proveedor.objects.all()

    data = {
        'proveedor': proveedor
    }

    return render(request, 'core/proveedor/listar.html', data)



@login_required
@permission_required('app.change_proveedor')
def modificar_proveedor(request, rut):

    proveedor = get_object_or_404(Proveedor, rut=rut)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor modificado exitosamente")
            return redirect(to="listar-proveedor")
        data["form"] = formulario    

    return render(request, 'core/proveedor/modificar.html', data)




@login_required
@permission_required('app.delete_proveedor')
def eliminar_proveedor(request, rut):
    proveedor = get_object_or_404(Proveedor, rut=rut)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado exitosamente")
    return redirect(to="listar-proveedor")






def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro Correcto")
            return redirect(to="index")

        data["form"] = formulario    

    return render(request, 'registration/registro.html', data)


