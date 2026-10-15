from flask import Flask, render_template, jsonify

app = Flask(__name__)

productos = [
    {
        "id": 1,
        "nombre": "Visor HoloGlass Pro X",
        "categoria": "Hardware Neural",
        "precio": 1290000,
        "descripcion": "Interfaz de realidad aumentada con proyección holográfica 8K y control por gestos.",
        "imagen": "https://images.unsplash.com/photo-1593508512255-86ab42a8e620?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "nombre": "Nexo Cyber-Pod Audio",
        "categoria": "Sonido Hi-Tech",
        "precio": 450000,
        "descripcion": "Cancelación de ruido magnética y transmisión cuántica sin latencia.",
        "imagen": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "nombre": "Chaqueta Neon Luminance",
        "categoria": "Moda Tech",
        "precio": 380000,
        "descripcion": "Fibra óptica autorregulable de temperatura y patrones LED personalizables.",
        "imagen": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 4,
        "nombre": "Reloj Biónico Quantum-V",
        "categoria": "Wearables",
        "precio": 890000,
        "descripcion": "Monitoreo biométrico avanzado y holograma proyectable de notificaciones.",
        "imagen": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 5,
        "nombre": "iPhone 12",
        "categoria": "Celulares",
        "precio": 1800000,
        "descripcion": "Pantalla Super Retina XDR de 6.1 pulgadas, chip A14 Bionic y sistema de doble cámara de 12 MP.",
        "imagen": "https://images.unsplash.com/photo-1605236453806-6ff36851218e?w=600&auto=format&fit=crop"
    },
    {
        "id": 6,
        "nombre": "iPhone 13",
        "categoria": "Celulares",
        "precio": 2400000,
        "descripcion": "Pantalla Super Retina XDR, chip A15 Bionic y modo Cine para grabación con enfoque dinámico.",
        "imagen": "https://images.unsplash.com/photo-1632661674596-df8be070a5c5?w=600&auto=format&fit=crop"
    },
    {
        "id": 7,
        "nombre": "iPhone 14",
        "categoria": "Celulares",
        "precio": 3100000,
        "descripcion": "Detección de accidentes, batería de mayor duración y chip A15 Bionic con GPU de 5 núcleos.",
        "imagen": "https://images.unsplash.com/photo-1663499482523-1c0c1bae4ce1?w=600&auto=format&fit=crop"
    },
    {
        "id": 8,
        "nombre": "iPhone 15",
        "categoria": "Celulares",
        "precio": 3800000,
        "descripcion": "Dynamic Island, cámara principal de 48 MP, conector USB-C y diseño con vidrio teñido en masa.",
        "imagen": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=600&auto=format&fit=crop"
    },
    {
        "id": 9,
        "nombre": "iPhone 16",
        "categoria": "Celulares",
        "precio": 4500000,
        "descripcion": "Diseñado para Apple Intelligence, control de cámara interactivo y chip A18 ultra eficiente.",
        "imagen": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600&auto=format&fit=crop"
    },
    {
        "id": 10,
        "nombre": "iPhone 17",
        "categoria": "Celulares",
        "precio": 5200000,
        "descripcion": "Chip A19 Pro, pantalla ProMotion de 120Hz adaptativa y cuerpo ultra delgado de titanio pulido.",
        "imagen": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=600&auto=format&fit=crop"
    },
    {
        "id": 11,
        "nombre": "iPhone 18 Ultra",
        "categoria": "Celulares",
        "precio": 6000000,
        "descripcion": "Cámara holográfica 8K, procesador cuántico A20 Neural y pantalla OLED sin bordes de nueva generación.",
        "imagen": "https://images.unsplash.com/photo-1591337676887-a217a6970a8a?w=600&auto=format&fit=crop"
    }
]

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/api/productos')
def obtener_productos():
    return jsonify(productos)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)