#include <stdio.h>

int main(void) {
    int n,*a,x,l=0,flag=0;
	scanf("%d",&n);
	a =(int *) malloc(sizeof(int)*n);
	for(int i=0;i<n;i++){
	    scanf("%d",&x);
	    l = (l>x?l:x);
	    a[x]++;
	    if(a[x]>1){
	        flag=1;
	    }
	}
	if(flag==0){
	        printf("unique");
	}
	else{
	for(int i=0;i<=l;i++){
	  if(a[i]>1)
	  printf("%d ",i);
	  
	}}
	return 0;
}

