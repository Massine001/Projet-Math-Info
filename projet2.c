#include<stdio.h>
#include<stdlib.h>
#include <math.h>
#include <errno.h>                  //utiliser <errno.h> pour détecter l'erreur d'une fonction mathématique
int k;
double f(double *t, double *y,double Tamb, int choix){ 
    float tmp = *t, b;
    double log ( double x );
    if (choix == 1){
        return *t*(Tamb-(*y));
    }
    if (choix == 2){
        b = (log(tmp)*(Tamb-(*y)));
        return b;
    }
    if (choix == 3){
        return (Tamb-(*y))*((2*log((*t))/((*t)*(1+log((*t))*log((*t))))));
    }
    if (choix == 4 && (*y)!=0){
        return ((*y)*log((*y))*(-1));
    }
    if (choix == 5){
        return k*Tamb-k*(*y);
    }
}


void Euler(double y0, int n, int t0, double T, double *t, double *y, double Tamb, int choix){
    int i;
    double h,k;
    h = (T-t0)/n;
    y[0] = y0;                  //*y = y0
    t[0] = t0;                  //*t = t0
    for(i=0;i<n;i++){
        //y[i+1] = y[i] + h*(t[i]*(Tamb - y[i]));
        k = f(&t[i],&y[i],Tamb,choix);
        y[i+1] = y[i] + h*k;
        t[i+1] = t[i] + h;

    }

}

void afficher(double *t, double *y, int n){
    int i;
    for(i=0;i<n;i++){
        printf("%f \n",t[i+1]);                               //Ou bien *(t+i)
        printf("%f \n",y[i+1]);                               //Ou bien *(y+i)
    }

}

void solexacte(double *t, double *sol, int choix, double lamda, int n, double Tamb){
    int i;
    if (choix == 1){
        for(i=0;i<n; i++){ 
            sol[i] = lamda*exp(-(0.5*t[i]*t[i]))+Tamb;
    
        }
    }
    else if (choix == 2){
        for(i=0;i<n; i++){ 
            sol[i] = lamda*exp(t[i]*(1-log(t[i])))+Tamb;

        }
    }
    else if (choix == 3){
        for(i=0;i<n; i++){ 
            sol[i] = lamda / (1+(log(t[i])*log(t[i])))+Tamb;

        }
    }
    else if (choix == 4){
        for(i=0;i<n; i++){
            sol[i] = exp(lamda*exp(-t[i]));            
        }
    } 
    else if (choix == 5){
        for(i=0;i<n; i++){
            sol[i] = lamda*exp(-k*t[i])+Tamb;            
        }
    }   
}

int main(){
    double Tamb, y0, T,lamda;
    int n, choix, t0;
    n = 10;
    printf("Le nombre d'itr : ");
    scanf(" %d",&n);
    double *t, *y, *sol;
    t = (double*)malloc(n*sizeof(double));
    y = (double*)malloc(n*sizeof(double));
    sol = (double*)malloc(n*sizeof(double));
    printf("La fonction de K(t,y(t)):\n 1/ t\n 2/ ln(t)\n 3/ 2*ln(t))/(t*(1+ln(t)*ln(t))\n 4/ y(t)*ln(y(t))/(y(t)−Tamb)\n 5/ K est constante\n Votre choix : ");
    scanf("%d",&choix);
    printf("La temperature de la piece : ");
    scanf(" %lf",&Tamb);
    printf("La temperature initiale : ");
    scanf("\n %lf",&y0);
    printf("Le temp final : ");
    scanf("%lf\n",&T);

    if (choix == 1){
        t0 = 0;
        lamda = y0 - Tamb;
    }
    else if (choix == 2){
        t0 = 1;
        lamda = (y0 - Tamb)*exp(-1);
    }
    else if (choix == 3){
        t0 = 1;
        lamda = y0 - Tamb;
    }
    else if (choix == 4){
        t0 = 0;
        lamda = log(y0); 
    }
    else if (choix == 5){
        printf("Le K est une constante\n Donner une valeur de k : ");
        scanf("%d",&k);
        t0 = 0;
        lamda = y0 - Tamb;
    }
    
    Euler(y0,n,t0,T,t,y,Tamb,choix);
    //afficher(t,y,n);
    for(int i=0;i<n; i++)
        printf("Le resultat de la solution Euler Y[%.2f] = %lf \n",t[i],y[i]);
    solexacte(t,sol,choix,lamda,n,Tamb);
    //afficher(t,sol,n);
    printf("------------------------------------------------------------------\n");
    for(int i=0;i<n; i++)
        printf("Le resultat de la solution exacte sol[%.2f] = %lf \n",t[i],sol[i]);

}
