module Main where
	
	potencia :: Double -> Double -> Double
	potencia x n = x**n

	--Funcion para obtener el primer parametro
	calE :: [Double] -> Double
	calE v = head v

	--Funcion para obtener el segundo parametro
	calC :: [Double] -> Double
	calC v = head $ tail v

	--Funcion para obtener el tercer parametro
	calR :: [Double] -> Double
	calR v = head $ tail (tail v)

	--Funcion para obtener el ultimo parametro
	calT :: [Double] -> Double
	calT v = last v

	--Funcion que lee el fichero con los parametros y los almacena en variables
	muestraContenidoFichero :: FilePath -> IO ()
	muestraContenidoFichero f = do
  		cs <- readFile f
  		let v = words cs
  		let v1 = map read v :: [Double] 
  		let e = calE v1
  		let c = calR v1
  		let r = calC v1
  		let t = calT v1
  		--Se genera el fichero con la lista a graficar
  		writeFile "DatosGraficarQ.txt" (capacitor e c r t)
  		writeFile "DatosGraficarV.txt" (voltaje e c r t)
  		writeFile "DatosGraficarI.txt" (corriente e c r t)

  	--Funcion auxiliar
 	cal :: Double -> Double -> Double -> Double
 	cal k r c = (-k)/(r*c)

 	--Funcion para calcular la carga en un instante de tiempo t
 	funCapacitor:: Double -> Double -> Double -> Double -> Double
 	funCapacitor e c r k = (e*c) * ( 1 - potencia 2.71828183 (cal k r c))

 	--Funcion que genera la lista de la carga en un intervalo de tiempo
	capacitor :: Double -> Double -> Double -> Double -> String
	capacitor e c r t = unlines ( map show [ funCapacitor e c r k | k <- [0,(t/49)..t]] )

	--Funcion que calcula el voltaje en un instante de tiempo t
	funVoltaje :: Double -> Double -> Double -> Double -> Double
	funVoltaje e c r k = e*(1-potencia 2.71828183 (cal k r c))

	--Funcion que genera la lista de la carga en un intervalo de tiempo
	voltaje :: Double -> Double -> Double -> Double -> String
	voltaje e c r t = unlines ( map show [ funVoltaje e c r k | k <- [0,(t/49)..t]] )

	--Funcion que calcula la corriente en un instante de tiempo t
	funCorriente :: Double -> Double -> Double -> Double -> Double
	funCorriente e c r k = (e/r)*(potencia 2.71828183 (cal k r c))

	--Funcion que genera la lista de la carga en un intervalo de tiempo
	corriente :: Double -> Double -> Double -> Double -> String
	corriente e c r t = unlines ( map show [ funCorriente e c r k | k <- [0,(t/49)..t]] )


  	

	main = do 	
		muestraContenidoFichero "datosint.txt"
