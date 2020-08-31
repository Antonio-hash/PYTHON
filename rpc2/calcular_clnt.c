/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include <memory.h> /* for memset */
#include "calcular.h"

/* Default timeout can be changed using clnt_control() */
static struct timeval TIMEOUT = { 25, 0 };

int *
sumar_1(int a, int b,  CLIENT *clnt)
{
	sumar_1_argument arg;
	static int clnt_res;

	memset((char *)&clnt_res, 0, sizeof(clnt_res));
	arg.a = a;
	arg.b = b;
	if (clnt_call (clnt, sumar, (xdrproc_t) xdr_sumar_1_argument, (caddr_t) &arg,
		(xdrproc_t) xdr_int, (caddr_t) &clnt_res,
		TIMEOUT) != RPC_SUCCESS) {
		return (NULL);
	}
	return (&clnt_res);
}

int *
restar_1(int a, int b,  CLIENT *clnt)
{
	restar_1_argument arg;
	static int clnt_res;

	memset((char *)&clnt_res, 0, sizeof(clnt_res));
	arg.a = a;
	arg.b = b;
	if (clnt_call (clnt, restar, (xdrproc_t) xdr_restar_1_argument, (caddr_t) &arg,
		(xdrproc_t) xdr_int, (caddr_t) &clnt_res,
		TIMEOUT) != RPC_SUCCESS) {
		return (NULL);
	}
	return (&clnt_res);
}

int *
multiplicar_1(int a, int b,  CLIENT *clnt)
{
	multiplicar_1_argument arg;
	static int clnt_res;

	memset((char *)&clnt_res, 0, sizeof(clnt_res));
	arg.a = a;
	arg.b = b;
	if (clnt_call (clnt, multiplicar, (xdrproc_t) xdr_multiplicar_1_argument, (caddr_t) &arg,
		(xdrproc_t) xdr_int, (caddr_t) &clnt_res,
		TIMEOUT) != RPC_SUCCESS) {
		return (NULL);
	}
	return (&clnt_res);
}

float *
dividir_1(int a, int b,  CLIENT *clnt)
{
	dividir_1_argument arg;
	static float clnt_res;

	memset((char *)&clnt_res, 0, sizeof(clnt_res));
	arg.a = a;
	arg.b = b;
	if (clnt_call (clnt, dividir, (xdrproc_t) xdr_dividir_1_argument, (caddr_t) &arg,
		(xdrproc_t) xdr_float, (caddr_t) &clnt_res,
		TIMEOUT) != RPC_SUCCESS) {
		return (NULL);
	}
	return (&clnt_res);
}

float *
areacircunferencia_1(float radio,  CLIENT *clnt)
{
	static float clnt_res;

	memset((char *)&clnt_res, 0, sizeof(clnt_res));
	if (clnt_call (clnt, areacircunferencia,
		(xdrproc_t) xdr_float, (caddr_t) &radio,
		(xdrproc_t) xdr_float, (caddr_t) &clnt_res,
		TIMEOUT) != RPC_SUCCESS) {
		return (NULL);
	}
	return (&clnt_res);
}