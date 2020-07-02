'use strict';

module.exports.soma = async event => {	
	function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
	}

	let resultado = 'insira no formato (/soma?a=<valor>&b=<valor>) os valores de a e de b como query parameters para ver o resultado da soma'
    let a = 0;
		let b = 0;
		if (event.queryStringParameters && event.queryStringParameters.a && event.queryStringParameters.b) {
			resultado = 0			
			a = parseFloat(event.queryStringParameters.a) || 0;								
			b = parseFloat(event.queryStringParameters.b) || 0;				
			resultado = a + b
			if (!isNumber(event.queryStringParameters.a) || !isNumber(event.queryStringParameters.b) ){
				resultado = 'insira apenas números nos valores de a e de b como query parameters no formato (/soma?a=<valor>&b=<valor>) para ver o resultado da soma'
			}			
		}		

    return {
        statusCode: 200,
        body: JSON.stringify(
            {
                resultado
            },
            null,
            2
        ),
    };

    // Use this code if you don't use the http event with the LAMBDA-PROXY integration
    // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};