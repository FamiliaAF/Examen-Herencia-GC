# Ejercicios de Herencia Múltiple

Este repositorio contiene ejercicios que demuestran cómo utilizar herencia múltiple en Python para combinar funcionalidades de diferentes clases base en clases derivadas. Cada ejercicio aborda un escenario práctico y incluye un objetivo específico.

---

## **Ejercicio 1: Clases Base de Mascotas**

### Requisitos:
1. Crea una clase `Animal` con un método `comer` que devuelva `"Estoy comiendo"`.
2. Crea otra clase `Jugueton` con un método `jugar` que devuelva `"Me encanta jugar"`.
3. Define una clase `Perro` que herede de ambas clases y tenga un método adicional `ladrar` que devuelva `"Guau Guau!"`.

### **Objetivo:**
Usar herencia múltiple para combinar habilidades en una clase derivada.

---

## **Ejercicio 2: Electrodomésticos**

### Requisitos:
1. Crea una clase `Electrodomestico` con un método `encender` que devuelva `"El electrodoméstico está encendido"`.
2. Crea otra clase `Conectividad` con un método `conectar_wifi` que devuelva `"Conectado a WiFi"`.
3. Define una clase `TelevisorInteligente` que herede de ambas clases y tenga un método adicional `streaming` que devuelva `"Iniciando transmisión en línea"`.

### **Objetivo:**
Combinar características generales de electrodomésticos con conectividad.

---

## **Ejercicio 3: Vehículos Especializados**

### Requisitos:
1. Define una clase `Vehiculo` con un método `arrancar` que devuelva `"El vehículo está en marcha"`.
2. Crea otra clase `TodoTerreno` con un método `activar_4x4` que devuelva `"Modo 4x4 activado"`.
3. Define una clase `Camioneta` que herede de ambas clases y tenga un método adicional `cargar_carga` que devuelva `"Cargando carga en la camioneta"`.

### **Objetivo:**
Usar herencia múltiple para crear vehículos con funcionalidades combinadas.

---

## **Retos**

### **Reto 1: Resolver Conflictos en Métodos**

1. Crea dos clases base con un método del mismo nombre.
2. Define una clase derivada que herede de ambas.
3. Escribe un método propio en la clase derivada que resuelva el conflicto.

### **Pista:**
Usa `super()` o llama explícitamente a los métodos de las clases base para resolver los conflictos de métodos.

---

## **Instrucciones**

1. Implementa cada ejercicio en archivos separados para una mejor organización.
2. Prueba cada clase derivada llamando a sus métodos y asegurándote de que los resultados sean los esperados.
3. Resuelve el reto utilizando las técnicas mencionadas para manejar conflictos en la herencia múltiple.

---