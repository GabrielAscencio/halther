module.exports = {
    devServer: {
      host: '0.0.0.0',  // Escuchar en todas las interfaces
      port: 80,  // Puedes cambiar el puerto si prefieres otro, pero 80 es común para producción
      disableHostCheck: true,  // Asegura que pueda acceder desde cualquier dirección
    },
  };