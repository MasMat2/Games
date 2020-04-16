
#include <stdio.h>

int main(){
  int num_alum;
  float cal[' '];
  int aprob=0, mayor=0, i;
  float sum=0, prom, per_aprob;

  printf("Ingrese el numero de aspirantes: ");
  scanf("%d", &num_alum);
  for(i=0; i<num_alum; i++){
    printf("Ingrese la calificacion del aspirante %d: ", i+1);
    scanf("%f", &cal[i]);
  }
  for(i=0; i<num_alum; i++){
    sum += cal[i];
    if (cal[i]>=1300){
      aprob += 1;
    }
    if (cal[i]>=1500){
      mayor++;
    }
  }
  prom = sum/num_alum;
  per_aprob = (float) aprob/num_alum;
  printf("El promedio de los alumnos es de %.2f\n", prom);
  printf("El porcentaje de aporbados es de %.2f\n", per_aprob);
  printf("El numero de estudiantes con una claificacion alta es de %d\n", mayor);
}
