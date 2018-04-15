#include <stdio.h>

int main(void) {
    int n,*a,x,l=0,flag=0;
	scanf("%d",&n);
	if(n%2==0)
	    printf("Wrong Inputs");
	else{    
	a =(int *) malloc(sizeof(int)*n);
	for(int i=0;i<n;i++){
	    scanf("%d",&x);
	    l = (l>x?l:x);
	    a[x]++;
	}
	for(int i=0;i<=l;i++){
	    if(a[i]==1)
	        {
	            printf("%d",i);
	            break;
	        }
	}}
	return 0;
}

