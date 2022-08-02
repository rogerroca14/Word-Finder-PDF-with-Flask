-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 02, 2022 at 06:10 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registro_archivos`
--

-- --------------------------------------------------------

--
-- Table structure for table `archivos_pdf`
--

CREATE TABLE `archivos_pdf` (
  `id_archivo` int(11) NOT NULL,
  `nombre_archivo` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `fecha_hora_subida` datetime NOT NULL,
  `ruta_pdf` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ruta_text` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `contenido` longtext COLLATE utf8_unicode_ci NOT NULL COMMENT 'Cadena de texto contenida en el PDF'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `archivos_pdf`
--

INSERT INTO `archivos_pdf` (`id_archivo`, `nombre_archivo`, `fecha_hora_subida`, `ruta_pdf`, `ruta_text`, `contenido`) VALUES
(26, 'a', '0000-00-00 00:00:00', 'a', 'a', 'textexample'),
(33, '1._Teoria_Introduccion.pdf', '2022-07-31 18:00:25', 'archivos_pdf/file-pdf-27.pdf', 'archivos_txt/file-text-27.txt', '               introduccion estadistica bayesiana estadistica bayesiana introduccion dr carlos lopez de castilla vasquez universidad nacional agraria la molina 2022-1 dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana introduccion teorema de bayes introduccion la estadistica bayesiana le debe su nombre al trabajo pionero del reverendo thomas bayes titulado: an essay towards solving a problem in the doctrine of chances publicado en 1764. el articulo fue enviado a la real sociedad de londres por richard price en 1763 quien escribio: yo ahora le mando un ensayo que he encontrado entre los papeles de nuestro fallecido amigo thomas bayes y el cual, en mi opinion, tiene un gran merito y bien merece ser preservado ... aunque la obra de thomas bayes data ya de mas de dos siglos la estadistica bayesiana es relativamente nueva y actualmente ostenta un gran desarrollo aunque no ajena tambien a grandes controversias. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana introduccion teorema de bayes introduccion la estadistica es el estudio de la incertidumbre. una forma de lidiar con ella es pensar en las probabilidades. algunos ejemplos: ¾cual es la probabilidad de lanzar dos dados y obtener como suma cuatro? ¾cual es la probabilidad que llueva mañana? ¾cual es la probabilidad que el universo siga expan- diendose para siempre? existen tres enfoques diferentes para de�nir probabilidades. la de�nicion clasica se basa en la suposicion de que cada resul- tado es igualmente probable. la de�nicion frecuentista requiere que se tenga una secuencia hipotetica de eventos in�nitos. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana introduccion teorema de bayes introduccion la de�nicion bayesiana se basa en una perspectiva personal, donde la probabilidad es una medida del conocimiento que se tiene sobre un fenomeno de interes. se trata de un enfoque subjetivo, pero que puede funcionar bien en una base estadistica rigurosa, y que conduce a resultados mucho mas intuitivos en comparacion al enfoque frecuentista. en el ejemplo de la expansion del universo se podria considerar la teoria del multiverso, donde existe un numero in�nito de uni- versos paralelos y preguntarse que fraccion tiene universos que se expanden para siempre. dependiendo de lo que se sepa sobre el universo, se podrian obtener diferentes respuestas. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana introduccion teorema de bayes teorema de bayes sean a y b dos eventos con pr (b) > 0, entonces: pr (a|b) = pr (b|a) pr (a) pr (b) si se tiene k eventos a1, · · · ,ak , los cuales constituyen una particion del espacio muestral Ω: pr (ai |b) = pr (b|ai ) pr (ai ) pr (b) = pr (b|ai ) pr (ai )∑k j=1 pr (b|aj) pr (aj) donde pr (b) se le conoce como probabilidad total. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana introduccion teorema de bayes teorema de bayes ejemplo 1: transmicion de señales un transmisor esta enviando un mensaje mediante un codigo binario con señales de 0 y 1. cada señal transmitida debe pasar por dos relevadores antes de llegar �nalmente al receptor. en cada relevador, la probabilidad de que la señal enviada sea diferente de la señal recibida (inversion de señal) es de 0,10. los relevadores funcionan independientemente uno de otro. el 60% de todas las señales enviadas desde el emisor son 1. si un 1 es recibido por el receptor ¾cual es la probabilidad de que haya sido enviado realmente un 1? dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana estadistica bayesiana distribucion predictiva posterior estadistica bayesiana el objetivo en la estadistica bayesiana es representar y actualizar la incertidumbre asociada a un parametro θ. un punto importante en la de�nicion clasica de inferencia es que el parametro θ es considerado como constante. la diferencia fundamental entre la teoria clasica y la bayesiana esta en que θ es considerado una variable aleatoria. la incertidumbre inicial sobre θ se representa usando una distri- bucion inicial o distribucion a priori. el proceso de actualizacion de la distribucion a priori se reali- za incorporando la informacion contenida en los datos, lo que permite hallar la distribucion posterior para θ. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana estadistica bayesiana distribucion predictiva posterior estadistica bayesiana el teorema de bayes, de�nido anteriormente usando eventos, puede presentarse en terminos de funciones de probabilidad o densidad: f (θ|y) = f (y |θ) f (θ) f (y) la distribucion marginal para y se puede obtener de la siguiente manera: f (y) = {∑ θ f (y |θ) f (θ) si θ es discreta∫ θ f (y |θ) f (θ) dθ si θ es continua y es llamada la distribucion predictiva a priori. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana estadistica bayesiana distribucion predictiva posterior estadistica bayesiana la distribucion a priori representa lo que es conocido de θ antes de observar los datos y se denota por f (θ). la distribucion posterior representa lo que se conoce de θ des- pues de observar los datos y se denota por f (θ|y). la funcion f (y |θ) es la distribucion muestral e incorpora la informacion proporcionada por los datos. el nucleo de la distribucion posterior es: f (θ|y) ∝ f (y |θ) f (θ) en muchos casos la distribucion muestral se reemplaza por la funcion de verosimilitud l (θ|y) en el teorema de bayes. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana estadistica bayesiana distribucion predictiva posterior estadistica bayesiana ejemplo 2: modelo binomial suponga que se tiene una muestra: y1, · · · , yn ∼ b (θ) y que a priori θ ∼ be (α, β). hallar la distribucion posterior. ejemplo 3: modelo de poisson suponga que se tiene una muestra: y1, · · · , yn ∼ p (λ) y que a priori λ ∼ g (α, β). hallar la distribucion posterior. dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana estadistica bayesiana distribucion predictiva posterior distribucion predictiva posterior luego de obtener la distribucion posterior es posible realizar el proceso de prediccion sobre una cantidad no observable ỹ que se de�ne a partir de la distribucion muestral. algunas opciones son: ỹ = ỹi ỹ = ∑m i=1 ỹi ỹ = 1 m m∑ i=1 ỹi la distribucion predictiva posterior: f (ỹ |y) = {∑ θ f (ỹ |θ) f (θ|y) si θ es discreta∫ θ f (ỹ |θ) f (θ|y) dθ si θ es continua dr carlos lopez de castilla vasquez estadistica bayesiana introduccion estadistica bayesiana estadistica bayesiana distribucion predictiva posterior distribucion predictiva posterior ejemplo 4: distribucion predictiva posterior modelo binomial considere el modelo binomial del ejemplo 2. hallar la distri- bucion predictiva posterior para ỹ = ỹi , un nuevo ensayo de bernoulli. ejemplo 5: distribucion predictiva posterior modelo de poisson considere el modelo de poisson del ejemplo 3. hallar la distri- bucion predictiva posterior para ỹ = ∑m i=1 ỹi , el numero total de eventos de interes en una nueva muestra ỹ1, · · · , ỹm. dr carlos lopez de castilla vasquez estadistica bayesiana 	introduccion 	introduccion 	teorema de bayes 	estadistica bayesiana 	estadistica bayesiana 	distribucion predictiva posterior '),
(34, 'MINSA_-_Carnet_Vacunacion.pdf', '2022-07-31 19:00:37', 'archivos_pdf/file-pdf-34.pdf', 'archivos_txt/file-text-34.txt', '          minsa - carnet vacunacion certificado de vacunacion / vaccination certificate nombre / name hilario llajaruna anampa fecha de nacimiento / date of birth 16/04/1963 documento de identidad / identi>cation document dni: 10608612 nacionalidad / nationality peru sexo / sex m vacuna / vaccine vacuna contra covid vacunado / vaccinated fecha de vacunacion / vaccination date dosis / dose fabricante y lote de vacuna / product name and manufacturer lot number lugar de vacunacion / vaccination place 26/06/2021 1° dosis pfizer (fa9093) lima sur - complejo deportivo del secto b de manchay - lima lima pachacamac 17/07/2021 2° dosis pfizer (fa7483) lima sur - complejo deportivo del secto b de manchay - lima lima pachacamac certi>cado emitido por / certi>cate issued by: ministerio de salud del peru fecha de emision / date of issue 30/07/2022, 4:01 pm copyright © 2022. desarrollado por la o[cina general de tecnologias de la informacion del ministerio de salud | todos los derechos reservados. regresar imprimir salir 30/07/22, 16:01 page 1 of 1 '),
(35, 'Carnet.pdf', '2022-07-31 19:04:48', 'archivos_pdf/file-pdf-35.pdf', 'archivos_txt/file-text-35.txt', '        roger ricardo roca llamocca dni: edad:74684620 23 años vacunacion covid-19 con tercera dosis dosis '),
(36, 'Carnet.pdf', '2022-07-31 19:06:17', 'archivos_pdf/file-pdf-36.pdf', 'archivos_txt/file-text-36.txt', '        roger ricardo roca llamocca dni: edad:74684620 23 años vacunacion covid-19 con tercera dosis dosis '),
(37, 'Carnet.pdf', '2022-07-31 19:53:15', 'archivos_pdf/file-pdf-37.pdf', 'archivos_txt/file-text-37.txt', '        roger ricardo roca llamocca dni: edad:74684620 23 años vacunacion covid-19 con tercera dosis dosis '),
(39, 'Carnet.pdf', '2022-07-31 19:56:30', 'archivos_pdf/file-pdf-39.pdf', 'archivos_txt/file-text-39.txt', '        roger ricardo roca llamocca dni: edad:74684620 23 años vacunacion covid-19 con tercera dosis dosis ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `archivos_pdf`
--
ALTER TABLE `archivos_pdf`
  ADD PRIMARY KEY (`id_archivo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `archivos_pdf`
--
ALTER TABLE `archivos_pdf`
  MODIFY `id_archivo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
