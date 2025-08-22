from datetime import date
from .models import Conductor, Direccion, Vehiculo



def imprimir_modelos():
    conductores = Conductor.objects.all()
    for c in conductores:
        print(f"[{c.rut}]: {c.nombre} {c.apellido} - {c.fecha_nac}")
        if hasattr(c, "direccion"):
            d = c.direccion
            print(f"dirección: {d.calle} {d.numero} / {d.comuna} / {d.ciudad} / {d.region}")
        if hasattr(c, "vehiculo_set"):
            vehiculos = c.vehiculo_set.all()
            for v in vehiculos:
                print(f"Vehiculo: {v.marca} / {v.modelo} / {v.patente} / {v.year} ")


def crear_conductor(rut, nombre, apellido, fecha_nac):
    if not rut.isdigit() and not isinstance(fecha_nac, date):
        print("por favor validar los datos del conductor")
        return
    
    conductor = Conductor(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        fecha_nac=fecha_nac
    )
    conductor.save()
    imprimir_modelos()


def obtener_conductor(rut):
    return Conductor.objects.get(rut=rut)

def crear_direccion(conductor, calle, numero, dpto, comuna, ciudad, region):
    direccion = Direccion(
        conductor=conductor,
        calle=calle,
        numero=numero,
        dpto=dpto,
        comuna=comuna,
        ciudad=ciudad,
        region=region
    )
    direccion.save()
    imprimir_modelos()


def agregar_un_vehiculo(conductor, patente, marca, modelo, year):
    vehiculo = Vehiculo(
        conductor=conductor,
        patente=patente,
        marca=marca,
        modelo=modelo,
        year=year
    )

    vehiculo.save()
    imprimir_modelos()


def eliminar_vehiculo(vehiculo):
    Vehiculo.objects.get(id=vehiculo.id).delete()
    imprimir_modelos()


def eliminar_conductor(conductor):
    Conductor.objects.get(rut=conductor.rut).delete()


def actualizar_conductor(rut, nombre, apellido, fecha_nacimiento):
    c = Conductor.objects.get(rut=rut)
    c.nombre = nombre
    c.apellido = apellido
    c.fecha_nac = fecha_nacimiento

    c.save()
    imprimir_modelos()