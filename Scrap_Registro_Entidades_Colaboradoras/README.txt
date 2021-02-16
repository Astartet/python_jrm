Scraper del Registro de Entidades Colaboradoras

Autor: Jorge Rodríguez Mora
Beneficiario: INVEPAT

Este programa consiste en la obtención de forma semiautomática de los resultados de un formulario

Lo primero será deshabilitar el firewall de la red privada a traves de windows defender. Una vez hecho, podremos ejecutar el programa.

Deberemos tener instalado en el equipo MSEdge y en la misma carpeta de instalación deberemos incorporar el webdriver correspondiente a la version de MSEdge

1. Ejecutaremos "rellenar_registro_entidades_colaboradoras" desde la terminal (python)
2. Aparecerá el navegador con la dirección correspondiente, si no aparece nada deberemos volver a ejecutar el programa
3. Si ha ido todo bien, se deberá ir completando el formulario, hay un tiempo de espera de 5 segundo para clickar en el pop-up que aparece
4. Cuando se cargen los resultados el programa irá manipulando la web para obtener la información deseada.
5. Cuando acabe los archivos estarán en la carpeta "html_files"

---------------------------CSV-------------------------

Para exportar a csv deberemos ejecutar el programa "analisis_html_registro_entidades_colaboradoras" y nos pedirá el nombre el archivo a formatear
El resultado aparecerá en la carpeta csv_files