curl -X POST -H "Content-Type: application/json" -d '{	"CRIM"     	: "0.02731"	,
														"ZN"     	: "0.0"		,
														"INDUS"    	: "7.07"	,
														"CHAS"     	: "0.0"		,
														"NOX"     	: "0.469"	,
														"RM"     	: "6.421"	,
														"AGE"     	: "78.9"	,
														"DIS"     	: "4.9671"	,
														"RAD"     	: "2.0"		,
														"TAX"     	: "242.0"	,
														"PTRATIO"   : "17.8"	,
														"B"     	: "396.9"	,
														"LSTAT"    	: "9.14"	,
														"MEDV"     	: "-1"  }' http://127.0.0.1:8000/houses/


curl http://127.0.0.1:8000/house/1/