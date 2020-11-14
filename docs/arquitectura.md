## Arquitectura

En primer lugar hay que analizar muy bien el problema que estamos tratando de resolver. El problema consiste en la gestión de un Conservatorio de forma que las gestiones que se realicen queden registradas facilitando la administración de dicho Centro y ofreciendo una solución *cloud* a una administración que sigue realizándose hoy en día sin avance tecnológico alguno. Por ejemplo, una matriculación de una asignatura se realiza de forma presencial en el Centro y mediante una inscripción en papel.

En este problema también nos encontramos con que queremos realizar las gestiones de forma automática y sin esperas por lo que queda descartada una arquitectura dirigida por eventos. Suponiendo que utilizáramos esta arquitectura no obtendríamos mejoras respecto al procedimiento actual ya que buscamos agilizarlo.

Por otro lado se debe realizar la gestión de las distintas tareas y componentes de la administración del Conservatorio de forma aislada de modo que cada gestión aunque esté relacionada con otros elementos del sistema de administración sea gestionada independientemente. Basándonos en este criterio una arquitectura monolítica quedaría descartada.

Uno de los problemas de utilizar una arquitectura inadecuada sería el impedimento de aumentar la escalabilidad o integración de posibles futuras funcionalidades como por ejemplo gestionar la biblioteca del Conservatorio. Además, buscamos con esta solución evitar cuellos de botella por lo que no vamos a considerar una arquitectura microkernel.

Teniendo en cuenta las características de dicho problema reconocemos que se necesita una arquitectura que permita la modularidad, la escalabilidad y facilidad de integración de nuevos elementos como podría ser la inclusión de una gestión de biblioteca. Para ello, podemos utilizar una **arquitectura de microservicios** la cual aporta todas estas ventajas. Realmente la arquitectura de microservicios es la que se debería de utilizar por omisión pero en nuestro caso además se adapta a cada una de las necesidades del problema.

Por último, cabe destacar que la arquitectura seleccionada nos permite aprovechar la descentralización de las gestiones y administración de la información y nos permite diseñar nuestro problema de una manera eficaz y sencilla.
