#include<stdio.h>
void main(){
	int a [100];
	int c[100];
	int b;
	int i;
	int j;
	int n;
	int k=0;
	
	printf(" enter the legth of array(<100)= \n");
	scanf("%d",&n);
	
	printf(" enter the elements of an array = \n");
	for (i=0; i<n;i++)
	{
		printf(" enter-\n");
		scanf("%d",&a[i]);
	}
	
	printf(" enter the target number \n");
	scanf("%d",&b);
	
	for(i=0;i<n;i++)
	{
		for(j=i+1; j<n; j++)
		{
			if(a[i]+a[j]==b)
			{
				c[k]=i;
				k=k+1;
				c[k]=j;
				
			}
			
		}
	}
	
	printf(" the indices are=\n");
	for(i=0;i<=k;i++)
	{

		printf("%d  ",c[i]);
	}
	
}
