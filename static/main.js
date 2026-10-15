let carrito = [];

document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/productos')
        .then(response => response.json())
        .then(productos => mostrarProductos(productos));
});

function mostrarProductos(productos) {
    const contenedor = document.getElementById('products-container');
    contenedor.innerHTML = '';
    
    productos.forEach(p => {
        contenedor.innerHTML += `
            <div class="product-card">
                <img src="${p.imagen}" alt="${p.nombre}">
                <div class="product-info">
                    <h3>${p.nombre}</h3>
                    <p style="font-size:0.9rem; color:#a0aec0;">${p.descripcion}</p>
                    <div class="price">$${p.precio.toLocaleString()}</div>
                    <button class="btn-add" onclick="agregarAlCarrito(${p.id}, '${p.nombre}', ${p.precio})">
                        <i class="fa-solid fa-cart-plus"></i> AGREGAR
                    </button>
                </div>
            </div>
        `;
    });
}

function agregarAlCarrito(id, nombre, precio) {
    carrito.push({ id, nombre, precio });
    actualizarCarrito();
    toggleCart(true);
}

function actualizarCarrito() {
    document.getElementById('cart-count').innerText = carrito.length;
    const itemsContenedor = document.getElementById('cart-items');
    let total = 0;
    
    itemsContenedor.innerHTML = '';
    carrito.forEach((item, index) => {
        total += item.precio;
        itemsContenedor.innerHTML += `
            <div style="display:flex; justify-content:space-between; margin:10px 0; border-bottom:1px solid #333; padding-bottom:5px;">
                <div>
                    <div>${item.nombre}</div>
                    <small style="color:var(--neon-blue);">$${item.precio.toLocaleString()}</small>
                </div>
                <button onclick="eliminarDelCarrito(${index})" style="background:none; border:none; color:red; cursor:pointer;">&times;</button>
            </div>
        `;
    });
    
    document.getElementById('cart-total').innerText = total.toLocaleString();
}

function eliminarDelCarrito(index) {
    carrito.splice(index, 1);
    actualizarCarrito();
}

function toggleCart(forceOpen = false) {
    const sidebar = document.getElementById('cart-sidebar');
    if (forceOpen) {
        sidebar.classList.add('active');
    } else {
        sidebar.classList.toggle('active');
    }
}

function checkoutWhatsApp() {
    if (carrito.length === 0) {
        alert("El carrito está vacío.");
        return;
    }
    
    let mensaje = "¡Hola! Quiero realizar el siguiente pedido:\n\n";
    let total = 0;
    
    carrito.forEach(item => {
        mensaje += `- ${item.nombre}: $${item.precio.toLocaleString()}\n`;
        total += item.precio;
    });
    
    mensaje += `\n*Total a pagar: $${total.toLocaleString()}*`;
    
    // Cambia este número por tu número real con código de país (ejemplo Colombia: 57)
    const numeroTelefono = "573106970738"; 
    const url = `https://wa.me/${numeroTelefono}?text=${encodeURIComponent(mensaje)}`;
    
    window.open(url, '_blank');
}
