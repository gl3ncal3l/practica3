using SistemaBancario.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace SistemaBancario.Controllers
{
    public class RegistrarController : Controller
    {
        //
        // GET: /Registrar/

        public ActionResult Index()
        {
            Console.WriteLine("Hello World!");
            return View();
            
        }

        [HttpPost]
        public JsonResult NuevoUsuario(Usuario usuario)
        {
            //Console.WriteLine(nombre);
            Console.WriteLine("Entro al metodo POST");
            return Json("'Success':'true'");
            /*
            if (InsertarCoche(nuevoCoche))
                return Json("'Success':'true'");
            else
                return Json(String.Format("'Success':'false','Error':'Ha habido un error al insertar el registro.'"));
             * */
        }

    }
}
