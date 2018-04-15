#include <stdio.h>

int main(void) {
    int n,x,flag=0;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
	    scanf("%d",&x);
	    if(x==i){
	     printf("%d ",x);
	        flag=1;
	    } 
	}
	if(flag==0){
	    printf("-1");
	}
	return 0;
}

