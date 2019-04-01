using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace SistemaBancario.Models
{
    public class Usuario
    {
        public int codigoUsuario{ get; set; }
        public String nombre{ get; set; }
        public String userName{ get; set; }
        public String correo{ get; set; }
        public String contrasenia { get; set; }
    }
}