# include "calcular.h"
#include <math.h>

#define PI 3.141592



int * sumar_1_svc(int a, int b, struct svc_req *rqstp)
{
static int r;
r = a + b;
return(&r);
}

int * restar_1_svc(int a, int b, struct svc_req *rqstp)
{
static int r;
r = a - b;
return(&r);
}

int * multiplicar_1_svc(int a, int b, struct svc_req *rqstp)
{
    static int r;
    r = a * b;
    return(&r);
}

float * dividir_1_svc(int a, int b, struct svc_req *rqstp)
{
    static float r;
    r = a / b;
    return(&r);
}

float * areacircunferencia_1_svc(float radio, struct svc_req *rqstp) {
    static float r;

    r = (float)(PI * pow( radio, 2 ));


    return(&r);

}

