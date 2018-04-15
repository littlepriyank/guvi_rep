#include <stdio.h>

int main(void) {
    int n,*a,x,l=0,flag=0;
	scanf("%d",&n);
	a =(int *) malloc(sizeof(int)*n);
	for(int i=0;i<n;i++){
	    scanf("%d",&x);
	    l = (l>x?l:x);
	    a[x]++;
	    if(x!=0 && a[x]>0)
	    flag=1;
	}
	if(flag==1)
	for(int i=l;i>=0;i--){
	  if(a[i]>0){
	  for(int j=1;j<=a[i];j++)
	    printf("%d",i);
	  
	}}
	else
	printf("0");
	return 0;
}

