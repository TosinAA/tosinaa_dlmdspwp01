CREATE DATABASE IF NOT EXISTS pwpDatasets;

USE pwpDatasets;

-- Creating the table objects to perform csv ingestion using python

CREATE OR REPLACE TABLE IF NOT EXISTS train(
	x float, 
	y1 float,
	y2 float,
	y3 float,
	y4 float
) ;


CREATE TABLE IF NOT EXISTS test(
	x float, 
	y float
); 


CREATE TABLE IF NOT EXISTS idealfour(
	x float,
	y1 float,
	y2 float,
	y3 float,
	y4 float
);


CREATE TABLE IF NOT EXISTS ideal(
	x float, 
	y1 float,
	y2 float,
	y3 float,
	y4 float,
    y5 float,
	y6 float,
	y7 float,
	y8 float,
	y9 float,
	y10 float,
	y11	float,
	y12	float,
	y13	float,
	y14	float,
	y15	float,
	y16	float,
	y17	float,
	y18	float,
	y19	float,
	y20	float,
	y21	float,
	y22	float,
	y23	float,
	y24	float,
	y25	float,
	y26	float,
	y27	float,
	y28	float,
	y29	float,
	y30	float,
	y31	float,
	y32	float,
	y33	float,
	y34	float,
	y35	float,
	y36	float,
	y37	float,
	y38	float,
	y39	float,
	y40	float,
	y41	float,
	y42	float,
	y43	float,
	y44	float,
	y45	float,
	y46	float,
	y47	float,
	y48	float,
	y49	float,
	y50	float
);